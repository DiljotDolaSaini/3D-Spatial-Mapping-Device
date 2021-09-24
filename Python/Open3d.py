import numpy as np
import open3d as o3d

#Diljot Dola Saini
#4000252842
#dolasaid

#Create Point Cloud
pcd = o3d.io.read_point_cloud("measurements.xyz",format='xyz')
print(pcd)

#print(np.asarray(pcd.points))
o3d.visualization.draw_geometries([pcd])


pt = 0
lines = []

#This is to connect the points in each plane 
for e in range(10): #10 planes 
    for x in range(63):
        lines.append([pt,(pt+1)])
        pt+=1

pt = 0
do = 64

#This is to connect each plane with each other 
for f in range(9):  #Stop at 10th plane
    for y in range(63): #64 points in total 
        lines.append([pt,pt+do])
        pt+= 1

#Visualize        
line_set = o3d.geometry.LineSet(points=o3d.utility.Vector3dVector(np.asarray(pcd.points)),lines=o3d.utility.Vector2iVector(lines))
o3d.visualization.draw_geometries([line_set])

#Attempt to create mesh
pcd.estimate_normals()

d = pcd.compute_nearest_neighbor_distance()
avg_distance = np.mean(d)

radius = 2*avg_distance

mesh = o3d.geometry.TriangleMesh.create_from_point_cloud_ball_pivoting(pcd,o3d.utility.DoubleVector([radius, radius*2]))

o3d.visualization.draw_geometries([mesh],point_show_normal = True, mesh_show_wireframe=True, mesh_show_back_face=True)

