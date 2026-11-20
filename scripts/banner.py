valuethingies = {
    "standard": ("stan", "Standard", "stan.png", [""], [""]),
    "1011": ("1011", "1.0 Phase 1", "1011.png", ["Venti"], ["Barbara", "Fischl", "Xiangling"]),
    "1021": ("1021", "1.0 Phase 2", "1021.png", ["Klee"], ["Noelle", "Sucrose", "Fischl"]),
    "1111": ("1111", "1.1 Phase 1", "1111.png", ["Tartaglia"], ["Beidou", "Ningguang", "Diona"]),
    "1121": ("1121", "1.1 Phase 2", "1121.png", ["Zhongli"], ["Razor", "Chongyun", "Xinyan"]),
    "1211": ("1211", "1.2 Phase 1", "1211.png", ["Albedo"], ["Bennett", "Fischl", "Sucrose"]),
    "1221": ("1221", "1.2 Phase 2", "1221.png", ["Ganyu"], ["Noelle", "Xiangling", "Xingqiu"]),
    "1311": ("1311", "1.3 Phase 1", "1311.png", ["Xiao"], ["Beidou", "Diona", "Xinyan"]),
    "1321": ("1321", "1.3 Phase 2", "1321.png", ["Keqing"], ["Barbara", "Bennett", "Ningguang"]),
    "1331": ("1331", "1.3 Phase 3", "1331.png", ["Hutao"], ["Xiangling", "Xingqiu", "Chongyun"]),
    "1411": ("1411", "1.4 Phase 1", "1411.png", ["Venti"], ["Razor", "Noelle", "Sucrose"]),
    "1421": ("1421", "1.4 Phase 2", "1421.png", ["Tartaglia"], ["Barbara", "Fischl", "Rosaria"]),
    "1511": ("1511", "1.5 Phase 1", "1511.png", ["Zhongli"], ["Noelle", "Diona", "Yanfei"]),
    "1521": ("1521", "1.5 Phase 2", "1521.png", ["Eula"], ["Beidou", "Xingqiu", "Xinyan"]),
    "1611": ("1611", "1.6 Phase 1", "1611.png", ["Klee"], ["Barbara", "Fischl", "Sucrose"]),
    "1621": ("1621", "1.6 Phase 2", "1621.png", ["kazuha"], ["Razor", "Bennett", "Rosaria"]),

}

def switch(id):
    return valuethingies.get(str(id))
