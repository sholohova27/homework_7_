import os
import shutil
import sys
from pathlib import Path
from normalize import normalize
from delete import delete


def get_path():
    path = None
    try:
        path = Path(sys.argv[1])# путь к папке, в которой находится скрипт
    except IndexError:
        print("Type path to folder")
    return path

    if path and path.exists():
        return path
    else:
        print("Path not exists")

    return path


def main(path_):
    p = path_
    images = []
    video = []
    docs = []
    audio = []
    archive = []
    reports = []
    unknown = []
    requests = []
    dir_suf = set()
    unknown_suf = set()
    for i in p.iterdir():
        norm = normalize(i.name)
        os.replace(os.path.join(path_, i.name), os.path.join(path_, norm))
        if i.is_file():
            if i.suffix.upper().lstrip('.') in ('JPEG', 'PNG', 'JPG', 'SVG'):
                images.append(i.name)
                dir_suf.add(i.suffix.lstrip('.').upper())
                images_path = os.path.join(path_, 'Images')
                try:
                    os.mkdir(images_path)
                except FileExistsError:
                    pass
                try:
                    shutil.move(os.path.join(path_, i), images_path)
                except AttributeError:
                    pass
            elif i.suffix.upper().lstrip('.') in ('AVI', 'MP4', 'MOV', 'MKV'):
                video.append(i.name)
                dir_suf.add(i.suffix.lstrip('.').upper())
                video_path = os.path.join(path_, 'Video')
                try:
                    os.mkdir(video_path)
                except FileExistsError:
                    pass
                try:
                    shutil.move(os.path.join(path_, i), video_path)
                except AttributeError:
                    pass
            elif i.suffix.upper().lstrip('.') in ('CSV', 'DOC', 'DOCX', 'TXT', 'PDF', 'XLS', 'XLSX', 'XLSB', 'PPTX'):
                docs.append(i.name)
                dir_suf.add(i.suffix.lstrip('.').upper())
                docs_path = os.path.join(path_, 'Docs')
                try:
                    os.mkdir(docs_path)
                except FileExistsError:
                    pass
                try:
                    shutil.move(os.path.join(path_, i), docs_path)
                except AttributeError:
                    pass
            elif i.suffix.upper().lstrip('.') in ('MP3', 'OGG', 'WAV', 'AMR'):
                audio.append(i.name)
                dir_suf.add(i.suffix.lstrip('.').upper())
                audio_path = os.path.join(path_, 'Audio')
                try:
                    os.mkdir(audio_path)
                except FileExistsError:
                    pass
                try:
                    shutil.move(os.path.join(path_, i), audio_path)
                except AttributeError:
                    pass
            elif i.suffix.upper().lstrip('.') in ('ZIP', 'GZ', 'TAR', 'RAR'):
                archive.append(i.name)
                dir_suf.add(i.suffix.lstrip('.').upper())
                archive_path = os.path.join(path_, 'Archives')
                try:
                    os.mkdir(archive_path)
                except FileExistsError:
                    pass
                try:
                    shutil.move(os.path.join(path_, i), archive_path)
                    shutil.unpack_archive(i)  # не распаковывает rar
                except AttributeError:
                    pass
                except shutil.ReadError:
                    pass
            elif i.suffix.upper().lstrip('.') == 'SQL':
                requests.append(i.name)
                dir_suf.add(i.suffix.lstrip('.').upper())
                sql_path = os.path.join(path_, 'Requests')
                try:
                    os.mkdir(sql_path)
                except FileExistsError:
                    pass
                try:
                    shutil.move(os.path.join(path_, i), sql_path)
                except AttributeError:
                    pass
            elif i.suffix.upper().lstrip('.') in ('TWBX', 'TWB'):
                reports.append(i.name)
                dir_suf.add(i.suffix.lstrip('.').upper())
                reports_path = os.path.join(path_, 'Reports')
                try:
                    os.mkdir(reports_path)
                except FileExistsError:
                    pass
                try:
                    shutil.move(os.path.join(path_, i), reports_path)
                except AttributeError:
                    pass
            else:  # Почему не сработал else c if вместо c elif во всех случаях?
                # Он тогда почему-то включает в себя файлы из других категорий!
                unknown.append(i.name)
                unknown_suf.add(i.suffix.lstrip('.').upper())
                others_path = os.path.join(path_, 'Others')
                try:
                    os.mkdir(others_path)
                except FileExistsError:
                    pass
                try:
                    shutil.move(os.path.join(path_, i), others_path)
                except AttributeError:
                    pass
        if i.is_dir() and i.name not in (
        'Images', 'Video', 'Docs', 'Audio', 'Archives', 'Requests', 'Reports', 'Others'):
            main(os.path.join(path_, i.name))
            delete(path_)
    categories = {
        'Images': images,
        'Video': video,
        'Docs': docs,
        'Audio': audio,
        'Archives': archive,
        'Requests': requests,
        'Reports': reports,
        'Others': unknown,
        'Dir_suf': dir_suf,
        'Other_suf': unknown_suf
    }
    categories_in_dir = {p: categories}
    for key, value in categories_in_dir.items():
        print(key)
        for key, value in categories.items():
            print(key, value)


if __name__ == "__main__":
    _path_ = get_path()
    if _path_:
        main(_path_)