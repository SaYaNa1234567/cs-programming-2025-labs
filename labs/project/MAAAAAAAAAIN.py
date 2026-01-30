import os
import sys
import random

class Race:
    HUMAN = "Человек"
    ELF = "Эльф"
    HALF_ORC = "Полуорк"

class Player:
    def __init__(self, race):
        self.race = race
        self.level = 1
        self.exp = 0
        self.exp_to_next_level = 100
        self.skill_points = 3
        
        if race == Race.HUMAN:
            self.max_hp = random.randint(80, 100)
            self.attack = random.randint(10, 14)
            self.defense = random.randint(8, 12)
            self.agility = random.randint(9, 13)
            self.height = random.randint(165, 185)
            self.weight = random.randint(65, 85)
        elif race == Race.ELF:
            self.max_hp = random.randint(70, 85)
            self.attack = random.randint(8, 12)
            self.defense = random.randint(6, 10)
            self.agility = random.randint(14, 18)
            self.height = random.randint(175, 195)
            self.weight = random.randint(55, 75)
        elif race == Race.HALF_ORC:
            self.max_hp = random.randint(95, 115)
            self.attack = random.randint(13, 17)
            self.defense = random.randint(9, 13)
            self.agility = random.randint(5, 9)
            self.height = random.randint(180, 200)
            self.weight = random.randint(85, 105)
        
        self.current_hp = self.max_hp
        self.equipped_weapon = None
        self.equipped_armor = None
        self.evasion = self.agility // 2
    
    def display_stats(self):
        print(f"Раса: {self.race}")
        print(f"Уровень: {self.level}")
        print(f"Опыт: {self.exp}/{self.exp_to_next_level}")
        print(f"Очки прокачки: {self.skill_points}")
        print(f"HP: {self.current_hp}/{self.max_hp}")
        print(f"Атака: {self.attack}")
        print(f"Защита: {self.defense}")
        print(f"Ловкость: {self.agility}")
        print(f"Уклонение: {self.evasion}%")
        print(f"Рост: {self.height} см, Вес: {self.weight} кг")
        
        if self.equipped_weapon:
            print(f"Оружие: {self.equipped_weapon.name}")
        if self.equipped_armor:
            print(f"Броня: {self.equipped_armor.name}")
    
    def gain_exp(self, amount):
        self.exp += amount
        print(f"Получено {amount} опыта")
        
        if self.exp >= self.exp_to_next_level:
            self.level_up()
    
    def level_up(self):
        self.level += 1
        self.exp -= self.exp_to_next_level
        self.exp_to_next_level = int(self.exp_to_next_level * 1.5)
        self.skill_points += 3
        self.current_hp = self.max_hp
        
        print(f"\nПоздравляем! Вы достигли {self.level} уровня!")
        print(f"Получено 3 очка прокачки. Всего: {self.skill_points}")
    
    def spend_skill_point(self, stat):
        if self.skill_points <= 0:
            print("Нет очков прокачки!")
            return False
            
        if stat == "hp":
            self.max_hp += 10
            self.current_hp += 10
            print(f"HP +10. Теперь: {self.max_hp}")
        elif stat == "attack":
            self.attack += 1
            print(f"Атака +1. Теперь: {self.attack}")
        elif stat == "defense":
            self.defense += 1
            print(f"Защита +1. Теперь: {self.defense}")
        elif stat == "agility":
            self.agility += 1
            self.evasion = self.agility // 2
            print(f"Ловкость +1. Теперь: {self.agility}")
        else:
            print("Неверная характеристика")
            return False
            
        self.skill_points -= 1
        print(f"Осталось очков: {self.skill_points}")
        return True
    
    def take_damage(self, damage):
        if random.randint(1, 100) <= self.evasion:
            print(f"Уклонение! ({self.evasion}% шанс)")
            return 0
            
        actual_damage = max(1, damage - self.defense)
        self.current_hp -= actual_damage
        
        if self.current_hp < 0:
            self.current_hp = 0
            
        return actual_damage
    
    def heal(self, amount):
        old_hp = self.current_hp
        self.current_hp = min(self.max_hp, self.current_hp + amount)
        return self.current_hp - old_hp

class Item:
    def __init__(self, name, item_type, stats=None):
        self.name = name
        self.item_type = item_type
        self.stats = stats or {}
    
    def use(self, player):
        if self.item_type == "potion" and "heal" in self.stats:
            healed = player.heal(self.stats["heal"])
            print(f"Восстановлено {healed} HP")
            return True
        return False
    
    def equip(self, player):
        if self.item_type == "weapon":
            player.equipped_weapon = self
            player.attack += self.stats.get("attack", 0)
            print(f"Экипирован {self.name}")
            return True
        elif self.item_type == "armor":
            player.equipped_armor = self
            player.defense += self.stats.get("defense", 0)
            print(f"Экипирован {self.name}")
            return True
        return False

class Inventory:
    def __init__(self, player):
        self.player = player
        self.items = []
        self.gold = 100
        
        self.add_item(Item("Малое зелье здоровья", "potion", {"heal": 20}))
        self.add_item(Item("Простой меч", "weapon", {"attack": 3}))
    
    def add_item(self, item):
        self.items.append(item)
        print(f"Получен предмет: {item.name}")
        return True
    
    def display(self):
        print(f"Золото: {self.gold}")
        
        if not self.items:
            print("Инвентарь пуст")
            return
            
        print("Предметы:")
        for i, item in enumerate(self.items):
            print(f"{i}: {item.name}")
            if item.stats:
                print(f"  Эффект: {item.stats}")

class Room:
    def __init__(self, room_type, content=None):
        self.room_type = room_type
        self.content = content

class Dungeon:
    def generate_room(self):
        room_type = random.choice(["combat", "treasure", "rest", "empty"])
        
        if room_type == "combat":
            content = self.generate_enemy()
        elif room_type == "treasure":
            content = self.generate_treasure()
        else:
            content = None
        
        return Room(room_type, content)
    
    def generate_enemy(self):
        enemies = [
            {"name": "Гоблин", "hp": 30, "attack": 8, "defense": 3, "exp": 20, "gold": 10},
            {"name": "Скелет", "hp": 40, "attack": 10, "defense": 4, "exp": 30, "gold": 15},
            {"name": "Орк", "hp": 50, "attack": 12, "defense": 5, "exp": 40, "gold": 20}
        ]
        
        return random.choice(enemies)
    
    def generate_treasure(self):
        treasures = [
            {"gold": 50},
            {"gold": 100},
            {"gold": 30, "item": "potion"}
        ]
        
        return random.choice(treasures)

class Combat:
    def __init__(self, player, enemy, inventory):
        self.player = player
        self.enemy = enemy
        self.inventory = inventory
    
    def start(self):
        print(f"\nБой с {self.enemy['name']}!")
        
        while self.player.current_hp > 0 and self.enemy["hp"] > 0:
            print(f"\nВаше HP: {self.player.current_hp}")
            print(f"HP врага: {self.enemy['hp']}")
            
            print("1 - Атаковать")
            print("2 - Использовать предмет")
            print("3 - Сбежать")
            
            choice = input("Ваш выбор: ")
            
            if choice == "1":
                self.player_attack()
            elif choice == "2":
                self.use_item()
            elif choice == "3":
                if self.try_flee():
                    return "flee"
            
            if self.enemy["hp"] <= 0:
                return "win"
            
            self.enemy_turn()
            
            if self.player.current_hp <= 0:
                return "lose"
        
        return "lose"
    
    def player_attack(self):
        print(f"\nВы атакуете {self.enemy['name']}!")
        damage = self.player.attack
        actual_damage = max(1, damage - self.enemy["defense"])
        self.enemy["hp"] -= actual_damage
        print(f"Нанесено {actual_damage} урона!")
    
    def use_item(self):
        print("\nВаши зелья:")
        potions = [i for i, item in enumerate(self.inventory.items) 
                  if item.item_type == "potion"]
        
        if not potions:
            print("Нет зелий!")
            return False
        
        for i in potions:
            print(f"{i}: {self.inventory.items[i].name}")
        
        try:
            choice = int(input("Выберите зелье: "))
            if choice in potions:
                item = self.inventory.items[choice]
                if item.use(self.player):
                    self.inventory.items.pop(choice)
                    return True
        except:
            print("Неверный выбор!")
        
        return False
    
    def try_flee(self):
        flee_chance = 30 + self.player.agility
        
        if random.random() * 100 < flee_chance:
            print("Вы сбежали!")
            return True
        else:
            print("Не удалось сбежать!")
            return False
    
    def enemy_turn(self):
        print(f"\n{self.enemy['name']} атакует!")
        damage = self.enemy["attack"]
        actual_damage = self.player.take_damage(damage)
        
        if actual_damage > 0:
            print(f"Вам нанесено {actual_damage} урона!")

class TextRPG:
    def __init__(self):
        self.player = None
        self.dungeon = None
        self.current_room = None
        self.inventory = None
        self.game_running = False
    
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def wait(self):
        input("\nНажмите Enter...")
    
    def character_creation(self):
        self.clear_screen()
        print("СОЗДАНИЕ ПЕРСОНАЖА")
        print("=" * 40)
        
        print("Выберите расу:")
        print("1 - Человек (сбалансированный)")
        print("2 - Эльф (ловкий)")
        print("3 - Полуорк (сильный)")
        
        while True:
            choice = input("\nВаш выбор: ")
            
            if choice == "1":
                race = Race.HUMAN
                break
            elif choice == "2":
                race = Race.ELF
                break
            elif choice == "3":
                race = Race.HALF_ORC
                break
            else:
                print("Неверный выбор")
        
        self.player = Player(race)
        self.inventory = Inventory(self.player)
        
        self.clear_screen()
        print("ПЕРСОНАЖ СОЗДАН!")
        self.player.display_stats()
        self.wait()
    
    def main_menu(self):
        while True:
            self.clear_screen()
            print("ТЕКСТОВАЯ RPG")
            print("=" * 40)
            print("1 - Новая игра")
            print("2 - Выход")
            
            choice = input("\nВыбор: ")
            
            if choice == "1":
                self.character_creation()
                self.start_game()
                break
            elif choice == "2":
                sys.exit(0)
    
    def start_game(self):
        self.dungeon = Dungeon()
        self.current_room = self.dungeon.generate_room()
        self.game_running = True
        self.game_loop()
    
    def game_loop(self):
        while self.game_running:
            self.enter_room()
            
            if self.player.current_hp <= 0:
                self.game_over()
                break
    
    def enter_room(self):
        self.clear_screen()
        print("ВЫ ВОШЛИ В КОМНАТУ")
        print("=" * 40)
        
        room_type = self.current_room.room_type
        
        if room_type == "combat":
            self.combat_room()
        elif room_type == "treasure":
            self.treasure_room()
        elif room_type == "rest":
            self.rest_room()
        elif room_type == "empty":
            self.empty_room()
        
        self.choose_path()
    
    def combat_room(self):
        enemy = self.current_room.content
        
        print(f"\nВы встретили {enemy['name']}!")
        print(f"HP: {enemy['hp']}, Атака: {enemy['attack']}")
        
        self.wait()
        
        combat = Combat(self.player, enemy, self.inventory)
        result = combat.start()
        
        if result == "win":
            self.after_combat_victory(enemy)
        elif result == "flee":
            print("\nВы сбежали, но получили урон!")
            self.player.take_damage(5)
            self.wait()
    
    def after_combat_victory(self, enemy):
        exp_gained = enemy['exp']
        gold_gained = enemy['gold']
        
        self.player.gain_exp(exp_gained)
        self.inventory.gold += gold_gained
        
        print(f"\nВы победили!")
        print(f"Опыт: +{exp_gained}, Золото: +{gold_gained}")
        self.wait()
    
    def treasure_room(self):
        treasure = self.current_room.content
        
        print("\nВы нашли сокровища!")
        
        if "gold" in treasure:
            gold = treasure["gold"]
            self.inventory.gold += gold
            print(f"Золото: +{gold}")
        
        if "item" in treasure and treasure["item"] == "potion":
            item = Item("Зелье здоровья", "potion", {"heal": 20})
            self.inventory.add_item(item)
        
        self.wait()
    
    def rest_room(self):
        print("\nКомната отдыха.")
        heal_amount = self.player.max_hp // 4
        healed = self.player.heal(heal_amount)
        print(f"Вы отдохнули и восстановили {healed} HP")
        self.wait()
    
    def empty_room(self):
        print("\nКомната пуста.")
        self.wait()
    
    def choose_path(self):
        self.clear_screen()
        print("РАЗВИЛКА")
        print("=" * 40)
        
        left_room = self.dungeon.generate_room()
        right_room = self.dungeon.generate_room()
        
        room_names = {
            "combat": "Боевая комната",
            "treasure": "Сокровища",
            "rest": "Отдых", 
            "empty": "Пустая"
        }
        
        print("Куда пойдете?")
        print(f"1 - Налево ({room_names[left_room.room_type]})")
        print(f"2 - Направо ({room_names[right_room.room_type]})")
        print("3 - Характеристики и прокачка")
        print("4 - Инвентарь")
        print("5 - Выйти в главное меню")
        
        while True:
            choice = input("\nВыбор: ")
            
            if choice == "1":
                self.current_room = left_room
                break
            elif choice == "2":
                self.current_room = right_room
                break
            elif choice == "3":
                self.show_character()
                self.choose_path()
                return
            elif choice == "4":
                self.show_inventory()
                self.choose_path()
                return
            elif choice == "5":
                print("\nВозвращаемся в главное меню...")
                self.wait()
                self.game_running = False
                self.main_menu()
                return
            else:
                print("Неверный выбор")
    
    def show_character(self):
        while True:
            self.clear_screen()
            print("ХАРАКТЕРИСТИКИ")
            print("=" * 40)
            
            self.player.display_stats()
            
            if self.player.skill_points > 0:
                print(f"\nОчков прокачки: {self.player.skill_points}")
                print("1 - Увеличить HP")
                print("2 - Увеличить атаку")
                print("3 - Увеличить защиту")
                print("4 - Увеличить ловкость")
                print("5 - Назад к развилке")
                
                choice = input("\nВыбор: ")
                
                if choice == "1":
                    self.player.spend_skill_point("hp")
                    self.wait()
                elif choice == "2":
                    self.player.spend_skill_point("attack")
                    self.wait()
                elif choice == "3":
                    self.player.spend_skill_point("defense")
                    self.wait()
                elif choice == "4":
                    self.player.spend_skill_point("agility")
                    self.wait()
                elif choice == "5":
                    break
            else:
                print("\nНет очков прокачки.")
                print("1 - Назад к развилке")
                
                if input("\nВыбор: ") == "1":
                    break
    
    def show_inventory(self):
        self.clear_screen()
        print("ИНВЕНТАРЬ")
        print("=" * 40)
        
        self.inventory.display()
        
        print("\n1 - Использовать предмет")
        print("2 - Экипировать предмет")
        print("3 - Назад к развилке")
        
        choice = input("\nВыбор: ")
        
        if choice == "1":
            self.use_item()
            self.show_inventory()
        elif choice == "2":
            self.equip_item()
            self.show_inventory()
        elif choice == "3":
            return
    
    def use_item(self):
        if not self.inventory.items:
            print("Инвентарь пуст!")
            self.wait()
            return
        
        print("\nВаши предметы:")
        for i, item in enumerate(self.inventory.items):
            print(f"{i}: {item.name}")
        
        try:
            index = int(input("\nВыберите предмет: "))
            if 0 <= index < len(self.inventory.items):
                item = self.inventory.items[index]
                if item.use(self.player):
                    self.inventory.items.pop(index)
        except:
            print("Неверный выбор!")
        
        self.wait()
    
    def equip_item(self):
        equipable = []
        for i, item in enumerate(self.inventory.items):
            if item.item_type in ["weapon", "armor"]:
                equipable.append((i, item))
        
        if not equipable:
            print("Нет предметов для экипировки!")
            self.wait()
            return
        
        print("\nПредметы для экипировки:")
        for i, item in equipable:
            print(f"{i}: {item.name}")
        
        try:
            index = int(input("\nВыберите предмет: "))
            for real_i, item in equipable:
                if real_i == index:
                    item.equip(self.player)
                    break
        except:
            print("Неверный выбор!")
        
        self.wait()
    
    def game_over(self):
        self.clear_screen()
        print("ИГРА ОКОНЧЕНА")
        print("=" * 40)
        
        print(f"\nВаш персонаж погиб...")
        print(f"Уровень: {self.player.level}")
        print(f"Золото: {self.inventory.gold}")
        
        print("\n1 - Новая игра")
        print("2 - Выход в меню")
        
        while True:
            choice = input("\nВыбор: ")
            
            if choice == "1":
                self.player = None
                self.character_creation()
                self.start_game()
                break
            elif choice == "2":
                self.game_running = False
                self.main_menu()
                break
    
    def run(self):
        self.main_menu()

if __name__ == "__main__":
    try:
        game = TextRPG()
        game.run()
    except KeyboardInterrupt:
        print("\nИгра прервана")
    except Exception as e:
        print(f"\nОшибка: {e}")
        input()
