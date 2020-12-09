from tkinter import *
from random import randrange
root = Tk()
root.title('Tic-tac-toe')

players_count = 2
turn = 'X'
x_wins = 0
o_wins = 0
draws = 0

indexes = ['  ' for i in range(9)]


def check_win():
    collection = (indexes[:3], indexes[3:6], indexes[6:9], indexes[::3],
                  indexes[1::3], indexes[2::3], indexes[::4], indexes[2:7:2])
    if ['X', 'X', 'X'] in collection:
        return 'X Player Won The Game'
    elif ['O', 'O', 'O'] in collection:
        return 'O Player Won The Game'
    elif '  ' not in indexes:
        return 'The Game Is Draw'


def game_turn():
    global x_wins, o_wins, draws, turn
    if check_win() == 'X Player Won The Game':
        x_wins += 1
        turn = 'X'
    elif check_win() == 'O Player Won The Game':
        o_wins += 1
        turn = 'O'
    elif check_win() == 'The Game Is Draw':
        draws += 1
        turn = 'X' if turn == 'O' else 'O'


def players():
    global players_count
    players_count = 1 if players_count == 2 else 2
    show_board()
    play_computer()


def play_computer():
    if players_count == 1 and turn == 'O':
        computer_choice = randrange(0, 9)
        while indexes[computer_choice] != '  ':
            computer_choice = randrange(0, 9)
        clicked(computer_choice)


def clicked(place):
    global turn, indexes, o_wins, x_wins, draws, frame_board
    if indexes[place] == '  ':
        indexes[place] = turn
        turn = 'X' if turn == 'O' else 'O'
        show_board()

        if check_win():
            game_turn()
            second_window(check_win())

            indexes = ['  ' for i in range(9)]
            frame_board.destroy()
            frame_board = LabelFrame(root, padx=5, pady=5)
            frame_board.grid(row=1, pady=5)
            show_board()

    play_computer()


frame_turn = LabelFrame(root)
frame_turn.grid(row=0)

frame_board = LabelFrame(root, padx=5, pady=5)
frame_board.grid(row=1, pady=5)

frame_stats = LabelFrame(root)
frame_stats.grid(row=2)

frame_player = LabelFrame(root)
frame_player.grid(row=3, pady=5)


def show_board():

    turn_label = Label(
        frame_turn, text=f'Turn: {turn}-Player', font=('Halvetica', 20))
    turn_label.grid(row=0)

    index0 = Button(frame_board, text=indexes[0], font=(
        'Halvetica', 25), command=lambda: clicked(0))
    index1 = Button(frame_board, text=indexes[1], font=(
        'Halvetica', 25), command=lambda: clicked(1))
    index2 = Button(frame_board, text=indexes[2], font=(
        'Halvetica', 25), command=lambda: clicked(2))
    index3 = Button(frame_board, text=indexes[3], font=(
        'Halvetica', 25), command=lambda: clicked(3))
    index4 = Button(frame_board, text=indexes[4], font=(
        'Halvetica', 25), command=lambda: clicked(4))
    index5 = Button(frame_board, text=indexes[5], font=(
        'Halvetica', 25), command=lambda: clicked(5))
    index6 = Button(frame_board, text=indexes[6], font=(
        'Halvetica', 25), command=lambda: clicked(6))
    index7 = Button(frame_board, text=indexes[7], font=(
        'Halvetica', 25), command=lambda: clicked(7))
    index8 = Button(frame_board, text=indexes[8], font=(
        'Halvetica', 25), command=lambda: clicked(8))

    index0.grid(row=0, column=0, padx=3, pady=3)
    index1.grid(row=0, column=1, padx=3, pady=3)
    index2.grid(row=0, column=2, padx=3, pady=3)
    index3.grid(row=1, column=0, padx=3, pady=3)
    index4.grid(row=1, column=1, padx=3, pady=3)
    index5.grid(row=1, column=2, padx=3, pady=3)
    index6.grid(row=2, column=0, padx=3, pady=3)
    index7.grid(row=2, column=1, padx=3, pady=3)
    index8.grid(row=2, column=2, padx=3, pady=3)

    x_stats = Label(
        frame_stats, text=f'X-Wins\n{x_wins}', font=('Halvetica', 20))
    o_stats = Label(
        frame_stats, text=f'O-Wins\n{o_wins}', font=('Halvetica', 20))
    draws_stats = Label(
        frame_stats, text=f'Draws\n{draws}', font=('Halvetica', 20))

    x_stats.grid(row=0, column=0)
    o_stats.grid(row=0, column=1)
    draws_stats.grid(row=0, column=2)

    players_btn = Button(
        frame_player, text=f'{players_count} Players', font=('Halvetica', 20), command=players)
    players_btn.grid(row=0)


def second_window(message):
    top = Toplevel()
    top.title('Winner')
    frame1 = LabelFrame(top, padx=5, pady=5)
    frame1.pack(padx=10, pady=10)
    for i in range(3):
        for j in range(3):
            Button(frame1, text=indexes[i*3+j],
                   font=('Halvetica', 15)).grid(row=i, column=j)

    Label(top, text=message, font=('Halvetica', 15)).pack()

    Button(top, text='Close', border=2, font=(
        'Halvetica', 15), command=top.destroy).pack()


show_board()

root.mainloop()
