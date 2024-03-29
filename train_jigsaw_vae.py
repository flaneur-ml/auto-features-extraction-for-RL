#!/usr/bin/env python
# coding: utf-8


from torch import optim

from src.args import args
from src.features_extraction import JigsawVAE, JigsawVAELossFunction
from src.utils import get_fixed_hyper_param, train_ae, get_device, game_data_loaders

device = get_device()
batch_size, num_of_channels, input_size, z_dim = get_fixed_hyper_param(args['hyper_parameters'])

DO_TRAIN = True

model = JigsawVAE(z_dim, num_of_channels, input_size).to(device)
loss = JigsawVAELossFunction()
optimizer = optim.Adam(model.parameters())

dataloaders = game_data_loaders()
train_loaders, val_loaders = dataloaders['train'], dataloaders['val']

if DO_TRAIN:
    num_epochs = int(3e3)
    train_ae(num_epochs, model, dataloaders['train'], dataloaders['val'], optimizer, device, loss)
