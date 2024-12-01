from .primitive_tribe_world import initialize_world
from tinytroupe.extraction import ResultsExtractor
import tinytroupe.control as control
from tinytroupe import openai_utils
import os
import configparser

def run_tribe_simulation():
    # 读取配置文件
    config = configparser.ConfigParser()
    config_path = os.path.join(os.path.dirname(__file__), 'config.ini')
    config.read(config_path)
    
    # 调试输出
    if not config.sections():
        raise FileNotFoundError(f"配置文件未正确加载，请检查路径: {config_path}")
    else:
        print(f"成功加载配置文件: {config.sections()}")

    # 启用缓存
    if config.getboolean("cache", "enable_simulation_state_cache"):
        cache_file = config.get("cache", "simulation_state_cache_file")
        control.begin(cache_file)
    
    cache_api_calls = True  # 或者根据您的配置设置
    openai_utils.force_api_cache(cache_api_calls)
    
    world = initialize_world()
    total_steps = 1  # 模拟的时间步数，例如30天
    world.make_everyone_accessible()
    
    for step in range(1, total_steps + 1):
        print(f"───────────────── 第 {step} 天 ─────────────────")
        world.run(step)
        # 在这里可以添加更多的情景变化或事件，例如天气变化、外来威胁等
    
    control.end()
    
    # 提取和分析结果
    extractor = ResultsExtractor()
    results = extractor.extract_results_from_world(world)
    print("模拟结果：")
    print(results)
