import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# 解决中文显示问题
plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei']
plt.rcParams['axes.unicode_minus'] = False

# 1. 载入训练数据
data = pd.read_csv('air_data.csv')
X = data[['ZL', 'ZR', 'ZF', 'ZM', 'ZC']]
print("测试数据前5条:")
print(X.head())
print("="*50)

# 2. 肘部法确定最佳聚类数
wcss = []
for i in range(1, 11):
    kmeans = KMeans(
        n_clusters=i,
        init='k-means++',
        max_iter=300,
        n_init=10,
        random_state=0,
        algorithm='lloyd'
    )
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)

# 肘部法折线图（含学号姓名）
plt.figure(figsize=(10, 6))
plt.plot(range(1, 11), wcss, marker='o', linestyle='-', color='b')
plt.title('肘部法确定最佳聚类数\n学号：230511637 姓名：张世浩')  # 中文标题更直观
plt.xlabel('聚类类别数目')
plt.ylabel('组内平方和 (WCSS)')
plt.grid(True, alpha=0.3)
plt.show()

bestClass = 5
print(f"最佳聚类类别数目: {bestClass}")
print("="*50)

# 3. 训练KMeans模型
kmeans_model = KMeans(
    copy_x=True,
    init='k-means++',
    max_iter=300,
    n_clusters=bestClass,
    n_init=10,
    random_state=None,
    tol=0.0001,
    verbose=0,
    algorithm='lloyd'
)
cluster_labels = kmeans_model.fit_predict(X)
data['Cluster_Label'] = cluster_labels

# 4. 输出聚类结果
cluster_sample_count = data['Cluster_Label'].value_counts().sort_index()
print("每个聚类类别的样本数量:")
print(cluster_sample_count)
print("="*50)

cluster_centers = pd.DataFrame(
    kmeans_model.cluster_centers_,
    columns=['ZL', 'ZR', 'ZF', 'ZM', 'ZC'],
    index=[f'Cluster_{i}' for i in range(bestClass)]
)
print("每个聚类类别的中心点:")
print(cluster_centers)
print("="*50)

# 聚类中心点散点图（含学号姓名）
plt.figure(figsize=(12, 7))
feature_positions = np.arange(len(cluster_centers.columns))
colors = ['r', 'g', 'b', 'y', 'purple']

for i in range(bestClass):
    cluster_center = cluster_centers.iloc[i].values
    plt.scatter(
        feature_positions,
        cluster_center,
        color=colors[i],
        label=f'Cluster_{i}',
        s=100
    )
    plt.plot(
        feature_positions,
        cluster_center,
        color=colors[i],
        linestyle='-',
        linewidth=2
    )

plt.xlabel('特征维度 (ZL:入会时长, ZR:最近消费间隔, ZF:消费频次, ZM:消费里程, ZC:舱位折扣系数)')
plt.ylabel('标准化中心值')
plt.title('各特征维度的聚类中心分布\n学号：230511637 姓名：张世浩')  # 中文标题更直观
plt.xticks(feature_positions, cluster_centers.columns)
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

# 5. 聚类结果分析
print("聚类结果分析（基于实验定义的5个核心属性含义）:")
for i in range(bestClass):
    center = cluster_centers.iloc[i]
    print(f"\nCluster_{i}:")
    print(f"- 入会时长(ZL): {center['ZL']:.4f}（值越高→入会时间越长，潜在活跃时间越久）")
    print(f"- 最近消费间隔(ZR): {center['ZR']:.4f}（值越低→最近消费越近，近期活跃度越高）")
    print(f"- 消费频次(ZF): {center['ZF']:.4f}（值越高→消费次数越多，客户忠诚度越高）")
    print(f"- 消费里程(ZM): {center['ZM']:.4f}（值越高→总里程越多，对乘机依赖度越高）")
    print(f"- 舱位折扣系数(ZC): {center['ZC']:.4f}（值越高→舱位等级越高，客户消费能力越强）")