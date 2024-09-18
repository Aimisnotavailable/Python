import os

class FileOrganizer:

    def __init__(self, path) -> None:
        self.path = path
        self.folder_type = {'images': ['png', 'jpg', 'jpeg'],
                       'documents': ['txt', 'doc', 'docx', 'ppt', 'pptx', 'xlsx', 'pdf'],
                       'videos': ['mp4', 'mov', 'mkv'],
                       'shortcuts': ['lnk'],
                       }

        self.folder_list = ['images', 'documents', 'videos', 'shortcuts', 'folders', 'other_files']

    def create_wd(self):
        for folder in self.folder_list:
            path = f"{folder}_main"
            if not os.path.isdir(path):
                os.system(f'mkdir {folder}_main')

    def organize(self) -> None:
        for path in os.listdir(self.path):
            f_path = f"{self.path}/{path}"
            dir_type = f_path.split('_')[-1]
            if dir_type != 'main':
                if not os.path.isdir(f_path):
                    f_type = path.split('.')[-1]
                    moved = False
                    if f_type != 'py':
                        for folder in self.folder_type:
                            if f_type in self.folder_type[folder]:
                                print(f_path)
                                self.move(source=f"\"{path}\"", dest=f"\"{folder}_main\"")
                                break
                        self.move(source=f"\"{path}\"", dest=f"\"other_files_main\"")
                else:
                    self.move(source=f"\"{path}\"", dest=f"\"folders_main\"")



    def move(self, source='', dest='') -> None:
        print(f'move {source} {dest}')
        os.system(f'move {source} {dest}')

if __name__ == '__main__':
    FileOrganizer(os.getcwd()).create_wd()
    FileOrganizer(os.getcwd()).organize()

