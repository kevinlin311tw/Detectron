CUDA_VISIBLE_DEVICES=3 python tools/infer_simple_ava.py \
--cfg /data/caffe2/detectron-old/configs/getting_started/ava_mini_1gpu_e2e_faster_rcnn_R-50-FPN.yaml  \
--output-dir ../detectron-mini-ava   \
--image-ext jpg   \
--wts /data/caffe2/detectron-old/tmp/ava-output/train/ava_mini_train/generalized_rcnn/model_final.pkl \
/data/dataset/AVA/mini-ava-test
