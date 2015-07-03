#!/bin/bash

source env.sh
ps aux | grep w_run | grep -v grep
pkill -9 -f w_run

SFX=.d$$
if [ -d traj_segs ]; then mv traj_segs{,$SFX}; fi
if [ -d seg_logs ]; then mv seg_logs{,$SFX}; fi
if [ -d istates ]; then mv istates{,$SFX}; fi
rm -Rf traj_segs$SFX seg_logs$SFX istates$SFX & disown %1
rm -f west.h5
mkdir seg_logs traj_segs istates


echo "running on node: $HOSTNAME" || exit 1
echo "shell is $SHELL" || exit 1

export WEST_SIM_ROOT="$PWD"

export PYTHONPATH=.

cd "$WEST_SIM_ROOT"
SIM_FILES=$(eval ls bstates)

cp -r bstates/* istates/
cp -r bstates/* "$WEST_SIM_ROOT"

BSTATE_ARGS="--bstate=well1,1,${MODEL_NAME}"
"$WEST_ROOT/bin/w_init" $BSTATE_ARGS --work-manager=threads --n-workers=8 "$@"

