import os


def check_dataset(dataset_root_dir='../dataset'):
    if not os.path.exists(dataset_root_dir + '/Fruit And Vegetable Diseases Dataset'):
        print('Dataset not found, checking directory...')
        if not os.path.exists(dataset_root_dir): os.mkdir(dataset_root_dir)
        if not os.path.isfile(dataset_root_dir + '/archive.zip'):
            print('Downloading archive...')
            import boto3
            from botocore import UNSIGNED
            from botocore.config import Config
            bucket_name = 'aai-university-content'
            endpoint = 'https://s3.fr-par.scw.cloud'
            file_key = 'archive2.zip'
            local_file = dataset_root_dir + '/archive.zip'
            s3 = boto3.client('s3', endpoint_url=endpoint, config=Config(signature_version=UNSIGNED))
            s3.download_file(bucket_name, file_key, local_file)
            print('Archive download complete.')

        print('Archive found, extracting archive...')
        from zipfile import ZipFile
        with ZipFile(dataset_root_dir + "/archive.zip", 'r') as zip_ref:
            zip_ref.extractall(path=dataset_root_dir)
        print('Archive extraction complete.')
        print('Removing archive...')
        os.remove(dataset_root_dir + '/archive.zip')
        print('Archive removed.')
    print('Dataset found.')


def get_class_names(dataset_root_dir):
    check_dataset(dataset_root_dir)
    return sorted([x for x in os.listdir(dataset_root_dir + '/Fruit And Vegetable Diseases Dataset') if
                   os.path.isdir(os.path.join(dataset_root_dir + '/Fruit And Vegetable Diseases Dataset', x))])
