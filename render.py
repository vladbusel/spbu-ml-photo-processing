import bpy
import argparse
import os
import sys

if '--' in sys.argv:
    argv = sys.argv[sys.argv.index('--') + 1:]
    
    parser = argparse.ArgumentParser()

    parser.add_argument('img', type=str)
    parser.add_argument('normal', type=str)
    parser.add_argument('depth', type=str)

    parser.add_argument('x1', type=float)
    parser.add_argument('y1', type=float)
    parser.add_argument('z1', type=float)
    parser.add_argument('x2', type=float)
    parser.add_argument('y2', type=float)
    parser.add_argument('z2', type=float)

    args = parser.parse_known_args(argv)[0]

    lamp1 = bpy.data.objects['lamp1']
    lamp1.location.x = args.x1
    lamp1.location.y = args.y1
    lamp1.location.z = args.z1

    lamp2 = bpy.data.objects['lamp2']
    lamp2.location.x = args.x2
    lamp2.location.y = args.y2
    lamp2.location.z = args.z2


    bpy.data.images['img'].filepath = args.img
    bpy.data.images['norm'].filepath = args.normal
    bpy.data.images['depth'].filepath = args.depth


    camera = bpy.data.objects['Camera']
    bpy.context.scene.render.filepath = 'result.png'
    bpy.ops.render.render(write_still = True)