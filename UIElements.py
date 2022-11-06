from tkinter import Label

def ConstructUIElements(root, bg_color, txt_color):
    # Some constants
    TITLE_SIZE = 12
    TITLE_Y = 0.4

    BTN_SIZE = 10
    BTN_Y = 0.58

    FONT = 'Arial'

    # Title text
    T_title = Label(root, text = "Controller Shortcuts")
    T_title.config(font =(FONT, 24, 'bold'), bg=bg_color, fg=txt_color)

    T_title.place(relx=0.5, rely=0.18, anchor='center')

    labels = [
        {
            'title_text': 'Previous Song',
            'btn_text':   'LSB + RSB\nLB',
            'x_pos':       0.2
        },
        {
            'title_text': 'Pause Song',
            'btn_text':   'LB + RB\nStart',
            'x_pos':       0.515
        },
        {
            'title_text': 'Next Song',
            'btn_text':   'LSB + RSB\nRB',
            'x_pos':       0.8
        }
    ]

    for label in labels:
        title = Label(root, text = label['title_text'])
        title.config(font =(FONT, TITLE_SIZE, 'bold'), bg=bg_color, fg=txt_color)
        
        btn_txt = Label(root, text = label['btn_text'])
        btn_txt.config(font =(FONT, BTN_SIZE), bg=bg_color, fg=txt_color)

        title.place(relx=label['x_pos'], rely=TITLE_Y, anchor='center')
        btn_txt.place(relx=label['x_pos'], rely=BTN_Y, anchor='center')