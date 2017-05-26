import numpy as np
import trimesh
mesh = trimesh.load_mesh("shark.ply")

# is the current mesh watertight?
print(mesh.is_watertight)

# what's the euler number for the mesh?
print(mesh.euler_number)

# lets get a convex hull of the mesh
hull = mesh.convex_hull

# since the mesh is watertight, it means there is a
# volumetric center of mass which we can set as the origin for our mesh
mesh.vertices -= mesh.center_mass

# what's the moment of inertia for the mesh?
print(mesh.moment_inertia)

# find groups of coplanar adjacent faces
facets, facets_area = mesh.facets(return_area=True)

# set each facet to a random color
for facet in facets:
    mesh.visual.face_colors[facet] = trimesh.visual.random_color()

# preview mesh in an opengl window if you installed pyglet with pip
mesh.show()

