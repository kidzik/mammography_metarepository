import pydicom as dicom
ds = dicom.read_file("/home/kidzik/workspace/mammography_metarepository/sample_data/images_dcm/0002.DCM")

print(ds[(0x0028,0x1352)])
