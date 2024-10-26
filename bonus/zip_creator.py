import zipfile
import pathlib

def make_archive(filepaths, dest_dir):
    dest_path = pathlib.Path(dest_dir, 'compressed.zip')
    with zipfile.ZipFile(dest_path, 'w') as archive:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            archive.write(filepath, arcname=filepath.name)



if __name__ == '__main__':
    make_archive(['/home/vv/Документи/Навчання/Лекції/Алгоритмізація/2024-2025/src/app1/bonus/e1.py', 'e2.py', 'e3.py', 'e4.py'],'/home/vv/Документи/Навчання/Лекції/Алгоритмізація/2024-2025/src/app1/bonus/dest')