#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Copyright (c) Megvii, Inc. and its affiliates.
import os

from yolox.exp import Exp as MyExp


class Exp(MyExp):
    def __init__(self):
        super(Exp, self).__init__()
        self.depth = 0.33
        self.width = 0.50
        self.exp_name = os.path.split(os.path.realpath(__file__))[1].split(".")[0]

        # Define yourself dataset path
        self.data_dir = "datasets/coco"
        self.train_dir = "train"
        self.val_dir = "val"
        self.train_ann = "train.json"
        self.val_ann = "valid.json"
        self.test_dir = "test"
        self.test_ann = "test.json"

        self.num_classes = 2

        self.max_epoch = 30
        self.data_num_workers = 4
        self.eval_interval = 10
        self.save_history_ckpt = False 

