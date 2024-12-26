from collections import deque

class Page:
    def __init__(self, page_id, is_dirty=False):
        self.page_id = page_id # 页面ID
        self.is_dirty = is_dirty # 页面是否为脏的
        self.timestamp = 0 # LRU的时间戳

    def printf_information(self):
        return f"Page({self.page_id}, Dirty: {self.is_dirty})"

class FlashSwapSystemLRU:
    def __init__(self, num_pages, max_cache_size):
        self.num_pages = num_pages # 总页面数
        self.max_cache_size = max_cache_size # 最大缓存页面数
        self.cache = deque() # 页面缓存队列
        self.page_map = {} # 页面ID到Page对象的映射
        self.time = 0  
        self.page_write_count = 0  
        self.page_eviction_count = 0  

    def access_page(self, page_id, is_dirty=False):
        """模拟访问一个页面，如果缓存已满则替换一个页面"""
        self.time += 1  

        if page_id in self.page_map:
            page = self.page_map[page_id]
            page.timestamp = self.time  
            if is_dirty:
                page.is_dirty = True 
        else:
            # 如果缓存未满，直接添加
            if len(self.cache) < self.max_cache_size:
                page = Page(page_id, is_dirty)
                self.cache.append(page)
                self.page_map[page_id] = page
            else:
                # 缓存已满，使用LRU替换策略
                self.evict_page(is_dirty)

    def evict_page(self, is_dirty):
        """根据LRU算法进行页面替换"""
        self.page_eviction_count += 1
        # 选择最久未使用的页面
        victim_page = min(self.cache, key=lambda p: p.timestamp)
        
        # 写回脏页面
        if victim_page.is_dirty:
            self.page_write_count += 1
            #print(f"Writing back dirty page: {victim_page}")
        
        # 清除页面并更新缓存
        self.cache.remove(victim_page)
        del self.page_map[victim_page.page_id]
        
        # 添加新页面
        new_page = Page(victim_page.page_id, is_dirty)
        self.cache.append(new_page)
        self.page_map[new_page.page_id] = new_page
        #print(f"Evicted page {victim_page} and added new page {new_page}")

    def simulate(self, access_pattern):
        """根据给定的访问模式进行模拟"""
        for page_id, is_dirty in access_pattern:
            self.access_page(page_id, is_dirty)

    def get_statistics(self):
        return {
            "page_write_count": self.page_write_count,
            "page_eviction_count": self.page_eviction_count
        }
