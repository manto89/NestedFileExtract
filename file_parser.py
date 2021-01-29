import os
import shutil

import patoolib

HOME_PATH = ''


def go_home():
    change_dir(HOME_PATH)


def change_dir(path):
    os.chdir(path)


def go_up():
    os.chdir('..')


def find_zip():
    files = os.listdir()
    zips = []
    for file in files:
        if '.zip' in file:
            zips.append(file)
    return zips


def find_rar(path):
    files = os.listdir(path)
    rars = []
    for file in files:
        if '.rar' in file:
            rars.append(file)
    return rars


def extract(zip_path, output_dir):
    return patoolib.extract_archive(zip_path, outdir=output_dir, interactive=False)


def parse_file(path):
    first_file = True
    for line in open(path, 'r').readlines():
        if line[0] == '.':
            go_home()
            change_dir(line[:-1])
            first_file = True
        else:
            if not first_file:
                go_up()
            first_file = False
            change_dir(line[:-1])
            zip_paths = find_zip()
            zip_output_path = os.path.join(HOME_PATH, 'rar')
            rar_file = ''
            for zip_path in zip_paths:
                temp_rar_file = extract(zip_path, zip_output_path)
                if rar_file == '':
                    rars = find_rar(os.path.join(HOME_PATH, temp_rar_file))
                    if len(rars) > 0:
                        rar_file = os.path.join(HOME_PATH, temp_rar_file, rars[0])
                    else:
                        raise Exception('unable to find extracted rar file from ' + temp_rar_file)
            rar_output_folder = os.path.join(HOME_PATH, 'res')
            if not os.path.exists(rar_output_folder):
                os.mkdir(rar_output_folder)
            final_folder = extract(rar_file, rar_output_folder)
            final_filename = os.listdir(final_folder)[0]
            shutil.rmtree(zip_output_path)
            output_folder = os.path.join(HOME_PATH, 'output')
            if not os.path.exists(output_folder):
                os.mkdir(output_folder)
            final_file = os.path.join(output_folder, final_filename)
            shutil.copy(final_file, final_file)
            shutil.rmtree(rar_output_folder)
            print(final_file)
