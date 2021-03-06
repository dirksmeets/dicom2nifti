import logging
import nibabel
import numpy


def ground_thruth_filenames(input_dir):
    nifti_file = input_dir + '_ground_truth.nii.gz'
    reoriented_nifti_file = input_dir + '_ground_truth_reoriented.nii.gz'
    bval_file = input_dir + '_ground_truth.bval'
    bvec_file = input_dir + '_ground_truth.bvec'
    return nifti_file, reoriented_nifti_file, bval_file, bvec_file


def compare_nifti(nifti_file_1, nifti_file_2):
    logging.info("%s %s" %(nifti_file_1, nifti_file_2))
    nifti_1 = nibabel.load(nifti_file_1)
    nifti_2 = nibabel.load(nifti_file_2)

    # check the affine
    if not (nifti_1.affine == nifti_2.affine).all():
        logging.warning('affine mismatch')
        return False

    # check the data
    if nifti_1.get_data_dtype() != nifti_2.get_data_dtype():
        logging.warning('dtype mismatch')
        return False
    if not (nifti_1.get_data() == nifti_2.get_data()).all():
        logging.warning('data mismatch')
        return False

    return True


def compare_bval(bval_file_1, bval_file_2):
    bval_1 = numpy.loadtxt(bval_file_1)
    bval_2 = numpy.loadtxt(bval_file_2)
    return numpy.array_equal(bval_1, bval_2)


def compare_bvec(bvec_file_1, bvec_file_2):
    bvec_1 = numpy.loadtxt(bvec_file_1)
    bvec_2 = numpy.loadtxt(bvec_file_2)
    return numpy.array_equal(bvec_1, bvec_2)
