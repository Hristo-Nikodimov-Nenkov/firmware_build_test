from uos import listdir, mkdir

def file_exists(path:str):
    try:
        with open(path, "r"):
            return True
    except:
        return False
    
def directory_exists(path:str):
    try:
        listdir(path)
        return True
    except:
        return False

def mkdirs(path:str):
    segments = path.split("/")
    segment = segments.pop(0)
    
    created_path = ""
    while len(segments):
        created_path += "/"
        segment = segments.pop(0)

        created_path += segment
        
        if not directory_exists(created_path):
            mkdir(created_path)