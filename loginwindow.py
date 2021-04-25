import tkinter as tk


def main():
    bgColor = '#FDAE6D';

    window = tk.Tk()
    window.title('Add Task')

    window.geometry('600x800')
    window.configure(bg=bgColor)
    window.grid_columnconfigure(0, weight=1, minsize=100)
    window.grid_columnconfigure(1, weight=1, minsize=100)
    window.grid_columnconfigure(2, weight=1, minsize=100)
    window.grid_columnconfigure(3, weight=1, minsize=100)

    headLabel = tk.Label(master=window, text='Add Task', font='None 20', bg=bgColor)
    headLabel.grid(row=0, columnspan=4, sticky=tk.W+tk.E, pady=(10,0))

    textName = tk.Label(master=window, text='Name:', font='None 18', anchor=tk.W, bg=bgColor)
    textName.grid(row=1, columnspan=4, sticky=tk.W, padx=80)

    inputName = tk.Entry(master=window)
    inputName.grid(row=2, columnspan=4, sticky=tk.W+tk.E, padx=80)

    labelDate = tk.Label(master=window, text='Day / Month', font='None 16', bg=bgColor)
    labelDate.grid(row=3, columnspan=4, sticky=tk.W + tk.E)

    select1 = tk.Spinbox(master=window, from_=0, to=31, width=10)
    select1.grid(row=4, column=1, padx=5, pady=5, sticky=tk.E)

    select2 = tk.Spinbox(master=window, from_=0, to=12, width=10)
    select2.grid(row=4, column=2, padx=5, pady=5, sticky=tk.W)

    labelTime = tk.Label(master=window, text='Time', font='None 16', bg=bgColor)
    labelTime.grid(row=5, columnspan=4, sticky=tk.W+tk.E)

    select3 = tk.Spinbox(master=window, from_=0, to=24, width=10)
    select3.grid(row=6, column=1, padx=5, pady=5, sticky=tk.E)

    select4 = tk.Spinbox(master=window, from_=0, to=60, width=10)
    select4.grid(row=6, column=2, padx=5, sticky=tk.W)

    textHeaderColor = tk.Label(master=window, text='Color swatch', font='None 14', anchor=tk.W, bg=bgColor)
    textHeaderColor.grid(row=7, column=0, sticky=tk.W, padx=10)

    textColorLine1 = tk.Label(master=window, text='User can choose to use color. The selected color represents', font='None 14', bg=bgColor)
    textColorLine1.grid(row=8, padx=(10, 0), columnspan=4, sticky=tk.W)

    textColorLine2 = tk.Label(master=window, text='the amount of time User spends each job. As follows', font='None 14', bg=bgColor)
    textColorLine2.grid(row=9, padx=(10, 0), columnspan=4, sticky=tk.W)

    textColorLine3 = tk.Label(master=window, text='Red : It takes approximately more than 3 days.', font='None 14', bg=bgColor)
    textColorLine3.grid(row=10, padx=(40, 0), columnspan=4, sticky=tk.W)

    textColorLine4 = tk.Label(master=window, text='Orange : 24 hours or less.', font='None 14', bg=bgColor)
    textColorLine4.grid(row=11, padx=(40, 0), columnspan=4, sticky=tk.W)

    textColorLine5 = tk.Label(master=window, text='Green : 1-5 hours', font='None 14', bg=bgColor)
    textColorLine5.grid(row=12, padx=(40, 0), columnspan=4, sticky=tk.W)

    colorBoxRed = tk.Frame(master=window, width=100, height=70, bg='red')
    colorBoxRed.grid(row=13, column=0, padx=5, pady=5)

    colorBoxOrange = tk.Frame(master=window, width=100, height=70, bg='orange')
    colorBoxOrange.grid(row=13, column=1, padx=5, pady=5)

    colorBoxGreen = tk.Frame(master=window, width=100, height=70, bg='green')
    colorBoxGreen.grid(row=13, column=2, padx=5, pady=5)

    radioButtonFrame = tk.Frame(master=window, bg=bgColor)

    radio = tk.StringVar(None, 1)

    radioButtonRed = tk.Radiobutton(master=radioButtonFrame, text='Red', variable=radio, value=1, bg=bgColor)
    radioButtonRed.grid(row=0, column=0, sticky=tk.W)

    radioButtonOrange = tk.Radiobutton(master=radioButtonFrame, text='Orange', variable=radio, value=2, bg=bgColor)
    radioButtonOrange.grid(row=1, column=0, sticky=tk.W)

    radioButtonGreen = tk.Radiobutton(master=radioButtonFrame, text='Green', variable=radio, value=3, bg=bgColor)
    radioButtonGreen.grid(row=2, column=0, sticky=tk.W)

    radioButtonFrame.grid(row=13, column=3, sticky=tk.W)

    buttonFrame = tk.Frame(master=window, bg='red')

    submitButton = tk.Button(master=buttonFrame, text='Submit')
    submitButton.grid(row=0, column=0, sticky=tk.W+tk.E)

    buttonFrame.grid(row=14, column=0, columnspan=4, pady=20)

    window.mainloop()


if __name__ == '__main__':
    main()
