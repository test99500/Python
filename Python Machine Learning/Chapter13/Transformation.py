import tensorflow as tf

tf.random.set_seed(1)

X = tf.random.uniform(shape=[4, 3], dtype=tf.float32)

y = tf.range(4)

joint_dataset = tf.data.Dataset.from_tensor_slices((X, y))

print(joint_dataset)

for individual_dataset in joint_dataset:
    print('X:', individual_dataset[0].numpy(), 'y:', individual_dataset[1].numpy())

