#!/usr/bin/python
import sys, yum, re, os, json
from csv import reader

def main():
  source = sys.argv[1]
  dest = sys.argv[2]
  baseDest = sys.argv[3]
  
  yum_vars = get_yum_vars()
  repos = create_repositories(source)
  transformed_repos = render_content_urls(repos, yum_vars, baseDest)
  repo_dict = dict((repo_id, content_url) for repo_id, content_url in transformed_repos)
  write_json(repo_dict, dest)
  
def get_yum_vars():
  base = yum.YumBase()
  return base.conf.yumvar
  
def create_repositories(csv_file):
  with open(csv_file) as f:
    r = reader(f)
    for line in r:
      yield { 'repository_id': line[0], 'content_url': line[1] }
      
def render_content_urls(repo, yum_vars, baseDest):
  """ Replace content_url variables with the expanded path """
  patterns = [
    (re.compile('\$releasever'), 'releasever'),
    (re.compile('\$basearch'), 'basearch'),
    (re.compile('\$arch'), 'arch'),
    (re.compile('\$uuid'), 'uuid')
  ]
  for r in repo:
    content_url = r['content_url'] # create a new content_url that we will transform
    for pattern in patterns: # apply all patterns to our content_url
      content_url = re.sub(pattern[0], yum_vars[pattern[1]], content_url) # Replace any instances of yum variables with the real value
    content_url = os.path.join(baseDest, content_url[1:]) # Strip first '/' character so join works properly
    yield (r['repository_id'], content_url) # Return tuple with valid dest
    
def write_json(repo_dict, dest):
  with open(dest, 'w') as f:
    json.dump(repo_dict, f)
    
if __name__ == '__main__':
  main()
