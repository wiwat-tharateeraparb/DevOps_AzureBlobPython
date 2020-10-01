# Need to install azure-storage-blob using conda with following command:
# conda install -c anaconda azure 
# conda install -c conda-forge azure-storage-blob
# conda install -c conda-forge azure-nspkg
# Connection string:



import os, uuid, sys
from azure.storage.blob import BlobClient, BlobServiceClient, ContainerClient, PublicAccess, __version__
from azure.storage.blob.blockblobservice import BlockBlobService
import re

account_name = 'dfqualifstoracc'
account_key = 'ACCOUNT_KEY'
connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
#connect_str = 'CONNECTION_STRING'
account_url = 'ACCOUNT_URL'
container_name = 'media-dfpoc1'
file_path = '/raw/FAS/PAT'
#block_blob_service = BlockBlobService(account_name = account_name, account_key = account_key)
#blob_service_client = BlobServiceClient(account_url = account_url)

try:
    print("Azure Blob Storage v" + __version__ + " - Python sample")

    

except Exception as ex:
    print('Exception:')
    print(ex)

# Retrieve the connection string for use with the application. The storage
# connection string is stored in an environment variable on the machine
# running the application called AZURE_STORAGE_CONNECTION_STRING. If the environment variable is
# created after the application is launched in a console or with Visual Studio,
# the shell or application needs to be closed and reloaded to take the
# environment variable into account.





'''
# Create BlobServiceClient object
blob_service_client = BlobServiceClient.from_connection_string(connect_str).get_container_client(container_name)


# process the size of blob
def process_blob_length(blob, total_size):
    total_size += block_blob_service.get_blob_properties(block_blob_service,container_name,blob.name).properties.content_length

def display_blobs(blob):
    print("\t Blob to be copied: " + blob.name )

def process_blob_url(blob):
    blob_url = block_blob_service.make_blob_url(container_name, blob.name, protocol=None, sas_token=None, snapshot=None)
    #print("\t Blob url to be copied: " + blob_url)
    return blob_url

def process_blob_target_name(blob):
    digit_date = re.findall(r"\D(2019\d{4})\D", blob.name)
    syntax_name = "reg2_ur27"
    blob_name_array = blob.name.split(syntax_name)
    if len(digit_date) == 1:
        s = digit_date[0]
        date_name = '/' + s[:4] + '/' + s[4:6]+ "/" + s[-2:]
        target_blob_name = blob_name_array[0] + syntax_name + date_name + blob_name_array[1]
        print (target_blob_name)
    return target_blob_name

def list_filenames_in_blob(blob):
    file_names = []
    blob_iter = blob_service_client.list_blobs(name_starts_with=file_path)
    for blob in blob_iter:
        file_names.append(blob.name)
    return file_names


def run_action():
    try:
        """
        Initial try to write a file in local then upload to the container in CIP blob account
        Create a similar environment of prod before managing all blobs
        # Create a file in Documents to test the upload and download.
        local_path=os.path.expanduser("D:/AIVI/azure-blob-storage/")
        local_file_name="PLZUR27_        _20190701-193113.json"
        blob_container_file_path = os.path.join("test/FIS/", local_file_name)
        full_path_to_file =os.path.join(local_path, local_file_name)
        # Test rite text to the file.
        file = open(full_path_to_file,  'w')
        file.write("Hello, World!")
        file.close()
        print("Temp file = " + full_path_to_file)
        print("\nUploading to Blob storage as blob" + local_file_name)
        # Upload the created file, use local_file_name for the blob name
        block_blob_service.create_blob_from_path(container_name, blob_container_file_path, full_path_to_file)
        """
        file_names_list = []

        # List the blobs in the container
        print("\nList blobs in the container")
        generator = block_blob_service.list_blobs(container_name)

        for blob in generator:
            file_names_list = list_filenames_in_blob(blob)
            print(file_names_list)
            return file_names_list
            
            if blob.name.startswith('raw'):
                display_blobs(blob)

                # The storage explorer has static features, so comment this method
                # process_blob_length(blob)

                # Copy blob from source to destination, but cut.
                block_blob_service.copy_blob(
                    container_name,
                    process_blob_target_name(blob),
                    process_blob_url(blob),
                )
            

        

    except Exception as e:
        print(e)

# Main method.
if __name__ == '__main__':
    run_action()
'''
