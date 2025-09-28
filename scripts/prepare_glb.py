# /scripts/prepare_glb.py
import sys, os, trimesh

if len(sys.argv)<3:
    print("Usage: prepare_glb.py input.obj output.glb")
    sys.exit(1)

inp, outp = sys.argv[1], sys.argv[2]
os.makedirs(os.path.dirname(outp), exist_ok=True)

mesh = trimesh.load(inp, force='mesh')
# Se ODM produce una Scene, unisci le geometrie
if isinstance(mesh, trimesh.Scene):
    mesh = trimesh.util.concatenate([g for g in mesh.geometry.values()])
mesh.export(outp)
print("Wrote", outp)
