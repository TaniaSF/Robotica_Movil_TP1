import pandas as pd
from scipy.spatial.transform import Rotation
import yaml
import numpy as np
import matplotlib.pyplot as plt

# Leo ^W\xi_{C_0} del archivo .yaml
yaml_file_path = "../../../MH_01_easy/mav0/cam0/sensor.yaml"
with open(yaml_file_path, 'r') as yaml_file:
    yaml_data = yaml.safe_load(yaml_file)
# Extraigo la matriz:
T_BS_data = yaml_data.get('T_BS', {}).get('data', [])
# Convierto la lista en array NumPy de 4x4:
W_xi_C0 = np.array(T_BS_data).reshape(4, 4)
C0_xi_W = np.linalg.inv(W_xi_C0)

# Leo ^W\xi_{B_0} del archivo .yaml
yaml_file_path = "../../../MH_01_easy/mav0/imu0/sensor.yaml"
with open(yaml_file_path, 'r') as yaml_file:
    yaml_data = yaml.safe_load(yaml_file)
# Extraigo la matriz:
T_BS_data = yaml_data.get('T_BS', {}).get('data', [])
# Convierto la lista en array NumPy de 4x4:
W_xi_B0 = np.array(T_BS_data).reshape(4, 4)
B0_xi_W = np.linalg.inv(W_xi_B0)
B_xi_C = np.dot(B0_xi_W, W_xi_C0)

# Lectura del archivo CSV en formato pandas DataFrame
csv_file_path = "../../../MH_01_easy/mav0/state_groundtruth_estimate0/data.csv"
df = pd.read_csv(csv_file_path)

# Extracción de las primeras 8 columnas
timestamps = df.iloc[:, 0]
timestamps = timestamps * 1e-9 #Para que los tiempos estén expresados en segundos
W_xi_Bi = []
for i in range(len(timestamps)):
    R = Rotation.from_quat(df.iloc[i, 4:8].to_numpy()).as_matrix()
    # t = np.matrix([[df.iloc[i,1]],[df.iloc[i,2]],[df.iloc[i,3]]])
    t = [df.iloc[i,1],df.iloc[i,2],df.iloc[i,3]]
    matriz = np.eye(4)
    matriz[:3,:3] = R
    matriz[:3,3] = t
    W_xi_Bi += [matriz]

# Transformo cada posición del robot al sistema de coordenadas de la cámara C_0
C0_xi_Bi = []
W_xi_Ci = []
for i in range(len(timestamps)):
    C0_xi_Bi += [np.dot(C0_xi_W, W_xi_Bi[i])]
    W_xi_Ci += [np.dot(W_xi_Bi[i], B_xi_C)]


# Gráfico del camino del robot y de la cámara
fig = plt.figure()
ax = plt.axes(projection='3d')

robot_x = []
robot_y = []
robot_z = []
camara_x = []
camara_y = []
camara_z = []
for i in range(0, len(W_xi_Bi), 50):
    print(i, "/", len(W_xi_Bi))
    robot_pose = W_xi_Bi[i]
    camara_pose = W_xi_Ci[i]

    robot_x += [robot_pose[0, 3]]
    robot_y += [robot_pose[1, 3]]
    robot_z += [robot_pose[2, 3]]
    camara_x += [camara_pose[0, 3]]
    camara_y += [camara_pose[1, 3]]
    camara_z += [camara_pose[2, 3]]

ax.plot3D(robot_x, robot_y, robot_z, c='blue', marker='o', label='Robot (IMU)')
ax.plot3D(camara_x, camara_y, camara_z, c='red', marker='x', label='Camara')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()

plt.show()
