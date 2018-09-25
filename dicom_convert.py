import argparse
import os
import dicom
import numpy as np
from skimage.transform import resize


def convert_dicom(d, size, output_direc):
    file = dicom.read_file(d)
    a = file.pixel_array
    out = resize(a, [size[0], size[1]])

    filename = str.split(d, "/")[-4]  # get the image name
    save_path = os.path.join(output_direc, filename)
    np.save(file=save_path, arr=out)


if __name__=="__main__":
    parser = argparse.ArgumentParser(description='Process Dicom Images to Numpy Arrays')
    parser.add_argument('-img', dest='img', type=str, help='path to a single dicom image')
    parser.add_argument('-s', dest='size', help='a tuple of output array size ', default=(299, 299))
    parser.add_argument('-o', dest='output_direc', help='directory of the output', default="./")
    parser.add_argument('-cbis', dest="cbis")
    args = parser.parse_args()

    if not os.path.exists(args.output_direc):
        os.mkdir(args.output_direc)
    if args.img:
        convert_dicom(d=args.img, size=args.size, output_direc=args.output_direc)
    # Internal use
    if args.cbis:
        for f in os.listdir(args.cbis):
            path = os.path.join(args.cbis, f)
            if os.path.isdir(path):
                while True:
                    try:
                        x = os.listdir(path)
                    except NotADirectoryError:
                        break
                    next_dir = x[-1]
                    path = os.path.join(path, next_dir)
                convert_dicom(d=path, size=args.size, output_direc=args.output_direc)
