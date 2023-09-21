from files import Task_7 as hf

if __name__ == '__main__':
    print("Переименование txt файлов в каталоге data_files")
    files_cnt = hf.group_rename_files("_fn_", ".txt", path="./Dive_into_Python/Task_7/data_files")
    print(f"Переименовано: {files_cnt}")