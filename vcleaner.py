#!/usr/bin/env python

import sys
from argparse import ArgumentParser
from os import mkdir
from os.path import dirname, join, exists, basename

from vrm.cleaner import clean
from vrm.debug import print_stat
from vrm.vrm import load


def main(argv):
    from vrm.version import app_name
    parser = ArgumentParser()
    parser.add_argument('path', help='VRM file.')
    parser.add_argument('-f', '--force', action='store_true', help='Overwrite file if already exists same file.')
    parser.add_argument('-V', '--version', action='version', version=app_name())
    opt = parser.parse_args(argv)

    path = opt.path
    print(path)

    # vrm読み込み
    vrm = load(path)

    print_stat(vrm.gltf)

    vrm.gltf = clean(vrm.gltf)

    print('-' * 30)
    print_stat(vrm.gltf)

    save_dir = join(dirname(path), 'result')
    if not exists(save_dir):
        mkdir(save_dir)  # 出力先作成

    save_path = join(save_dir, basename(path))
    # 上書き確認
    if not opt.force and exists(save_path):
        if input('Already exists file. Overwrite?(y/N):').lower() not in ['y', 'yes']:
            return

    # vrm保存
    vrm.save(save_path)
    print('saved.')


if __name__ == '__main__':
    main(sys.argv[1:])
