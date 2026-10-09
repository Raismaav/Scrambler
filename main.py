import random

# Diccionario de movimientos permitidos por categoría
scramble_config = {
    "2x2": {"moves": ["R", "U", "F"], "length": 10},
    "3x3": {"moves": ["R", "L", "U", "D", "F", "B"], "length": 20},
    "4x4": {"moves": ["R", "L", "U", "D", "F", "B", "Rw", "Uw", "Fw"], "length": 40},
    "5x5": {"moves": ["R", "L", "U", "D", "F", "B", "Rw", "Lw", "Uw", "Dw", "Fw", "Bw"], "length": 60},
    "6x6": {"moves": ["R", "L", "U", "D", "F", "B", "Rw", "Lw", "Uw", "Dw", "Fw", "Bw", "3Rw", "3Uw", "3Fw"], "length": 80},
    "7x7": {"moves": ["R", "L", "U", "D", "F", "B", "Rw", "Lw", "Uw", "Dw", "Fw", "Bw", "3Rw", "3Lw", "3Uw", "3Dw", "3Fw", "3Bw"], "length": 80},
}

# Modificadores de los movimientos
modifiers = ["", "'", "2"]

def generate_random_move(moves, previous_move=None):
    """Genera un movimiento aleatorio sin repetir la misma cara consecutiva."""
    move = random.choice(moves)
    while previous_move and move[0] == previous_move[0]:
        move = random.choice(moves)
    modifier = random.choice(modifiers)
    return f"{move}{modifier}"

def generate_scramble(cube_type="3x3"):
    """Genera un scramble de acuerdo con la categoría NxN."""
    if cube_type not in scramble_config:
        raise ValueError(f"Categoría no soportada: {cube_type}")

    config = scramble_config[cube_type]
    moves = config["moves"]
    length = config["length"]

    scramble = []
    previous_move = None
    for _ in range(length):
        move = generate_random_move(moves, previous_move)
        scramble.append(move)
        previous_move = move

    return " ".join(scramble)

print(generate_scramble("3x3"))
