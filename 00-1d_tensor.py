import numpy as np
import tensorflow as tf

tensor_1d = np.array([1.3, 12.1, 1.34, 3.14])
print('印出 tensor_1d')
print(tensor_1d)
print('印出 tensor_1d[0]')
print(tensor_1d[0])
print('印出 tensor_1d[3]')
print(tensor_1d[3])
print('印出 tensor_1d 的張量')
print(tensor_1d.ndim)
print('印出 tensor_1d 張量維度的元組(tuple)')
print(tensor_1d.shape)
print('印出 tensor_1d 張量 的型別(data type)')
print(tensor_1d.dtype)

print()
print('將numpy 陣列 轉為tensorflow 的張量')
tf_tensor = tf.convert_to_tensor(tensor_1d, dtype=tf.float64)
