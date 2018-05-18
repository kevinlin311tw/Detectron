CUDA_VISIBLE_DEVICES=2 python tools/infer_simple_ava_eval.py \
--cfg configs/ava/ava_mini_1gpu_e2e_faster_rcnn_R-50-FPN.yaml  \
--output-dir ../detectron-ava-eval  \
--image-ext jpg   \
--wts /data/caffe2/myDetectron/ava-output/train/ava_train_multilabel_full/generalized_rcnn/model_iter39999.pkl \
/data/dataset/AVA/preproc/val/keyframes
