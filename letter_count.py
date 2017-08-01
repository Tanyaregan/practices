import turtle

wn = turtle.Screen()
wn.bgcolor("gray")
wn.exitonclick()

turtur = turtle.Turtle()
turtur.color("red")
turtur.shape("turtle")
turtur.up()
turtur.setx(-300)
turtur.sety(-100)
turtur.down()


def letter_count(text):
    """Returns dictionary of letters(keys) with occurances(values)."""
    count = {}
    for letter in text:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1
    return count


def letter_count_summary(text):
    """returns a dict by number of occurances(keys) and letters (values)."""

    count_dict = letter_count(text)
    num_count = {}

    for letter in count_dict:
        num = count_dict[letter]
        if num not in num_count:
            num_count[num] = [letter]
        else:
            num_count[num].append(letter)
    return num_count


def letter_list(text):
    """Reads keys from letter_count dict into a list."""

    letter_dict = letter_count(text)
    letter_list = []

    for letter in letter_dict:
        letter_list.append(letter)

    return letter_list.sort()


letter_list('test text')


def turtur_lines(text, turtle, color):
    """Draws histogram of letters and their occurance for text in a specific color."""

    letter_dict = letter_count(text)
    letter_ls = letter_list(text)

    for letter in letter_ls:
        freq = int(letter_dict[letter]) * 10
        turtle.forward(freq)
        turtle.back(freq)
        turtle.right(90)
        turtle.up()
        turtle.forward(10)
        turtle.left(90)
        turtle.down()

