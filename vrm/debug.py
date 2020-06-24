#!/usr/bin/env python


def print_stat(gltf):
    """
    モデル情報表示
    :param gltf: glTFオブジェクト
    """
    vrm = gltf['extensions']['VRM']
    print('vrm materials:', len(list(vrm['materialProperties'])))
    print('materials:', len(list(gltf['materials'])))
    print('textures:', len(list(gltf['textures'])))
    print('images:', len(list(gltf['images'])))

    meshes = gltf['meshes']
    print('meshes:', len(meshes))
    print('primitives:', sum([len(m['primitives']) for m in meshes]))
    for mesh in meshes:
        print('\t', mesh['name'], ':', len(mesh['primitives']))
