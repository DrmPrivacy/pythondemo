#coding:utf-8
import tensorflow as tf
import numpy as np #python科学计算模块
BATCH_SIZE=8 #一次载入神经网络多少组数据 不宜过大 过大神经网络吃不消
seed = 23455

#基于seed产生随机数
rng = np.random.RandomState(seed)
#随机数返回32行2列的矩阵 表示32组的体积和重量
X = rng.rand(32,2)
Y = [[int(x0+x1<1)] for x0,x1 in X]
print('X:\n',X)
print('Y:\n',Y)
# 前向传播
#定义神经网络传入、参数、输出
x=tf.placeholder(tf.float32,shape=[None,2])
y_=tf.placeholder(tf.float32,shape=[None,1]) #标签 1是合格
#输入 2行3列
w1 = tf.Variable(tf.random_normal([2,3],stddev=1,seed=1))
#输出 3行1列
w2 = tf.Variable(tf.random_normal([3,1],stddev=1,seed=1))
a = tf.matmul(x,w1)
y = tf.matmul(a,w2)
#反向传播
#定义损失函数以及反向传播方法
loss = tf.reduce_mean(tf.square(y-y_))
train_step = tf.train.GradientDescentOptimizer(0.001).minimize(loss)
#train_step = tf.train.MomentumOptimizer(0.001,0.09).minimize(loss)
#train_step = tf.train.AdadeltaOptimizer(0.001).minimize(loss)
#生成会话 训练Steps轮
with tf.Session() as sess:
    init_op = tf.global_variables_initializer()
    sess.run(init_op)
    #输出当前目录 未经训练的参数值
    print('W1:\n',sess.run(w1))
    print('W2:\n', sess.run(w2))
    #训练模型
    Steps =100000;
    for i in range(Steps):
        start = (i * BATCH_SIZE) % 32
        end = start+BATCH_SIZE
        sess.run(train_step,feed_dict={x:X[start:end],y_:Y[start:end]})
        if i % 500 == 0:
            total_loss = sess.run(loss,feed_dict={x:X,y_:Y})
            print('After %d training Steps,loss on all data %g'%(i,total_loss))
    print('\n')
    print('w1:\n',sess.run(w1))