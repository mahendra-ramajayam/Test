# Batch Normalization – Solutions
# Batch Normalization 解决方案
"""
批量标准化在构建深度神经网络时最为有用。为了证明这一点，我们将创建一个具有20个卷积层的卷积神经网络，然后是一个完全连接的层。
我们将使用它来对MNIST数据集中的手写数字进行分类，现在您应该熟悉这一点。这不是划分MNIST数字的最好网络。您可以创建更简单的网络并获得更好的结果。
但是，为了给您批量标准化的实践经验，我们将使用这个作为一个例子:
1:这个网络足够复杂，可以保证体现BN算法对深层神经网络进行训练时的优势
2:这个例子比较简单，你可以很快获得训练的结果，这个简短的练习只是为了给你一次向深度神经玩过中添加BN算法的机会
3:足够简单，无需额外资源即可轻松理解架构。
"""
# 这个教程中有两种你可以自行编辑的在CNN中实现Batch Normalization的方法,
# 第一个是使用高级函数'tf.layers.batch_normalization',
# 第二个使用低级函数'tf.nn.batch_normalization'

# 下载MNIST手写数字识别数据集
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True, reshape=False)