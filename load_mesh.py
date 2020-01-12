from pyrender import Mesh, Scene, Viewer
from io import BytesIO
import numpy as np
import trimesh
import requests

coin = trimesh.load('./models/CHAHIN_COIN.obj')
coinmesh = Mesh.from_trimesh(coin)
scene = Scene(ambient_light=np.array([1.0, 1.0, 1.0, 1.0]))
scene.add(coinmesh)
Viewer(scene)
