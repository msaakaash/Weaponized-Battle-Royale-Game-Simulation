import networkx as nx
import matplotlib.pyplot as plt
import random

class Node:
    def __init__(self, weapon):
        self.weapon = weapon
        self.next = None
        self.prev = None

class Arsenal:
    def __init__(self):
        self.head = None
        self.size = 0

    def insert_weapon_front(self, weapon):
        new_node = Node(weapon)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size += 1

    def insert_weapon_after(self, prev_node, weapon):
        if prev_node is None:
            print("Previous node cannot be null")
            return
        new_node = Node(weapon)
        new_node.next = prev_node.next
        prev_node.next = new_node
        new_node.prev = prev_node
        if new_node.next:
            new_node.next.prev = new_node
        self.size += 1

    def deleteAtX(self, pos):
        if self.size == 0 or self.size <= pos:
            print("UnderFlow")
            return None
        if self.size == pos + 1:
            if self.size == 1:
                a = self.head.weapon
                self.head = None
                self.size -= 1
                return a
            x = self.head
            for i in range(pos - 1):
                x = x.next
            y = x.next
            y.prev = None
            x.next = None
            a = y.weapon
            self.size -= 1
            return a
        elif pos == 0:
            x = self.head.next
            a = self.head.weapon
            self.head.next = None
            x.prev = None
            self.head = x
            self.size -= 1
            return a
        else:
            self.size -= 1
            x = self.head
            for i in range(pos):
                x = x.next
            a = x.weapon
            y = x.next
            z = x.prev
            y.prev = z
            z.next = y
            return a

    def display_arsenal(self, node):
        while node:
            print(node.weapon, end="->")
            last = node
            node = node.next
        print("None")

    def sizeOfArsenal(self):
        return self.size

class Junction:
    def __init__(self, name):
        self.name = name
        self.weapon = Arsenal()

    def __str__(self):
        return f"{self.name}"

class World:
    def __init__(self):
        self.vertices = {}
        self.edges = {}

    def addVertices(self, v):
        if v.name not in self.vertices:
            self.vertices[v.name] = v
            self.edges[v.name] = []

    def addEdges(self, a, b):
        if a.name not in self.vertices or b.name not in self.vertices:
            return "NoVertexError"
        else:
            self.edges[a.name].append(b.name)
            self.edges[b.name].append(a.name)

    def assignWeapons(self, weapons):
        vertices = list(self.vertices.values())
        vertices = [v for v in vertices if v.name != "Duppalapudi"]
        selected_vertices = random.sample(vertices, k=len(weapons))
        for vertex in selected_vertices:
            vertex.weapon = random.choice(weapons)

    def display(self):
        a = nx.Graph()
        a.add_nodes_from(self.vertices.values())
        for v, neighbors in self.edges.items():
            for neighbor in neighbors:
                a.add_edge(self.vertices[v], self.vertices[neighbor])

        spring_pos = nx.spring_layout(a, seed=42)

        plt.figure(figsize=(12, 9))
        nx.draw(a, pos=spring_pos, with_labels=True, node_color='lightblue', node_size=1000, font_size=8, font_weight='bold', width=1, edge_color='gray')
        plt.title("Game World Graph")
        plt.show()

class Weapon:
    def __init__(self, name, bullets, level):
        self.name = name
        self.bullets = bullets
        self.level = level

    def __str__(self):
        return f"{self.name} (Level: {self.level})"

vertices = [
    Junction("Mamidada"), Junction("Peddada"), Junction("Pedapudi"), Junction("Bikkavolu"), Junction("Voolapalli"),
    Junction("Gandredu"), Junction("Sampara"), Junction("Kandri"), Junction("Sahapura"), Junction("Kikavolu"),
    Junction("Kumaripriyam"), Junction("P.B.Devam"), Junction("Medapadu"), Junction("Vetlapalem"), Junction("Chintapalle"),
    Junction("Rajupalem"), Junction("Melluru"), Junction("Pyna"), Junction("Konkuduru"), Junction("Komaripalem"), Junction("Tossipudi"),
    Junction("Pandalapaka"), Junction("Mahendrawada"), Junction("Polamuru"), Junction("Ramavaram"), Junction("Anaparthi"),
    Junction("B.Puram"), Junction("Kotturu"), Junction("Kanedu"), Junction("R.Khandrika"), Junction("Duppalapudi"), Junction("Rayavaram")
]

edges = [
    (Junction("Mamidada"), Junction("Peddada")), (Junction("Mamidada"), Junction("Bikkavolu")), (Junction("Mamidada"), Junction("Rajupalem")),
    (Junction("Mamidada"), Junction("Voolapalli")), (Junction("Mamidada"), Junction("Gandredu")),
    (Junction("Gandredu"), Junction("Sampara")), (Junction("Gandredu"), Junction("Chintapalle")),
    (Junction("Gandredu"), Junction("Peddada")), (Junction("Gandredu"), Junction("Kumaripriyam")),
    (Junction("Sampara"), Junction("Kandri")), (Junction("Kandri"), Junction("Sahapura")),
    (Junction("Sahapura"), Junction("Kikavolu")), (Junction("Kumaripriyam"), Junction("Kikavolu")),
    (Junction("Kumaripriyam"), Junction("Pedapudi")), (Junction("Kikavolu"), Junction("Pedapudi")),
    (Junction("Peddada"), Junction("Pedapudi")), (Junction("Peddada"), Junction("Medapadu")),
    (Junction("Pedapudi"), Junction("Vetlapalem")), (Junction("Medapadu"), Junction("Vetlapalem")),
    (Junction("P.B.Devam"), Junction("Medapadu")), (Junction("Bikkavolu"), Junction("P.B.Devam")),
    (Junction("Bikkavolu"), Junction("R.Khandrika")), (Junction("Bikkavolu"), Junction("Kanedu")),
    (Junction("B.Puram"), Junction("Kotturu")), (Junction("Bikkavolu"), Junction("B.Puram")),
    (Junction("Kotturu"), Junction("Anaparthi")), (Junction("Bikkavolu"), Junction("Voolapalli")),
    (Junction("Anaparthi"), Junction("Duppalapudi")), (Junction("Kotturu"), Junction("Duppalapudi")),
    (Junction("Anaparthi"), Junction("Polamuru")), (Junction("Polamuru"), Junction("Mahendrawada")),
    (Junction("Polamuru"), Junction("Ramavaram")), (Junction("Ramavaram"), Junction("Rayavaram")),
    (Junction("Mahendrawada"), Junction("Rayavaram")), (Junction("Rayavaram"), Junction("Komaripalem")),
    (Junction("Voolapalli"), Junction("Pandalapaka")), (Junction("Pandalapaka"), Junction("Komaripalem")),
    (Junction("Pandalapaka"), Junction("Konkuduru")), (Junction("Tossipudi"), Junction("Komaripalem")),
    (Junction("Tossipudi"), Junction("Pandalapaka")), (Junction("B.Puram"), Junction("Tossipudi")),
    (Junction("Rajupalem"), Junction("Pyna")), (Junction("Pyna"), Junction("Konkuduru")),
    (Junction("Pyna"), Junction("Chintapalle")), (Junction("Chintapalle"), Junction("Melluru")),
    (Junction("Chintapalle"), Junction("Sampara")), (Junction("Konkuduru"), Junction("Melluru")),
    (Junction("Rayavaram"), Junction("Melluru")), (Junction("Rayavaram"), Junction("Konkuduru"))
]

game_world = World()
for vertex in vertices:
    game_world.addVertices(vertex)
for edge in edges:
    game_world.addEdges(edge[0], edge[1])

weapons = [
    Weapon('AKM', 40, 15),
    Weapon('M416', 40, 12),
    Weapon('M249', 100, 13),
    Weapon('Groza', 40, 17),
    Weapon('M762', 40, 14),
    Weapon('M24', 5, 18),
    Weapon('SCAR-L', 40, 11),
    Weapon('Kar98K', 5, 16),
    Weapon('UMP-45', 35, 10),
    Weapon('Uzi', 35, 9),
    Weapon('PP-Bizon', 50, 8),
    Weapon('AWM', 5, 20),
    Weapon('Mk-14', 20, 17),
    Weapon('S12K', 10, 9),
    Weapon('DBS', 10, 10),
    Weapon('S686', 2, 6)
]

l = [(2, 3, 12), (15, 1, 15), (10, 2, 10), (14, 11, 2), (10, 10, 9), (3, 5, 7), (10, 10, 6),
     (15, 13, 5), (14, 6, 8), (9, 13, 4), (2, 8, 5), (7, 2, 13), (11, 14, 1), (10, 7, 8),
     (8, 2, 8), (3, 5, 2), (4, 8, 0), (4, 9, 7), (6, 8, 11), (12, 1, 11), (2, 5, 11), (15, 14, 13),
     (3, 9, 2), (4, 15, 3), (4, 2, 9), (7, 2, 5), (9, 7, 4), (9, 1, 8),
     (3, 0, 5), (10, 14, 12), (6, 10, 14), (9, 10, 1)]

for i in range(len(l)):
    for j in l[i]:
        vertices[i].weapon.insert_weapon_front(weapons[j])

class Player:
    def __init__(self, name, position):
        self.name = name
        self.position = position
        self.health = 100
        self.weapons = []
        self.is_alive = True

    def move(self, new_position):
        if new_position in game_world.edges[self.position]:
            self.position = new_position
            print(f"{self.name} moved to {new_position}")
        else:
            print(f"Invalid move for {self.name} to {new_position}")

    def get_possible_moves(self):
        return game_world.edges[self.position]

    def pickWeapon(self):
        junction = game_world.vertices[self.position]
        if junction.weapon.sizeOfArsenal() != 0:
            junction.weapon.display_arsenal(junction.weapon.head)
            x = int(input("Enter the weapon number")) - 1
            weapon = junction.weapon.deleteAtX(x)
            self.weapons.append(weapon)
            print(f"{self.name} picked up {weapon}")
        else:
            print(f"No weapon found at {self.position}")

    def fight(self, opponent):
        if self.position == opponent.position:
            if self.weapons and opponent.weapons:
                self_weapon_level = max(weapon.level for weapon in self.weapons)
                opponent_weapon_level = max(weapon.level for weapon in opponent.weapons)
                if self_weapon_level > opponent_weapon_level:
                    opponent.takeDamage(50)
                    print(f"{self.name} won the fight against {opponent.name}")
                elif self_weapon_level < opponent_weapon_level:
                    self.takeDamage(50)
                    print(f"{opponent.name} won the fight against {self.name}")
                else:
                    print("It's a draw!")
            else:
                print("Both players need weapons to fight")
        else:
            print("Players are not in the same junction")

    def takeDamage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.is_alive = False
            junction = game_world.vertices[self.position]
            for weapon in self.weapons:
                junction.weapon.insert_weapon_front(weapon)
            print(f"{self.name} is knocked out!")

players = [
    Player("Player1", "Mamidada"),
    Player("Player2", "Bikkavolu"),
    Player("Player3", "Voolapalli")
]

while len(players) > 1:
    player_actions = {}
    print("Available players:")
    for player in players:
        print(f"Player: {player.name}, Position: {player.position}, Health: {player.health}")

    for player in players:
        print(f"\nPlayer: {player.name}")
        print("Menu:")
        print("1. Move")
        print("2. Pick Weapon")
        print("3. Fight")
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            possible_moves = player.get_possible_moves()
            print("Possible Moves:", possible_moves)
            new_position = input("Enter the junction to move: ")
            player_actions[player.name] = ('move', new_position)
        elif choice == '2':
            player_actions[player.name] = ('pick', None)
        elif choice == '3':
            player_actions[player.name] = ('fight', None)
        else:
            print("Invalid choice! Player eliminated.")
            players.remove(player)

    for player_name, action in player_actions.items():
        if player_name in [player.name for player in players]:  # Ensure player is still in the game
            player = next(p for p in players if p.name == player_name)
            if action[0] == 'fight':
                other_players = [p for p in players if p.name != player_name and p.position == player.position]
                if other_players:
                    opponent = other_players[0]
                    player.fight(opponent)
                    if not player.is_alive:
                        players.remove(player)
                    if not opponent.is_alive:
                        players.remove(opponent)
            elif action[0] == 'pick':
                player.pickWeapon()
            elif action[0] == 'move':
                new_position = action[1]
                player.move(new_position)
                if not player.is_alive:
                    players.remove(player)

    game_world.display()

if players:
    print(f"\nWinner: {players[0].name}")
else:
    print("No winner! All players are eliminated.")
