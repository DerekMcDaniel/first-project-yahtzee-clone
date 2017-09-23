from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import random
import winsound
import time

root = Tk()

#  image open and imageTk required to extend support for png file display
dice1 = Image.open("dice1.png")
dice1pic = ImageTk.PhotoImage(dice1)
dice2 = Image.open("dice2.png")
dice2pic = ImageTk.PhotoImage(dice2)
dice3 = Image.open("dice3.png")
dice3pic = ImageTk.PhotoImage(dice3)
dice4 = Image.open("dice4.png")
dice4pic = ImageTk.PhotoImage(dice4)
dice5 = Image.open("dice5.png")
dice5pic = ImageTk.PhotoImage(dice5)
dice6 = Image.open("dice6.png")
dice6pic = ImageTk.PhotoImage(dice6)
placeholder1 = Image.open("p1image.jpg")
placeholder1_img = ImageTk.PhotoImage(placeholder1)
dork1 = Image.open("dork1.jpg")
dork1pic = ImageTk.PhotoImage(dork1)
dork2 = Image.open("dork2.jpg")
dork2pic = ImageTk.PhotoImage(dork2)
dork3 = Image.open("dork3.jpg")
dork3pic = ImageTk.PhotoImage(dork3)
dork4 = Image.open("dork4.jpg")
dork4pic = ImageTk.PhotoImage(dork4)

#  Main Frames SETUP
top_center = Frame(root, bg="black", pady=30)
top_center.pack(fill=X)
top_frame = Frame(top_center, bg="black", padx=100, pady=20)
top_frame.pack(side=TOP, anchor=CENTER)

mid_frame = Frame(root, bg="black", pady=30)
mid_frame.pack(fill=X)

p1_upper_score_frame = Frame(root, pady=10)
p1_upper_score_frame.pack()
p1_bot_frame = Frame(root, pady=10)
p1_bot_frame.pack()

p2_upper_score_frame = Frame(root, pady=10)
p2_upper_score_frame.pack()
p2_bot_frame = Frame(root, pady=10)
p2_bot_frame.pack()

final_score_frame = Frame(root)
final_score_frame.pack(fill=X)

final_score_frame_left = Frame(final_score_frame)
final_score_frame_left.pack(side=LEFT)

final_score_frame_right = Frame(final_score_frame)
final_score_frame_right.pack(side=RIGHT)


#  Classes
class Game:
    def __init__(self, player_a, player_b):
        self.num_to_roll = 5
        self.has_started = False
        self.player_a = player_a
        self.player_b = player_b
        self.current_player = 1
        self.current_roll = []
        self.pic_list = [dork1pic, dork2pic, dork3pic, dork4pic]
        self.top_frame1 = Frame(top_center, bg="black", padx=100, pady=20)
        self.top_frame1.pack(side=TOP, anchor=CENTER)

        self.button1 = Button(self.top_frame1, bg='khaki1', image=placeholder1_img, command=lambda: hold_me("button1"))
        self.button2 = Button(self.top_frame1, bg='khaki1', image=placeholder1_img, command=lambda: hold_me("button2"))
        self.button3 = Button(self.top_frame1, bg='khaki1', image=placeholder1_img, command=lambda: hold_me("button3"))
        self.button4 = Button(self.top_frame1, bg='khaki1', image=placeholder1_img, command=lambda: hold_me("button4"))
        self.button5 = Button(self.top_frame1, bg='khaki1', image=placeholder1_img, command=lambda: hold_me("button5"))

        self.button_list = [self.button1, self.button2, self.button3, self.button4, self.button5]

        self.button1.pack(side=LEFT)
        self.button2.pack(side=LEFT)
        self.button3.pack(side=LEFT)
        self.button4.pack(side=LEFT)
        self.button5.pack(side=LEFT)

    def reset(self):
        self.button1.configure(bg='khaki1', image=random.choice(self.pic_list), command=lambda: hold_me("button1"))
        self.button2.configure(bg='khaki1', image=random.choice(self.pic_list), command=lambda: hold_me("button2"))
        self.button3.configure(bg='khaki1', image=random.choice(self.pic_list), command=lambda: hold_me("button3"))
        self.button4.configure(bg='khaki1', image=random.choice(self.pic_list), command=lambda: hold_me("button4"))
        self.button5.configure(bg='khaki1', image=random.choice(self.pic_list), command=lambda: hold_me("button5"))

    def set_player(self):
        now_playing = yahtzee.get_player()
        if now_playing.top_half_count == 6:
            score_total1()
            score_bonus()
            score_total2()
        if now_playing.bottom_half_count == 7 and now_playing.top_half_count == 6:
            score_bot_total()
            score_grand_total()
        now_playing_text.configure(text="TURN ENDED!!! No More Scoring!", bg="yellow")
        self.current_player = (self.current_player * -1)
        if self.current_player == 1:
            player_turn = self.player_a
            self.player_b.control_dict = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
            self.player_b.turn_count = 1
            yahtzee.reset()
        else:
            player_turn = self.player_b
            self.player_a.turn_count = 1
            self.player_a.control_dict = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
            yahtzee.reset()
        return player_turn

    def get_player(self):
        if self.current_player == 1:
            player_turn = self.player_a
            p1_upper_score_frame.pack()
            p1_bot_frame.pack()
            p2_upper_score_frame.pack_forget()
            p2_bot_frame.pack_forget()
        else:
            player_turn = self.player_b
            p1_upper_score_frame.pack_forget()
            p1_bot_frame.pack_forget()
            p2_upper_score_frame.pack()
            p2_bot_frame.pack()
        return player_turn

    def roll(self, num_to_roll):
        self.has_started = True
        winsound.PlaySound("dice_sound", winsound.SND_ASYNC)
        now_playing = yahtzee.get_player()
        now_playing.turn_count += 1
        for i in range(0, num_to_roll):
            i = random.randint(1, 6)
            self.current_roll.append(i)
        counter = 0
        for i in self.current_roll:
            if self.button_list[counter].cget('bg') == 'khaki1':
                if i == 1:
                    self.button_list[counter].configure(image=dice1pic)
                    self.button_list[counter].image = dice1pic
                elif i == 2:
                    self.button_list[counter].configure(image=dice2pic)
                    self.button_list[counter].image = dice2pic
                elif i == 3:
                    self.button_list[counter].configure(image=dice3pic)
                    self.button_list[counter].image = dice3pic
                elif i == 4:
                    self.button_list[counter].configure(image=dice4pic)
                    self.button_list[counter].image = dice4pic

                elif i == 5:
                    self.button_list[counter].configure(image=dice5pic)
                    self.button_list[counter].image = dice5pic

                else:
                    self.button_list[counter].configure(image=dice6pic)
                    self.button_list[counter].image = dice6pic
            counter += 1
        self.current_roll.clear()


class Player:
    def __init__(self):
        self.turn_count = 1
        self.top_half_count = 0
        self.bottom_half_count = 0
        self.score_dict = {}
        self.score_dict_bot = {}
        self.control_dict = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}


# Functions

#  Intro event shows random dorky pictures when the mouse moves
# noinspection PyUnusedLocal
def intro(event):
    if not yahtzee.has_started:
        for i in yahtzee.button_list:
            i.configure(image=random.choice(yahtzee.pic_list))
            time.sleep(0.05)


root.bind("<Motion>", intro)


def remove_me(name):
    if name == 'button1':
        yahtzee.button1.configure(bg='khaki1', command=lambda: hold_me('button1'))
    elif name == 'button2':
        yahtzee.button2.configure(bg='khaki1', command=lambda: hold_me('button2'))
    elif name == 'button3':
        yahtzee.button3.configure(bg='khaki1', command=lambda: hold_me('button3'))
    elif name == 'button4':
        yahtzee.button4.configure(bg='khaki1', command=lambda: hold_me('button4'))
    elif name == 'button5':
        yahtzee.button5.configure(bg='khaki1', command=lambda: hold_me('button5'))


def hold_me(name):
    if name == 'button1':
        yahtzee.button1.configure(bg='dodger blue', command=lambda: remove_me('button1'))
    elif name == 'button2':
        yahtzee.button2.configure(bg='dodger blue', command=lambda: remove_me('button2'))
    elif name == 'button3':
        yahtzee.button3.configure(bg='dodger blue', command=lambda: remove_me('button3'))
    elif name == 'button4':
        yahtzee.button4.configure(bg='dodger blue', command=lambda: remove_me('button4'))
    elif name == 'button5':
        yahtzee.button5.configure(bg='dodger blue', command=lambda: remove_me('button5'))


def roll_it():
    now_playing = yahtzee.get_player()  # get the current player
    if now_playing.turn_count < 4:
        yahtzee.roll(5)
    else:
        messagebox.showinfo("No More Rolls", "No More Rolls, Enter A Score!")
    if now_playing == yahtzee.player_a:
        whose_turn = "Player 1"
    else:
        whose_turn = "Player 2"
    now_playing_text.configure(text=whose_turn, bg="red")


# Scoring
def score_aces():
    now_playing = yahtzee.get_player()
    now_playing.top_half_count += 1
    current_dice = []
    for child in yahtzee.top_frame1.pack_slaves():  # get buttons
        current_dice.append(int(child.cget('image').split('e')[1]))  # get images, split at 'e'. return trailing #
    score = 0
    for num in current_dice:
        if num == 1:
            score += 1
    now_playing.score_dict["Aces"] = score
    if now_playing == yahtzee.player_a:
        aces_label.configure(text=score)
    else:
        p2aces_label.configure(text=score)
    yahtzee.set_player()


def score_twos():
    now_playing = yahtzee.get_player()
    now_playing.top_half_count += 1
    current_dice = []
    for child in yahtzee.top_frame1.pack_slaves():  # get buttons
        current_dice.append(int(child.cget('image').split('e')[1]))  # get images, split at 'e'. return trailing #
    score = 0
    for num in current_dice:
        if num == 2:
            score += 2
    now_playing.score_dict["Twos"] = score
    if now_playing == yahtzee.player_a:
        twos_label.configure(text=score)
    else:
        p2twos_label.configure(text=score)
    yahtzee.set_player()


def score_threes():
    now_playing = yahtzee.get_player()
    now_playing.top_half_count += 1
    current_dice = []
    for child in yahtzee.top_frame1.pack_slaves():  # get buttons
        current_dice.append(int(child.cget('image').split('e')[1]))  # get images, split at 'e'. return trailing #
    score = 0
    for num in current_dice:
        if num == 3:
            score += 3
    now_playing.score_dict["Threes"] = score
    if now_playing == yahtzee.player_a:
        threes_label.configure(text=score)
    else:
        p2threes_label.configure(text=score)
    yahtzee.set_player()


def score_fours():
    now_playing = yahtzee.get_player()
    now_playing.top_half_count += 1
    current_dice = []
    for child in yahtzee.top_frame1.pack_slaves():  # get buttons
        current_dice.append(int(child.cget('image').split('e')[1]))  # get images, split at 'e'. return trailing #
    score = 0
    for num in current_dice:
        if num == 4:
            score += 4
    now_playing.score_dict["Fours"] = score
    if now_playing == yahtzee.player_a:
        fours_label.configure(text=score)
    else:
        p2fours_label.configure(text=score)
    yahtzee.set_player()


def score_fives():
    now_playing = yahtzee.get_player()
    now_playing.top_half_count += 1
    current_dice = []
    for child in yahtzee.top_frame1.pack_slaves():  # get buttons
        current_dice.append(int(child.cget('image').split('e')[1]))  # get images, split at 'e'. return trailing #
    score = 0
    for num in current_dice:
        if num == 5:
            score += 5
    now_playing.score_dict["Fives"] = score
    if now_playing == yahtzee.player_a:
        fives_label.configure(text=score)
    else:
        p2fives_label.configure(text=score)
    yahtzee.set_player()


def score_sixes():
    now_playing = yahtzee.get_player()
    now_playing.top_half_count += 1
    current_dice = []
    for child in yahtzee.top_frame1.pack_slaves():  # get buttons
        current_dice.append(int(child.cget('image').split('e')[1]))  # get images, split at 'e'. return trailing #
    score = 0
    for num in current_dice:
        if num == 6:
            score += 6
    now_playing.score_dict["Sixes"] = score
    if now_playing == yahtzee.player_a:
        sixes_label.configure(text=score)
    else:
        p2sixes_label.configure(text=score)
    yahtzee.set_player()


def score_total1():
    now_playing = yahtzee.get_player()
    score = 0
    for k, v in now_playing.score_dict.items():
        if k != "Total1" and k != "Bonus" and k != "Total2":
            score += v
    now_playing.score_dict["Total1"] = score
    if now_playing == yahtzee.player_a:
        p1_top_score.configure(text=("Player 1 Top Half:  " + str(score)))
        total_1_label.configure(text=score)
    else:
        p2total_1_label.configure(text=score)
        p2_top_score.configure(text=("Player 2 Top Half:  " + str(score)))


def score_bonus():
    now_playing = yahtzee.get_player()
    if 'Total1' in now_playing.score_dict:
        if now_playing.score_dict["Total1"] >= 63:
            score = 35
        else:
            score = 0
        now_playing.score_dict["Bonus"] = score
        if now_playing == yahtzee.player_a:
            bonus_label.configure(text=score)
            p1_bonus_score.configure(text=("Player 1 Bonus:  " + str(score)))
        else:
            p2bonus_label.configure(text=score)
            p2_bonus_score.configure(text=("Player 2 Bonus:  " + str(score)))
    else:
        messagebox.showinfo('Score Total1', 'You must calculate total1 first')


def score_total2():
    now_playing = yahtzee.get_player()
    if 'Bonus' and 'Total1' in now_playing.score_dict:
        score = (now_playing.score_dict["Total1"] + now_playing.score_dict["Bonus"])
        now_playing.score_dict["Total2"] = score

        if now_playing == yahtzee.player_a:
            total_2_label.configure(text=score)
            p1_top_total_score.configure(text=("Player 1 Total:  " + str(score)))
        else:
            p2total_2_label.configure(text=score)
            p2_top_total_score.configure(text=("Player 2 Total:  " + str(score)))
    else:
        messagebox.showinfo('Score Bonus', 'You must calculate total1 and bonus score first!')


def score_3_kind():
    now_playing = yahtzee.get_player()
    now_playing.bottom_half_count += 1
    current_dice = []
    for child in yahtzee.top_frame1.pack_slaves():  # get buttons
        current_dice.append(int(child.cget('image').split('e')[1]))  # get images, split at 'e'. return trailing #
    score = 0
    valid = 0
    for i in current_dice:
        for k, v in now_playing.control_dict.items():
            if i == k:
                now_playing.control_dict[k] = v + 1
    for k, v in now_playing.control_dict.items():
        if v >= 3:
            valid = 1
    if valid == 1:
        for k, v in now_playing.control_dict.items():
            if v >= 3 or v == 2 or v == 1:
                score += k * v
    else:
        score = 0
    now_playing.score_dict_bot["3 Of A Kind"] = score
    if now_playing == yahtzee.player_a:
        three_kind_label.configure(text=score)
    else:
        p2three_kind_label.configure(text=score)
    yahtzee.set_player()


def score_4_kind():
    now_playing = yahtzee.get_player()
    now_playing.bottom_half_count += 1
    current_dice = []
    for child in yahtzee.top_frame1.pack_slaves():  # get buttons
        current_dice.append(int(child.cget('image').split('e')[1]))  # get images, split at 'e'. return trailing #
    score = 0
    valid = 0
    for i in current_dice:
        for k, v in now_playing.control_dict.items():
            if i == k:
                now_playing.control_dict[k] = v + 1
    for k, v in now_playing.control_dict.items():
        if v == 4:
            valid = 1
    if valid == 1:
        for k, v in now_playing.control_dict.items():
            if v == 4 or v == 1:
                score += k * v
    else:
        score = 0
    now_playing.score_dict_bot["4 Of A Kind"] = score
    if now_playing == yahtzee.player_a:
        four_kind_label.configure(text=score)
    else:
        p2four_kind_label.configure(text=score)
    yahtzee.set_player()


def score_full_house():
    now_playing = yahtzee.get_player()
    now_playing.bottom_half_count += 1
    current_dice = []
    for child in yahtzee.top_frame1.pack_slaves():  # get buttons
        current_dice.append(int(child.cget('image').split('e')[1]))  # get images, split at 'e'. return trailing #
    score = 0
    valid = 0
    for i in current_dice:
        for k, v in now_playing.control_dict.items():
            if i == k:
                now_playing.control_dict[k] = v + 1
    for k, v in now_playing.control_dict.items():
        if v == 3:
            valid = 1
    for k, v in now_playing.control_dict.items():
        if v == 2:
            valid += 1
    if valid == 2:
        for k, v in now_playing.control_dict.items():
            if v == 3 or v == 2:
                score = 25
    else:
        score = 0
    now_playing.score_dict_bot["Full House"] = score
    if now_playing == yahtzee.player_a:
        full_house_label.configure(text=score)
    else:
        p2full_house_label.configure(text=score)
    yahtzee.set_player()


def score_small_straight():
    now_playing = yahtzee.get_player()
    now_playing.bottom_half_count += 1
    current_dice = []
    for child in yahtzee.top_frame1.pack_slaves():  # get buttons
        current_dice.append(int(child.cget('image').split('e')[1]))  # get images, split at 'e'. return trailing #
    valid1 = set([1, 2, 3, 4])
    valid2 = set([2, 3, 4, 5])
    valid3 = set([3, 4, 5, 6])
    check = set(current_dice)
    if len(valid1 & check) >= 4:
        score = 30
    elif len(valid2 & check) >= 4:
        score = 30
    elif len(valid3 & check) >= 4:
        score = 30
    else:
        score = 0
    now_playing.score_dict_bot["Small Straight"] = score
    if now_playing == yahtzee.player_a:
        small_straight_label.configure(text=score)
    else:
        p2small_straight_label.configure(text=score)
    yahtzee.set_player()


def score_large_straight():
    now_playing = yahtzee.get_player()
    now_playing.bottom_half_count += 1
    current_dice = []
    for child in yahtzee.top_frame1.pack_slaves():  # get buttons
        current_dice.append(int(child.cget('image').split('e')[1]))  # get images, split at 'e'. return trailing #
    control_list = []
    for i in current_dice:
        for k, v in now_playing.control_dict.items():
            if i == k:
                now_playing.control_dict[k] = v + 1
    for k, v in now_playing.control_dict.items():
        if v >= 1:
            control_list.append(k)
    if len(control_list) >= 5:
        score = 40
    else:
        score = 0
    now_playing.score_dict_bot["Large Straight"] = score
    if now_playing == yahtzee.player_a:
        large_straight_label.configure(text=score)
    else:
        p2large_straight_label.configure(text=score)
    yahtzee.set_player()


def score_chance():
    now_playing = yahtzee.get_player()
    now_playing.bottom_half_count += 1
    current_dice = []
    for child in yahtzee.top_frame1.pack_slaves():  # get buttons
        current_dice.append(int(child.cget('image').split('e')[1]))  # get images, split at 'e'. return trailing #
    score = 0
    for i in current_dice:
        for k, v in now_playing.control_dict.items():
            if i == k:
                now_playing.control_dict[k] = v + 1
    for k, v in now_playing.control_dict.items():
        if v > 0:
            score += k * v
    now_playing.score_dict_bot["Chance"] = score
    if now_playing == yahtzee.player_a:
        chance_label.configure(text=score)
    else:
        p2chance_label.configure(text=score)
    yahtzee.set_player()


def score_yahtzee():
    now_playing = yahtzee.get_player()
    current_dice = []
    for child in yahtzee.top_frame1.pack_slaves():  # get buttons
        current_dice.append(int(child.cget('image').split('e')[1]))  # get images, split at 'e'. return trailing #
    score = 0
    valid = 0
    for i in current_dice:
        for k, v in now_playing.control_dict.items():
            if i == k:
                now_playing.control_dict[k] = v + 1
    for k, v in now_playing.control_dict.items():
        if v == 5:
            valid = 1
    if valid == 1:
        if "Yahtzee" in now_playing.score_dict_bot:  # check to see if a yahtzee has been scored
            if now_playing.score_dict_bot["Yahtzee"] < 350:  # Ensure max of 3 bonus yahtzees
                if now_playing.score_dict_bot["Yahtzee"] >= 50:  # check to see if a yahtzee has been scored
                    score = now_playing.score_dict_bot["Yahtzee"]
                    score += 100  # if yahtzee has been scored add 100 for each bonus
            else:
                score = now_playing.score_dict_bot["Yahtzee"]
                messagebox.showinfo('NOPE', 'You can only have 3 bonus Yahtzees')
        else:
            score = 50  # score 50 for first yahtzee
            now_playing.bottom_half_count += 1
    else:
        score = 0
        now_playing.bottom_half_count += 1
    now_playing.score_dict_bot["Yahtzee"] = score
    if now_playing == yahtzee.player_a:
        yahtzee_label.configure(text=score)
    else:
        p2yahtzee_label.configure(text=score)
    yahtzee.set_player()


def score_bot_total():
    now_playing = yahtzee.get_player()
    score = 0
    for k, v in now_playing.score_dict_bot.items():
        score += v
    now_playing.score_dict_bot["Bot_Total"] = score
    if now_playing == yahtzee.player_a:
        bot_total_label.configure(text=score)
    else:
        p2bot_total_label.configure(text=score)


# noinspection PyBroadException
def score_grand_total():
    now_playing = yahtzee.get_player()
    score = 0
    if 'Total2' in now_playing.score_dict:
        score += now_playing.score_dict['Total2']
        score += now_playing.score_dict_bot['Bot_Total']
        now_playing.score_dict_bot["Grand Total"] = score
        if now_playing == yahtzee.player_a:
            p1_final_score.configure(text=("Player 1 Grand Total:   " + str(score)))
            grand_total_label.configure(text=score)
        else:
            p2grand_total_label.configure(text=score)
            p2_final_score.configure(text=("Player 2 Grand Total:   " + str(score)))
    try:
        if yahtzee.player_a.score_dict_bot["Grand Total"] > yahtzee.player_b.score_dict_bot["Grand Total"]:
            winner = Label(mid_frame, text="Player One Wins!!!!", font="-weight bold", bg="red")
            winner.pack(ipadx=10, ipady=10)
        else:
            winner = Label(mid_frame, text="Player Two Wins!!!!", font="-weight bold", bg="red")
            winner.pack(ipadx=10, ipady=10)
    except:
        pass


# SETUP
winsound.PlaySound("game_music.wav", winsound.SND_ASYNC | winsound.SND_LOOP)

p1 = Player()  # create object of player class
p2 = Player()  # create object of player class

yahtzee = Game(p1, p2)   # pass in p1 and p2 to Game class

# game play buttons
now_playing_text = Label(mid_frame, text="Let's Play!", bg='red', font="-weight bold")
now_playing_text.pack(ipadx=10, ipady=10)

roll_button = Button(mid_frame, text="Roll!", command=roll_it, font="-weight bold")
roll_button.pack(pady=20)

#  Additional Score Display - Left & Right Side
p1_top_score = Label(final_score_frame_left, text='Player 1 Top-Half Score')
p1_bonus_score = Label(final_score_frame_left, text='Player 1 Bonus Score')
p1_top_total_score = Label(final_score_frame_left, text='Player 1 Top-Half Total Score')
p1_final_score = Label(final_score_frame_left, text='Player 1 Grand Total')

p1_top_score.pack(anchor=W)
p1_bonus_score.pack(anchor=W)
p1_top_total_score.pack(anchor=W)
p1_final_score.pack(anchor=W)

p2_top_score = Label(final_score_frame_right, text='Player 2 Top-Half Score')
p2_bonus_score = Label(final_score_frame_right, text='Player 2 Bonus Score')
p2_top_total_score = Label(final_score_frame_right, text='Player 2 Top-Half Total Score')
p2_final_score = Label(final_score_frame_right, text='Player 2 Grand Total')

p2_top_score.pack(anchor=E)
p2_bonus_score.pack(anchor=E)
p2_top_total_score.pack(anchor=E)
p2_final_score.pack(anchor=E)

#  Player 1 Score Frames - Packed here and unpacked when player changes
aces_label = Button(p1_upper_score_frame, text='aces', command=score_aces)
aces_label.pack(side=LEFT, ipadx=10)

twos_label = Button(p1_upper_score_frame, text='twos', command=score_twos)
twos_label.pack(side=LEFT, ipadx=10)

threes_label = Button(p1_upper_score_frame, text='threes', command=score_threes)
threes_label.pack(side=LEFT, ipadx=10)

fours_label = Button(p1_upper_score_frame, text='fours', command=score_fours)
fours_label.pack(side=LEFT, ipadx=10)

fives_label = Button(p1_upper_score_frame, text='fives', command=score_fives)
fives_label.pack(side=LEFT, ipadx=10)

sixes_label = Button(p1_upper_score_frame, text='sixes', command=score_sixes)
sixes_label.pack(side=LEFT, ipadx=10)

total_1_label = Button(p1_upper_score_frame, text='total 1')
total_1_label.pack(side=LEFT, ipadx=10)

bonus_label = Button(p1_upper_score_frame, text='bonus')
bonus_label.pack(side=LEFT, ipadx=10)

total_2_label = Button(p1_upper_score_frame, text='total 2')
total_2_label.pack(side=LEFT, ipadx=10)

three_kind_label = Button(p1_bot_frame, text="3 of a kind", command=score_3_kind)
three_kind_label.pack(side=LEFT)

four_kind_label = Button(p1_bot_frame, text="4 of a kind", command=score_4_kind)
four_kind_label.pack(side=LEFT)

full_house_label = Button(p1_bot_frame, text="Full House", command=score_full_house)
full_house_label.pack(side=LEFT)

small_straight_label = Button(p1_bot_frame, text="Small Straight", command=score_small_straight)
small_straight_label.pack(side=LEFT)

large_straight_label = Button(p1_bot_frame, text="Large Straight", command=score_large_straight)
large_straight_label.pack(side=LEFT)

chance_label = Button(p1_bot_frame, text="Chance", command=score_chance)
chance_label.pack(side=LEFT)

yahtzee_label = Button(p1_bot_frame, text="Yahtzee!", command=score_yahtzee)
yahtzee_label.pack(side=LEFT)

bot_total_label = Button(p1_bot_frame, text="Bottom Total")
bot_total_label.pack(side=LEFT)

grand_total_label = Button(p1_bot_frame, text="Grand Total")
grand_total_label.pack(side=LEFT)

#  Player 2 score frames
p2aces_label = Button(p2_upper_score_frame, text='aces', command=score_aces)
p2aces_label.pack(side=LEFT)

p2twos_label = Button(p2_upper_score_frame, text='twos', command=score_twos)
p2twos_label.pack(side=LEFT)

p2threes_label = Button(p2_upper_score_frame, text='threes', command=score_threes)
p2threes_label.pack(side=LEFT)

p2fours_label = Button(p2_upper_score_frame, text='fours', command=score_fours)
p2fours_label.pack(side=LEFT)

p2fives_label = Button(p2_upper_score_frame, text='fives', command=score_fives)
p2fives_label.pack(side=LEFT)

p2sixes_label = Button(p2_upper_score_frame, text='sixes', command=score_sixes)
p2sixes_label.pack(side=LEFT)

p2total_1_label = Button(p2_upper_score_frame, text='total 1')
p2total_1_label.pack(side=LEFT)

p2bonus_label = Button(p2_upper_score_frame, text='bonus')
p2bonus_label.pack(side=LEFT)

p2total_2_label = Button(p2_upper_score_frame, text='total 2')
p2total_2_label.pack(side=LEFT)

p2three_kind_label = Button(p2_bot_frame, text="3 of a kind", command=score_3_kind)
p2three_kind_label.pack(side=LEFT)

p2four_kind_label = Button(p2_bot_frame, text="4 of a kind", command=score_4_kind)
p2four_kind_label.pack(side=LEFT)

p2full_house_label = Button(p2_bot_frame, text="Full House", command=score_full_house)
p2full_house_label.pack(side=LEFT)

p2small_straight_label = Button(p2_bot_frame, text="Small Straight", command=score_small_straight)
p2small_straight_label.pack(side=LEFT)

p2large_straight_label = Button(p2_bot_frame, text="Large Straight", command=score_large_straight)
p2large_straight_label.pack(side=LEFT)

p2chance_label = Button(p2_bot_frame, text="Chance", command=score_chance)
p2chance_label.pack(side=LEFT)

p2yahtzee_label = Button(p2_bot_frame, text="Yahtzee!", command=score_yahtzee)
p2yahtzee_label.pack(side=LEFT)

p2bot_total_label = Button(p2_bot_frame, text="Bottom Total")
p2bot_total_label.pack(side=LEFT)

p2grand_total_label = Button(p2_bot_frame, text="Grand Total")
p2grand_total_label.pack(side=LEFT)

root.mainloop()
