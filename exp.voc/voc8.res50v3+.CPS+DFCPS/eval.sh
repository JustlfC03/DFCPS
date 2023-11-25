#!/usr/bin/env bash
nvidia-smi
export NGPUS=8
export OUTPUT_PATH="/home/lmz/lmz/TorchSemiSeg-main/TorchSemiSeg-main/exp.voc/voc8.res50v3+.CPS/results"
export snapshot_dir=$OUTPUT_PATH/snapshot

export TARGET_DEVICE=$[$NGPUS-1]
python eval.py -e 20-34 -d 0-$TARGET_DEVICE --save_path $OUTPUT_PATH/results

# following is the command for debug
# export NGPUS=1
# export batch_size=2
# python -m torch.distributed.launch --nproc_per_node=$NGPUS train.py --debug 1