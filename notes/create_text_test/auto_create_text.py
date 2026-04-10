import random
from datetime import datetime

# ================= 可自定义配置区（小白直接改这里！） =================
# 1. 生成数量
role_num = 25  # 生成角色名的数量
world_num = 15  # 生成世界设定的数量

# 2. 角色名字配置（可添加/删除词库）
# 姓（古风/现代/二次元都能加）
surnames = ["赵", "钱", "孙", "李", "王", "欧阳", "上官", "诸葛", "风", "夜", "墨", "白"]
# 名（单字/双字都可）
names = ["轩", "宇", "辰", "阳", "雪", "月", "灵", "瑶", "逸", "尘", "璃", "殇"]
# 角色称号（可选，留空则不生成）
titles = ["[战神]", "[医仙]", "[刺客]", "[精灵王]", "[城主]", "[召唤师]"]

# 3. 世界设定词库（可扩充！）
world_templates = [
    "这是一个以{element}为力量核心的世界，人类觉醒{skill}能力，传说中{legend}。",
    "大陆被{sea}分割为七大城邦，每座城邦都有专属的{craft}工艺，而{secret}是世界最大的秘密。",
    "千年之前，{god}降临人间，留下{treasure}传承，如今，{conflict}在大陆上悄然爆发。"
]
# 词库填充
elements = ["金木水火土", "雷电", "精神", "时间", "空间", "光影"]
skills = ["御兽", "炼丹", "御剑", "控冰", "读心", "瞬移"]
legends = ["有神兽沉睡在昆仑之巅", "有上古神器藏于海底深渊", "有精灵族守护着世界树"]
seas = ["无尽之海", "迷雾之海", "冰封之海"]
crafts = ["炼器", "制药", "制符", "驯兽", "铸甲"]
secrets = ["大陆的尽头是虚空", "人类的血脉源自神明", "世界正在缓慢消亡"]
gods = ["创世神", "战神", "海神", "生命女神", "暗影之神"]
treasures = ["乾坤壶", "通天剑", "定海珠", "生命之晶", "时空沙漏"]
conflicts = ["种族之争", "资源掠夺", "传承争夺", "权力更迭"]

# 4. 导出文件名
export_filename = "生成素材_{date}.txt".format(date=datetime.now().strftime("%Y%m%d"))
# ======================================================================

# 🔧 功能1：生成随机角色名
def create_role_name():
    surname = random.choice(surnames)  # 随机选姓
    name = random.choice(names)      # 随机选名
    full_name = surname + name       # 组合全名
    # 随机加称号（50%概率）
    if random.random() > 0.5 and titles:
        full_name += " " + random.choice(titles)
    return full_name

# 🔧 功能2：生成随机世界设定
def create_world_setting():
    template = random.choice(world_templates)  # 随机选模板
    # 用对应词库填充模板
    return template.format(
        element=random.choice(elements),
        skill=random.choice(skills),
        legend=random.choice(legends),
        sea=random.choice(seas),
        craft=random.choice(crafts),
        secret=random.choice(secrets),
        god=random.choice(gods),
        treasure=random.choice(treasures),
        conflict=random.choice(conflicts)
    )

# 🔧 功能3：导出到TXT文件
def export_to_txt(role_texts, world_texts):
    with open(export_filename, "w", encoding="utf-8") as f:
        f.write("===== 生成的角色名字 =====\n")
        for i, name in enumerate(role_texts, 1):
            f.write(f"{i}. {name}\n")
        
        f.write("\n===== 生成的世界设定 =====\n")
        for i, setting in enumerate(world_texts, 1):
            f.write(f"{i}. {setting}\n")
    print(f"\n✅ 素材已导出到：{export_filename}")

# 🚀 主程序（运行核心逻辑）
if __name__ == "__main__":
    print("🚀 开始自动生成素材...")
    # 生成角色名
    role_list = [create_role_name() for _ in range(role_num)]
    print("\n📛 生成的角色名字：")
    for name in role_list:
        print(f"- {name}")
    
    # 生成世界设定
    world_list = [create_world_setting() for _ in range(world_num)]
    print("\n🌍 生成的世界设定：")
    for setting in world_list:
        print(f"- {setting}")
    
    # 导出文件
    export_to_txt(role_list, world_list)
    print("\n🎉 第14天任务完成！素材已保存~")