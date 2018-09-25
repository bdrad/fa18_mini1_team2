import numpy as np
import pandas as pd
import dicom
import os
from skimage.transform import resize
import argparse


class DicomReader:
    def __init__(self, train_or_test):
        self.train_or_test = train_or_test
        if train_or_test == 'train':
            self.files = os.listdir('training/CBIS-DDSM')
        else:
            self.files = os.listdir('test/CBIS-DDSM')
        self.curr = 0

    def next_file(self, dim1, dim2):
        # Grab the image
        path = 'training/CBIS-DDSM/' + self.files[self.curr]
        self.curr += 1
        while True:
            try:
                x = os.listdir(path)
            except NotADirectoryError:
                break
            next = x[0]
            path = path + '/' + next

        file = dicom.read_file(path)
        a = file.pixel_array
        out = resize(a, [dim1, dim2])

        # Grab the patient ID
        p_id = ''
        for i in range(len(path)):
            if path[i:i + 2] == 'P_':
                p_id = path[i:i + 7]
                break
        # Grab breast density given p_id
        c = pd.read_csv('mass_case_description_' + self.train_or_test + '_set.csv')
        a = c['patient_id']
        b = c['breast_density']
        x = -1
        for i in range(len(a)):
            if a[i] == p_id:
                x = i
                break
        return [out, b[i]]

    def training_input(self, dim1, dim2, batch_size=None):
        inputs = []
        labels = []
        if batch_size:
            for _ in range(batch_size):
                x = self.next_file(dim1, dim2)
                inputs.append(x[0])
                labels.append(x[1])
        else:
            while self.curr != len(self.files):
                x = self.next_file(dim1, dim2)
                inputs.append(x[0])
                labels.append(x[1])
        return inputs, labels
