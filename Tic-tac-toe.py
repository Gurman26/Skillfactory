def print_board(board):
    print("  0 1 2")
    for i, row in enumerate(board):
        print(f"{i} {' '.join(row)}")


def check_winner(board, player):
    # Проверка строк
    for row in board:
        if all(cell == player for cell in row):
            return True
    # Проверка столбцов
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    # Проверка диагоналей
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False


def is_board_full(board):
    return all(cell != '-' for row in board for cell in row)


def get_valid_input(prompt):
    while True:
        value = input(prompt)
        if value.isdigit():
            value = int(value)
            if 0 <= value <= 2:
                return value
        print("Некорректный ввод. Пожалуйста, введите число от 0 до 2.")


def main():
    board = [['-' for _ in range(3)] for _ in range(3)]
    players = ['X', 'O']
    current_player = 0

    while True:
        print_board(board)

        row = get_valid_input(f"Игрок {players[current_player]}, введите номер строки: ")
        col = get_valid_input(f"Игрок {players[current_player]}, введите номер столбца: ")

        if board[row][col] != '-':
            print("Эта клетка уже занята, выберите другую.")
            continue

        board[row][col] = players[current_player]

        if check_winner(board, players[current_player]):
            print_board(board)
            print(f"Игрок {players[current_player]} победил!")
            break

        if is_board_full(board):
            print_board(board)
            print("Игра закончилась ничьей, победила дружба!")
            break

        current_player = 1 - current_player


if __name__ == "__main__":
    main()