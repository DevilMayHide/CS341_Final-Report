from GDLRU import FlashSwapSystemGDLRU
from LRU import FlashSwapSystemLRU
from random_pattern import Simulate_Experiment

# 实验参数
page_sizes = [10, 50, 100] # 页面数量
cache_sizes = [5, 10, 50] # 缓存大小
num_accesses = 5000 # 每组模拟访问次数

# 创建实验实例
exp = Simulate_Experiment(page_sizes, cache_sizes, num_accesses)
result = exp.run_all() # 所有统计结果

for experiment_name, stats in result.items():
    print(f"Results for {experiment_name}:")
    print(f"GDLRU (XMMS) Stats: {stats['GDLRU_XMMS']}")
    print(f"LRU (XMMS) Stats: {stats['LRU_XMMS']}")
    print(f"GDLRU (GEDIT) Stats: {stats['GDLRU_GEDIT']}")
    print(f"LRU (GEDIT) Stats: {stats['LRU_GEDIT']}\n")

# xmms = [
#     (1, False), (2, True), (3, False), (4, True),
#     (1, True), (2, False), (3, False), (4, True),
#     (5, False), (1, False), (2, True), (3, True)
# ]

# gedit = [
#     (1, True), (2, False), (3, False), (4, True),
#     (1, False), (5, True), (2, True), (3, False),
#     (4, False), (5, False)
# ]


# 生成随机访问
# xmms = generate_random_access_pattern(num_pages=50, num_accesses=60)
# gedit = generate_random_access_pattern(num_pages=50, num_accesses=60)

# # 使用xmms访问模式进行模拟实验
# print("Running GDLRU Algorithm for XMMS access pattern:")
# gdlru_system = FlashSwapSystemGDLRU(num_pages=100, max_cache_size=20)
# gdlru_system.simulate(xmms)
# gdlru_stats = gdlru_system.get_statistics()
# print(f"GDLRU Stats: {gdlru_stats}\n")

# print("Running LRU Algorithm for XMMS access pattern:")
# lru_system = FlashSwapSystemLRU(num_pages=100, max_cache_size=20)
# lru_system.simulate(xmms)
# lru_stats = lru_system.get_statistics()
# print(f"LRU Stats: {lru_stats}\n")

# print("----------------------------------------------\n")

# 使用gedit访问模式进行模拟实验
# print("Running GDLRU Algorithm for GEDIT access pattern:")
# gdlru_system.simulate(gedit)
# gdlru_stats = gdlru_system.get_statistics()
# print(f"GDLRU Stats: {gdlru_stats}\n")

# print("Running LRU Algorithm for GEDIT access pattern:")
# lru_system.simulate(gedit)
# lru_stats = lru_system.get_statistics()
# print(f"LRU Stats: {lru_stats}\n")