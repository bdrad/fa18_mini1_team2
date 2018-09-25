# fa18_mini1_team2
## Breast Mammography Multi-Classification of Breast Density
Credits to: Mian, Vishnu

Description: This project uses data from the Digital Database for Screening Mammography to train a classifier which determines the breast density given a mammography dicom image. 

This repo contains a python script to convert dicom image to numpy array, and a jupyter notebook with a ResNet50 trained on 100+ mammography samples. It does not aim for accuracy, but a walk-a-through to use tensorflow/keras to build such networks.
 ## Required Libraries
 Keras, Numpy, Pandas

 ## Convert Dicom Image
 Use `dicom_convert.py` to convert a single dicom image into numpy array with given
 input image path and desired output size. The default output size is (299, 299), and
 the default output directory is current directory.

 Example Use:
 `python3 dicom_convert.py -img path/to/your/img.dcm -s (224, 224) -o ./train_np/`
 ## ResNet50 Training
 Use `ResNest50.ipynb` to run the training and testing process.
