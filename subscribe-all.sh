#!/bin/bash
poolIds=$(subscription-manager list --all --available | grep 'Pool ID' | awk '{print $3}')
args="attach --quantity=1 "

for poolId in ${poolIds[@]}; do
        args="$args --pool=$poolId"
done

echo "$args"
eval subscription-manager "$args"
