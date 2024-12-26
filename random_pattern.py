import random
from GDLRU import FlashSwapSystemGDLRU
from LRU import FlashSwapSystemLRU

class Simulate_Experiment:
    def __init__(self, page_sizes, cache_sizes, num_accesses):
        """
        初始化参数
        Args:
            page_sizes (_List_): 页面数量的列表
            cache_sizes (_List_): 缓存大小的列表
            num_accesses (_int_): 每次模拟的页面访问次数
        """
        self.page_sizes = page_sizes
        self.cache_sizes = cache_sizes
        self.num_accesses = num_accesses

    # 随机生成访问模式
    def generate_random_access_pattern(self, num_pages):
        """
        Args:
            num_pages (_int_): _系统中模拟的页面数量。该参数决定了页面ID的范围（从 1 到 num_pages）_

        Returns:
            _List_: 一个元组 (page_id, is_dirty)
        """
        access_pattern = []
        for _ in range(self.num_accesses):
            page_id = random.randint(1, num_pages)  # 随机选择页面ID
            is_dirty = random.choice([True, False])  # 随机选择脏页面或清洁页面
            access_pattern.append((page_id, is_dirty))
        return access_pattern
    
    def run_experiment(self, algorithm_type, num_pages, max_cache_size, access_pattern):
        """
        运行单个实验
        Args:
            algorithm_type: 算法类(GDLRU 或 LRU)
            num_pages: 页面数量
            max_cache_size: 最大缓存大小
            access_pattern: 页面访问模式
        Returns: 
            实验结果（统计数据）
        """
        system = algorithm_type(num_pages=num_pages, max_cache_size=max_cache_size)
        
        # 运行算法模拟
        system.simulate(access_pattern)
        
        # 获取统计数据
        stats = system.get_statistics()
        return stats
    
    
    def run_all(self):
        results = {}
        for num_pages in self.page_sizes:
            for max_cache_size in self.cache_sizes:
                print(f"Running experiment with {num_pages} pages and cache size {max_cache_size}")
            
                # 为每组实验生成随机访问模式
                xmms = self.generate_random_access_pattern(num_pages)
                gedit = self.generate_random_access_pattern(num_pages)
                
                # 运行GDLRU算法
                gdlru_stats_xmms = self.run_experiment(FlashSwapSystemGDLRU, num_pages, max_cache_size, xmms)
                gdlru_stats_gedit = self.run_experiment(FlashSwapSystemGDLRU, num_pages, max_cache_size, gedit)
                
                # 运行LRU算法
                lru_stats_xmms = self.run_experiment(FlashSwapSystemLRU, num_pages, max_cache_size, xmms)
                lru_stats_gedit = self.run_experiment(FlashSwapSystemLRU, num_pages, max_cache_size, gedit)
                
                # 存储每组实验的结果
                results[f"{num_pages} pages, cache {max_cache_size}"] = {
                    "GDLRU_XMMS": gdlru_stats_xmms,
                    "LRU_XMMS": lru_stats_xmms,
                    "GDLRU_GEDIT": gdlru_stats_gedit,
                    "LRU_GEDIT": lru_stats_gedit
                }
        
        return results
