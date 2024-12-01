import json
from tinytroupe.factory import TinyPersonFactory
import logging
from tinytroupe.agent import EpisodicMemory

logger = logging.getLogger("tinytroupe")
logging.basicConfig(level=logging.INFO)

def load_tribe_members(file_path="./tribe_members.json"):
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

def assign_skills(role):
    skills_dict = {
        "猎人": ["追踪", "弓箭使用", "野外生存"],
        "采集者": ["植物识别", "食物储存", "自然观察"],
        "工匠": ["工具制作", "建筑设计", "维修"],
        "医者": ["草药治疗", "急救", "健康监测"],
        "领导者": ["决策", "协调", "策略规划"],
        "护卫": ["防御", "警戒", "战斗技能"],
        "猎手": ["陷阱设置", "步伐轻盈", "快速反应"],
        "厨师": ["烹饪", "食材处理", "菜单设计"],
        "音乐家": ["乐器演奏", "舞蹈编排", "节奏感"],
        "故事讲述者": ["口才", "记忆力", "文化传承"],
        "育儿": ["照看孩子", "教育指导", "活动组织"],
        "渔夫": ["捕鱼技巧", "网具维护", "水域了解"]
    }
    return skills_dict.get(role, ["多种技能"])

def determine_role(name):
    # 根据名字或其他逻辑确定角色类型
    role_mapping = {
        "Kali Hunt": "猎人",
        "Elder Wise": "领导者",
        "Lara Healer": "医者",
        "Bram Builder": "工匠",
        "Nia Firekeeper": "护卫",
        "Theo Scout": "猎手",
        "Lila Weaver": "工匠",
        "Rian Cook": "厨师",
        "Tara Childcare": "育儿",
        "Garth Fisher": "渔夫",
        "Willa Tanner": "工匠",
        "Jace Toolmaker": "工匠",
        "Sage Storyteller": "故事讲述者",
        "Finn Tracker": "猎手",
        "Ina Basketmaker": "工匠",
        "Orin Gatherer": "采集者",
        "Tess Herbalist": "医者",
        "Kian Waterbearer": "护卫",
        "Pia Craftswoman": "工匠",
        "Liam Guard": "护卫",
        "Eva Musician": "音乐家",
        "Rex Hunter": "猎人",
        "Maya Cook": "厨师",
        "Talon Hunter": "猎人"
    }
    return role_mapping.get(name, "多种角色")

def create_primitive_tribe_members(file_path="./tribe_members.json"):
    tribe_data = load_tribe_members(file_path)
    factory = TinyPersonFactory("A primitive hunting tribe in a dense forest.")
    tribe = []
    for member in tribe_data:
        if 'name' not in member:
            logger.error(f"成员数据缺少 'name' 字段: {member}")
            continue
        role = determine_role(member['name'])
        current_goals = member.get('current_goals', [f"执行{role}的职责，并与部落成员协作以确保部落的繁荣和生存。"])
        description = f"""
Create a tribe member with the following attributes:
- Name: {member['name']}
- First Name: {member.get('first_name', '')}
- Last Name: {member.get('last_name', '')}
- Age: {member.get('age', 'Unknown')}
- Nationality: {member.get('nationality', 'Unknown')}
- Country of Residence: {member.get('country_of_residence', 'Unknown')}
- Occupation: {member.get('occupation', 'Unknown')}
- Routines: {', '.join(member.get('routines', []))}
- Occupation Description: {member.get('occupation_description', '')}
- Personality Traits: {', '.join(member.get('personality_traits', []))}
- Professional Interests: {', '.join(member.get('professional_interests', []))}
- Personal Interests: {', '.join(member.get('personal_interests', []))}
- Skills: {', '.join(member.get('skills', []))}
- Relationships: {', '.join(member.get('relationships', []))}
- Current Datetime: {member.get('current_datetime', 'Unknown')}
- Current Location: {member.get('current_location', 'Unknown')}
- Current Context: {', '.join(member.get('current_context', []))}
- Current Attention: {member.get('current_attention', 'Unknown')}
- Current Goals: {json.dumps(current_goals, ensure_ascii=False)}
- Current Emotions: {member.get('current_emotions', 'Unknown')}
- Currently Accessible Agents: {json.dumps(member.get('currently_accessible_agents', []), ensure_ascii=False)}
- Innate Traits: {', '.join(member.get('innate_traits', []))}

Please return only the agent specification as a JSON object with the following structure, and nothing else:

{{
    "name": "{member['name']}",
    "_configuration": {{
        "name": "{member['name']}",
        "age": {json.dumps(member.get('age', None))},
        "nationality": "{member.get('nationality', None)}",
        "country_of_residence": "{member.get('country_of_residence', None)}",
        "occupation": "{member.get('occupation', 'Unknown')}",
        "routines": {json.dumps(member.get('routines', []), ensure_ascii=False)},
        "occupation_description": "{member.get('occupation_description', None)}",
        "personality_traits": {json.dumps(member.get('personality_traits', []), ensure_ascii=False)},
        "professional_interests": {json.dumps(member.get('professional_interests', []), ensure_ascii=False)},
        "personal_interests": {json.dumps(member.get('personal_interests', []), ensure_ascii=False)},
        "skills": {json.dumps(member.get('skills', []), ensure_ascii=False)},
        "relationships": {json.dumps(member.get('relationships', []), ensure_ascii=False)},
        "current_datetime": "{member.get('current_datetime', None)}",
        "current_location": "{member.get('current_location', None)}",
        "current_context": {json.dumps(member.get('current_context', []), ensure_ascii=False)},
        "current_attention": "{member.get('current_attention', None)}",
        "current_goals": {json.dumps(current_goals, ensure_ascii=False)},
        "current_emotions": "{member.get('current_emotions', 'Unknown')}",
        "currently_accessible_agents": {json.dumps(member.get('currently_accessible_agents', []), ensure_ascii=False)},
        "innate_traits": {json.dumps(member.get('innate_traits', []), ensure_ascii=False)}
    }}
}}
"""
        agent_spec = factory.generate_person(description)
        if agent_spec:
            agent_spec_dict = agent_spec.__dict__
        #     if isinstance(agent_spec_dict.get("episodic_memory"), EpisodicMemory):
        #         agent_spec_dict["episodic_memory"] = agent_spec_dict["episodic_memory"].to_dict()
        #     try:
        #         print(f"生成的 agent_spec for {member['name']}:\n{json.dumps(agent_spec_dict, ensure_ascii=False, indent=4)}\n")
        #     except TypeError as e:
        #         logger.error(f"JSON序列化失败: {e}")
        #         # 进一步处理或清理 agent_spec_dict
        #     tribe.append(agent_spec)
        # # 检查 'current_goals' 是否存在
        # if "_configuration" not in agent_spec_dict:
        #     raise KeyError(f"Agent spec for {member['name']} 缺少 '_configuration' 部分。")
        # if "current_goals" not in agent_spec_dict["_configuration"]:
        #     raise KeyError(f"Agent spec for {member['name']} 缺少 'current_goals' 键。")

        tribe.append(agent_spec_dict)
    return tribe
