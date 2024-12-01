from tinytroupe.environment import TinyWorld
from tinytroupe.agent import TinyPerson
from .create_primitive_tribe import create_primitive_tribe_members
import datetime
import json
import os

CACHE_FILE = "tribe_agents_cache.json"

def setup_primitive_tribe_world():
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, 'r', encoding='utf-8') as f:
            agents_data = json.load(f)
        agents = [TinyPerson(**agent_spec['_configuration']) for agent_spec in agents_data]
    else:
        tribe_members = create_primitive_tribe_members("tribe/tribe_members.json")
        agents_data = tribe_members  # Assuming tribe_members contains the necessary data
        agents = [TinyPerson(**agent_spec['_configuration']) for agent_spec in agents_data]
        # 保存代理到缓存
        with open(CACHE_FILE, 'w', encoding='utf-8') as f:
            json.dump(tribe_members, f, ensure_ascii=False, indent=4)

    world = TinyWorld(
        name="Primitive Tribe World",
        agents=agents,
        initial_datetime=datetime.datetime(2024, 12, 1, 14, 0, 0),
        broadcast_if_no_target=True
    )
    world.make_everyone_accessible()
    # 为每个代理人设置初始目标或任务
    for agent in world.agents:
        agent.internalize_goal("通过与部落成员合作，确保部落的繁荣和生存。")
    
    # 定义初始情景
    world.broadcast("""
    欢迎来到原始狩猎部落。你们需要在这片森林中生存下来，通过狩猎、采集和合作来确保部落的繁荣。环境丰富，但也充满挑战，请合理分配任务，互相协作，共同面对可能的威胁和机遇。
    请开始你们的日常活动。
    """)
    return world

def define_environment(world):
    environment_description = """
    部落位于一片密林深处，周围环绕着高大的树木和丰富的野生动物。附近有一条清澈的河流，为部落提供了充足的水源和鱼类资源。气候温暖且湿润，四季分明，有充足的降雨和温和的温度。地形崎岖，有多条小径穿过森林，适合狩猎和采集。部落周围拥有丰富的植物资源，包括可食用的果实、药用草药和可用来制作工具的木材和藤条。
    """
    
    social_structure = """
    部落的社会结构基于角色分工和合作。每个成员根据其职责和技能在部落中扮演特定的角色，如猎人、采集者、工匠、医者、领导者等。部落由领导者和长者指导，决策过程注重集体讨论和共识。资源分配遵循公平和互助的原则，确保每个人的基本需求得到满足。
    """
    
    interaction_rules = """
    社会规则：
    1. **决策机制**：重要决策由领导者和长者共同讨论决定，所有成员都有表达意见的权利。
    2. **资源分配**：食物和资源由采集者和猎人负责获取，工匠和制作者根据需要进行分配和使用。
    3. **合作与互助**：成员之间需互相协作，分享资源和知识，协助彼此完成任务。
    4. **冲突解决**：若发生冲突，通过集体讨论和调解来解决，避免暴力。
    5. **技能培训**：长者和专家定期培训年轻成员，传授生存技能和文化传统。
    """
    
    world.broadcast(environment_description)
    world.broadcast(social_structure)
    world.broadcast(interaction_rules)

def add_environmental_factors(world):
    environmental_factors = """
    环境要素：
    1. **天气系统**：每天的天气情况可能变化，包括晴天、雨天、风天等，影响狩猎和采集活动。
    2. **季节变化**：四季更替带来资源的变化，如春季花卉盛开，秋季果实丰收，冬季食物稀缺。
    3. **自然灾害**：偶发的风暴、火灾或动物入侵等自然灾害，考验部落的应对能力。
    4. **资源枯竭与再生**：部分资源可能会被过度利用，需设立再生机制以维持生态平衡。
    """
    world.broadcast(environmental_factors)

def define_resources(world):
    resources = """
    资源配置：
    1. **食物资源**：
        - 动物肉类：由猎人和渔夫提供。
        - 可食用植物：由采集者和园艺师提供。
        - 鱼类：由渔夫提供。
    2. **材料资源**：
        - 木材和藤条：由工匠采集，用于制作工具和建筑。
        - 石材和骨头：由工具制作者采集，用于制造武器和工具。
    3. **医药资源**：
        - 草药和药用植物：由草药师和医者采集，用于治疗和保健。
    4. **文化资源**：
        - 乐器材料：由音乐家和工匠提供，用于文化活动。
        - 编织材料：由织工提供，用于制作服饰和篮子。
    5. **水资源**：
        - 河流和水源：由水拿取者负责收集和分配。
    """
    world.broadcast(resources)

def initialize_world():

    world = setup_primitive_tribe_world()
    
    # 设置环境描述、社会结构与互动规则
    define_environment(world)
    
    # 添加环境要素
    add_environmental_factors(world)
    
    # 定义资源与经济系统
    define_resources(world)
    
    return world
