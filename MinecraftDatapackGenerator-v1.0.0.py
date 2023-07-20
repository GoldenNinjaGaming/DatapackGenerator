import os
import sys
import colorama
from colorama import Back, Fore, Style
colorama.init(autoreset=True)

def generate(mode='s'):
    
    # Generate Namespace, Data, Minecraft, Pack.mcmeta, etc.
    
    script_directory = os.path.dirname(os.path.abspath(sys.argv[0]))
    name = os.path.join(script_directory, nam)
    os.mkdir(name)
    os.mkdir(name + "\\data")
    namespace = os.path.join(name, "data", namespac)
    minecraft = os.path.join(name, "data", "minecraft")
    os.mkdir(minecraft)
    os.mkdir(namespace)
    with open(f'{name}\\pack.mcmeta', 'w') as pack:
        pack.write('{\n    "pack": {\n        "pack_format": 15,\n        "description": "Generated by Python"\n    }\n}\n')
        pack.close()
        
    # Generate Basic Namespace Folders
    
    os.mkdir(namespace + "\\functions")
    os.mkdir(namespace + "\\loot_tables")
    os.mkdir(namespace + "\\structures")
    os.mkdir(namespace + "\\worldgen")
    os.mkdir(namespace + "\\advancements")
    os.mkdir(namespace + "\\recipes")
    os.mkdir(namespace + "\\tags")
    os.mkdir(namespace + "\\predicates")
    os.mkdir(namespace + "\\dimension")
    os.mkdir(namespace + "\\dimension_type")
    
    # Generate Advanced Namespace Subfolders
    
    if mode == 'a':
        os.mkdir(namespace + "\\worldgen\\noise_settings")
        os.mkdir(namespace + "\\worldgen\\biome")
        os.mkdir(namespace + "\\worldgen\\configured_carver")
        os.mkdir(namespace + "\\worldgen\\template_pool")
        os.mkdir(namespace + "\\worldgen\\structure")
        os.mkdir(namespace + "\\worldgen\\structure_set")
        os.mkdir(namespace + "\\worldgen\\processor_list")
    
        os.mkdir(namespace + "\\tags\\blocks")
        os.mkdir(namespace + "\\tags\\fluids")
        os.mkdir(namespace + "\\tags\\items")
        os.mkdir(namespace + "\\tags\\entity_types")
        os.mkdir(namespace + "\\tags\\game_events")
        os.mkdir(namespace + "\\tags\\worldgen")
        os.mkdir(namespace + "\\tags\\functions")
        os.mkdir(namespace + "\\tags\\loot_tables")
        os.mkdir(namespace + "\\tags\\structures")
        os.mkdir(namespace + "\\tags\\advancements")
        os.mkdir(namespace + "\\tags\\recipes")
        os.mkdir(namespace + "\\tags\\tags")
        os.mkdir(namespace + "\\tags\\predicates")
        os.mkdir(namespace + "\\tags\\dimension")
        
        os.mkdir(namespace + "\\tags\\worldgen\\noise_settings")
        os.mkdir(namespace + "\\tags\\worldgen\\biome")
        os.mkdir(namespace + "\\tags\\worldgen\\configured_carver")
        os.mkdir(namespace + "\\tags\\worldgen\\template_pool")
        os.mkdir(namespace + "\\tags\\worldgen\\structure")
        os.mkdir(namespace + "\\tags\\worldgen\\structure_set")
        os.mkdir(namespace + "\\tags\\worldgen\\processor_list")
        
    # Generate Minecraft Folders
    
    os.mkdir(minecraft + "\\advancements")
    os.mkdir(minecraft + "\\loot_tables")
    os.mkdir(minecraft + "\\recipes")
    os.mkdir(minecraft + "\\structures")
    os.mkdir(minecraft + "\\tags")
    
    os.mkdir(minecraft + "\\tags" + "\\blocks")
    os.mkdir(minecraft + "\\tags" + "\\entity_types")
    os.mkdir(minecraft + "\\tags" + "\\fluids")
    os.mkdir(minecraft + "\\tags" + "\\game_events")
    os.mkdir(minecraft + "\\tags" + "\\items")
    os.mkdir(minecraft + "\\tags" + "\\functions")
    
    # Generate Advanced Minecraft Subfolders
    
    if mode == 'a':
        os.mkdir(minecraft + "\\advancements" + "\\adventure")
        os.mkdir(minecraft + "\\advancements" + "\\end")
        os.mkdir(minecraft + "\\advancements" + "\\husbandry")
        os.mkdir(minecraft + "\\advancements" + "\\nether")
        os.mkdir(minecraft + "\\advancements" + "\\recipes")
        os.mkdir(minecraft + "\\advancements" + "\\story")
    
        os.mkdir(minecraft + "\\loot_tables" + "\\blocks")
        os.mkdir(minecraft + "\\loot_tables" + "\\chests")
        os.mkdir(minecraft + "\\loot_tables" + "\\entities")
        os.mkdir(minecraft + "\\loot_tables" + "\\gameplay")
    
        os.mkdir(minecraft + "\\structures" + "\\bastion")
        os.mkdir(minecraft + "\\structures" + "\\end_city")
        os.mkdir(minecraft + "\\structures" + "\\fossil")
        os.mkdir(minecraft + "\\structures" + "\\igloo")
        os.mkdir(minecraft + "\\structures" + "\\nether_fossils")
        os.mkdir(minecraft + "\\structures" + "\\pillager_outpost")
        os.mkdir(minecraft + "\\structures" + "\\ruined_portal")
        os.mkdir(minecraft + "\\structures" + "\\shipwreck")
        os.mkdir(minecraft + "\\structures" + "\\underwater_ruin")
        os.mkdir(minecraft + "\\structures" + "\\village")
        os.mkdir(minecraft + "\\structures" + "\\woodland_mansion")
        
    # Generate Load and Tick files
    
    with open(f'{namespace}\\functions\\tick.mcfunction', 'w') as tick:
        tick.write('# Tick File. Any commands in here run every tick (20 times per second)')
        tick.close()
    with open(f'{namespace}\\functions\\load.mcfunction', 'w') as load:
        load.write('tellraw "Datapack Loaded"\n# Anything in here runs every time the pack is loaded.')
        load.close()
    with open(f'{minecraft}\\tags\\functions\\tick.json', 'w') as tickJS:
        tickJS.write('{\n    "values":[\n        ' + f'"{namespac}' + ':tick"\n        ]\n    }')
        tickJS.close()
    with open(f'{minecraft}\\tags\\functions\\load.json', 'w') as loadJS:
        loadJS.write('{\n    "values":[\n        ' + f'"{namespac}' + ':load"\n        ]\n    }')
        loadJS.close()

nam = input(Fore.LIGHTCYAN_EX + "What is your datapack's name?\n")
namespac = input(Fore.LIGHTCYAN_EX + "What is your datapack's namespace?\n").lower()
mode = input(Fore.LIGHTCYAN_EX + "Simple or Advanced mode? (S/A)\n").lower()
run = input(Fore.LIGHTCYAN_EX + "Generate Template? (" + Fore.LIGHTGREEN_EX + "Y" + Fore.LIGHTCYAN_EX + "/" + Fore.RED + "N" + Fore.LIGHTCYAN_EX + ")\n").lower()

if run == 'y':
    generate(mode)
else:
    print(Fore.RED + "Generation Canceled.")
    input(Fore.WHITE + "Press Enter to Close...")