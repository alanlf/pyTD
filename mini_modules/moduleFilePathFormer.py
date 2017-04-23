import os 

class FilePathFormer():
    def __init__(self,main_directory): 
        path = os.getcwd()
        parameter_length = len(main_directory)
        while not path[-parameter_length:] == main_directory:
            path = (os.path.split(path))[0]
            
        self.main_path = path #Gets path to main directory
        
    def create_path_to_file(self,objects_on_the_path):
        return os.path.join(self.main_path,*objects_on_the_path)
