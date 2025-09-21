ICSPTrack

<!-- [![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/seqtrack-sequence-to-sequence-learning-for/visual-object-tracking-on-tnl2k)](https://paperswithcode.com/sota/visual-object-tracking-on-tnl2k?p=seqtrack-sequence-to-sequence-learning-for)
[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/seqtrack-sequence-to-sequence-learning-for/visual-object-tracking-on-lasot)](https://paperswithcode.com/sota/visual-object-tracking-on-lasot?p=seqtrack-sequence-to-sequence-learning-for)
[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/seqtrack-sequence-to-sequence-learning-for/visual-object-tracking-on-lasot-ext)](https://paperswithcode.com/sota/visual-object-tracking-on-lasot-ext?p=seqtrack-sequence-to-sequence-learning-for)
[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/seqtrack-sequence-to-sequence-learning-for/visual-object-tracking-on-trackingnet)](https://paperswithcode.com/sota/visual-object-tracking-on-trackingnet?p=seqtrack-sequence-to-sequence-learning-for)
[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/seqtrack-sequence-to-sequence-learning-for/visual-object-tracking-on-got-10k)](https://paperswithcode.com/sota/visual-object-tracking-on-got-10k?p=seqtrack-sequence-to-sequence-learning-for)
[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/seqtrack-sequence-to-sequence-learning-for/visual-object-tracking-on-uav123)](https://paperswithcode.com/sota/visual-object-tracking-on-uav123?p=seqtrack-sequence-to-sequence-learning-for)
[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/seqtrack-sequence-to-sequence-learning-for/visual-object-tracking-on-needforspeed)](https://paperswithcode.com/sota/visual-object-tracking-on-needforspeed?p=seqtrack-sequence-to-sequence-learning-for) -->




<p align="center">
  <img width="85%" src="assets/arch.png" alt="Framework"/>
</p>

ICSPTrack is a simple and high performance tracker. 




## Install the environment
```
conda create -n icsptrack python=3.8
conda activate icsptrack
bash install.sh
```


## Data Preparation
Put the tracking datasets in ./data. It should look like:
   ```
   ${PROJECT_ROOT}
    -- data
        -- lasot
            |-- airplane
            |-- basketball
            |-- bear
            ...
        -- got10k
            |-- test
            |-- train
            |-- val
        -- coco
            |-- annotations
            |-- images
        -- trackingnet
            |-- TRAIN_0
            |-- TRAIN_1
            ...
            |-- TRAIN_11
            |-- TEST
   ```


## Set project paths
Run the following command to set paths for this project
```
python tracking/create_default_local_file.py --workspace_dir . --data_dir ./data --save_dir ./output
```
After running this command, you can also modify paths by editing these two files
```
lib/train/admin/local.py  # paths about training
lib/test/evaluation/local.py  # paths about testing
```


## Training
Download pre-trained [MAE HiViT-Base weights](https://drive.google.com/file/d/1VZQz4buhlepZ5akTcEvrA3a_nxsQZ8eQ/view?usp=share_link) and put it under `$PROJECT_ROOT$/pretrained_networks` (different pretrained models can also be used, see [MAE](https://github.com/facebookresearch/mae) for more details).

```
python tracking/train.py 
--script icsptrack --config icsptrack-full-256 
--save_dir ./output 
--mode multiple --nproc_per_node 2 
--use_wandb 0
```
```
python tracking/train.py 
--script icsptrack --config icsptrack-full-256 
--save_dir ./output 
--mode multiple --nproc_per_node 2 
--use_wandb 0
```
```

############### Train 256 
python -m torch.distributed.launch --nproc_per_node 2 lib/train/run_training.py --script icsptrack --config icsptrack-full-256 --save_dir ./output --mode multiple --nproc_per_node 2 --use_wandb 0

python -m torch.distributed.launch --nproc_per_node 2 lib/train/run_training.py --script icsptrack --config icsptrack-got-256 --save_dir ./output --mode multiple --nproc_per_node 2 --use_wandb 0


python -m torch.distributed.launch --nproc_per_node 2 lib/train/run_training.py --script icsptrack --config icsptrack-full-384 --save_dir ./output --mode multiple --nproc_per_node 2 --use_wandb 0

```
Replace `--config` with the desired model config under `experiments/icsptrack`.

We use [wandb](https://github.com/wandb/client) to record detailed training logs, in case you don't want to use wandb, set `--use_wandb 0`.


## Test and Evaluation

- GOT10K-test
```
python tracking/test.py  --tracker_param icsptrack-got-256 --dataset got10k_test --threads 20 --num_gpus 2 
 python tracking/test.py  --tracker_param icsptrack-got-256 --dataset got10k_test --threads 2 --num_gpus 2  


python lib/test/utils/transform_got10k.py --tracker_name icsptrack --cfg_name icsptrack-got-256
python lib/test/utils/transform_got10k.py --tracker_name icsptrack --cfg_name icsptrack-got-384
```

- LaSOT or other off-line evaluated benchmarks (modify `--dataset` correspondingly)  # to test change the GPUID
```

######################    Lasot Test 256
python tracking/test.py --tracker_param icsptrack-full-256 --dataset lasot --threads 18 --num_gpus 2    

python tracking/test.py --tracker_param icsptrack-full-256 --dataset lasot --threads 12 --num_gpus 2    
python tracking/test.py --tracker_param icsptrack-full-256 --dataset lasot --threads 2 --num_gpus 2    
python tracking/test.py --tracker_param icsptrack-full-256 --dataset lasot --threads 1 --num_gpus 2    


# lasotExt
python tracking/test.py --tracker_param icsptrack-full-256 --dataset lasot_extension_subset --threads 20 --num_gpus 2
python tracking/test.py --tracker_param icsptrack-full-256 --dataset lasot_extension_subset --threads 10 --num_gpus 2
python tracking/test.py --tracker_param icsptrack-full-256 --dataset lasot_extension_subset --threads 8 --num_gpus 2    
python tracking/test.py --tracker_param icsptrack-full-256 --dataset lasot_extension_subset --threads 4 --num_gpus 2 
   
   
# tnl2k   
python tracking/test.py --tracker_param icsptrack-full-256 --dataset tnl2k --threads 4 --num_gpus 2   
python tracking/test.py --tracker_param icsptrack-full-256 --dataset tnl2k --threads 20 --num_gpus 2    
 
# uav 
python tracking/test.py --tracker_param icsptrack-full-256 --dataset uav --threads 6 --num_gpus 2 
python tracking/test.py --tracker_param icsptrack-full-256 --dataset uav --threads 20 --num_gpus 2 


# otb
python tracking/test.py --tracker_param icsptrack-full-256 --dataset otb --threads 8 --num_gpus 2 
python tracking/test.py --tracker_param icsptrack-full-256 --dataset otb --threads 4 --num_gpus 2 
python tracking/test.py --tracker_param icsptrack-full-256 --dataset otb --threads 2 --num_gpus 2 


# NFS
python tracking/test.py --tracker_param icsptrack-full-256 --dataset nfs --threads 2 --num_gpus 2   
python tracking/test.py --tracker_param icsptrack-full-256 --dataset nfs --threads 4 --num_gpus 2   


          
#####################  
 LaSOT Eval 
python tracking/analysis_results.py # need to modify tracker configs and names
```


- TrackingNet
```

###########     TrackingNet Test 
python tracking/test.py  --tracker_param icsptrack-full-256 --dataset trackingnet --threads 18 --num_gpus 2



python tracking/test.py  --tracker_param icsptrack-full-256 --dataset UAV123

###########      TrackingNet Eval
python lib/test/utils/transform_trackingnet.py --tracker_name icsptrack --cfg_name icsptrack-full-256
python lib/test/utils/transform_trackingnet.py --tracker_name icsptrack --cfg_name icsptrack-full-384
```



## Test FLOPs, and Speed
*Note:* The speeds reported in our paper were tested on a single 4090 GPU.

```
python tracking/profile_model.py --script icsptrack --config icsptrack-full-256
```


## Acknowledgments
* Thanks for the [OSTrack](https://github.com/botaoye/OSTrack) and [PyTracking](https://github.com/visionml/pytracking) library, which helps us to quickly implement our ideas.


