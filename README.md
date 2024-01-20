# DFCPS

Overall structure of the DFCPS:

![image](img/structure.png)

Model renderings:

![image](img/comparison.png)

## 1. Installation

### (1) Create a conda environment:

```
$ conda env create -f semiseg.yaml
$ conda activate semiseg
```

### (2) Install apex 0.1 (requires CUDA)

```
$ cd . /furnace/apex
$ python setup.py install --cpp_ext --cuda_ext
```

The implementation of our model code references [TorchSemiSeg](https://github.com/charlesCXK/TorchSemiSeg), which you can also refer to for further details by checking out this model.

## 2. Data Preparation

support the import of medical image datasets, including CT scans, MRI images, etc., this time using the Kvasir-SEG dataset for segmentation, if necessary, you can replace the dataset.

## 3. Training and Inference

```
$ cd . /exp.voc/voc8.res50v3+.CPS+DFCPS
$ bash script.sh
```
- The tensorboard file is saved in `log/tb/` directory.
- In `script.sh`, you need to specify some variables, such as the path to your data dir, the path to your snapshot dir that stores checkpoints, etc.

## 4. Different Partitions
To try other data partitions beside 1/8, you just need to change two variables in `config.py`:

```
C.labeled_ratio = 8
C.nepochs = 34
```

Please note that, for fair comparison, we control the total iterations during training in each experiment similar (almost the same), including the supervised baseline and semi-supervised methods. Therefore, the nepochs for different partitions are different.

## 5. Citation

```
Yifei Chen
```