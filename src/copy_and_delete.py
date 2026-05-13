import os, shutil
def copy_recursive(src, dst):
    for file in os.listdir(src):
        src_path = os.path.join(src, file)
        dst_path = os.path.join(dst, file)
        if os.path.isfile(src_path):
            shutil.copy(src_path, dst_path)
        elif os.path.isdir(src_path):
            os.mkdir(dst_path)
            copy_recursive(src_path, dst_path)

            
def copy_and_delete(src, dst):
    if os.path.exists(dst):
        shutil.rmtree(dst)
    os.mkdir(dst)
    copy_recursive(src, dst)