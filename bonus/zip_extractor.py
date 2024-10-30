import zipfile

def extract_archive(archpath, dest_dir):
    with zipfile.ZipFile(archpath, 'r') as archive:
        archive.extractall(dest_dir)

if __name__ == '__main__':
    extract_archive('/home/vv/Документи/Навчання/Лекції/Алгоритмізація/2024-2025/src/app1/bonus/output.zip',
                    '/home/vv/Документи/Навчання/Лекції/Алгоритмізація/2024-2025/src/app1/bonus/dest')