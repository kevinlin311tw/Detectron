CUDA_VISIBLE_DEVICES=3 python tools/train_net.py \
    --cfg configs/ava/ava_2gpu_e2e_faster_rcnn_R-50-FPN.yaml \
    OUTPUT_DIR ./ava-output
