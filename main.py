import os
import shutil
import dropbox
from dropbox.files import WriteMode

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token
    
    def upload_Files(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)
        for root, dirs, files in os.walk(file_from):
            for fileName in files:
                local_path = os.path.join(root, fileName)
                relative_path = os.path.relpath(local_path, file_from)
                dropbox_path = os.path.join(file_to, relative_path)
                with open(local_path, 'rb') as f:
                    dbx.files_upload(f.read(), dropbox_path, mode = WriteMode('overwrite'))
    
def main():
    access_token = "Fon3fnuDRjwAAAAAAAAAAY414TA7EdryAgJyBl95tuNmss47B_O9MqAM_KMCQ35E"
    transferdata = TransferData(access_token)
    file_from = str(input("Enter the folder path to be transfered"))
    file_to = str(input("Enter the folder path of the dropbox"))
    transferdata.upload_Files(file_from, file_to)
    print("File has been moved")

main()