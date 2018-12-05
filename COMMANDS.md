# Commands

## Training

python -u run_squad_withemb.py \
    --vocab_file uncased/vocab.txt \
    --bert_config_file preprocessed/bert_config.json \
    --do_train \
    --train_file hotpot/hp_train_full.squad \
    --do_predict \
    --predict_file hotpot/hp_dev_full.squad \
    --train_batch_size 60 \
    --gradient_accumulation_steps 5 \
    --learning_rate 0.0001 \
    --num_train_epochs 50.0 \
    --max_seq_length 2500 \
    --doc_stride 512 \
    --output_dir ./emblog \
    --save_checkpoints_steps 10000

train_batch_size / num_gpu / gradient_accumulation_steps should be between 1-3

## Debug(Overfit small dataset using 1 GPU)

python -u run_squad_withemb.py \
      --vocab_file uncased/vocab.txt \
      --bert_config_file preprocessed/bert_config.json \
      --do_train \
      --train_file hotpot/hp_debug.squad \
      --do_predict \
      --predict_file hotpot/hp_debug.squad \
      --train_batch_size 8 \
      --gradient_accumulation_steps 4 \
      --learning_rate 0.0001 \
      --num_train_epochs 500.0 \
      --max_seq_length 2500 \
      --doc_stride 512 \
      --output_dir ./debug \
      --debug \
      --save_checkpoints_steps 500

##  Evaluate

### 1 Prediction file:

python evaluate_squad --prediction_file {path/to/predictions.json} --dataset_file {path/to/dev_set_used_during_training}

### entire log folder:

Edit eval_all.sh to point to correct log folder

./eval_all.sh

Results are written to results.out file