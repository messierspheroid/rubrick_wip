from tkinter import *


class FormApp(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title('Form Tutorial in TKinter')
        self.geometry('600x500')
        container = Frame(self)
        self.frames = {
            'login': UserLogin(self),
            'registration': UserRegistration(self)
        }

        self.show_login_frame()
        container.config(bg='#f1f1f1')
        container.pack(fill=BOTH, expand=True, padx=20, pady=20)

    def show_frame(self, name):
        frame = self.frames[name]
        frame.config(borderwidth=2, relief="groove", bg='#f1f1f1')
        frame.place(width=500, height=400, relx=0.5, rely=0.5, anchor=CENTER)
        frame.tkraise()

    def show_sign_up_frame(self):
        self.show_frame('registration')

    def show_login_frame(self):
        self.show_frame('login')


class UserLogin(Frame):
    def __init__(self, form):
        Frame.__init__(self, form)

        frame = Frame(self, bg='#f1f1f1')
        Label(frame, text='User Login Form', font=('Arial Bold', 20), pady=20, bg='#f1f1f1')\
            .grid(row=0, column=0, columnspan=2)

        Label(frame, text='Username', bg='#f1f1f1').grid(row=1, column=0)
        Entry(frame).grid(row=1, column=1)

        Label(frame, text='Password', bg='#f1f1f1').grid(row=2, column=0)
        Entry(frame).grid(row=2, column=1)

        self.check_var = IntVar()
        Checkbutton(frame, text='I agree to terms & conditions',
                    variable=self.check_var, bg='#f1f1f1',
                    command=self.check_status)\
            .grid(row=3, column=0, columnspan=2, sticky=W)

        self.login_btn = Button(frame, text='Login !', state=DISABLED)
        self.login_btn.grid(row=4, column=0, sticky=W)

        Button(frame, text='New User ! Sign me up',
               command=form.show_sign_up_frame)\
            .grid(row=4, column=1, sticky=W)

        frame.place(relx=0.5, rely=0.5, anchor=CENTER)

    def check_status(self):
        print(self.check_var.get())
        if self.check_var.get() == 1:
            self.login_btn.config(state=NORMAL)
        elif self.check_var.get() == 0:
            self.login_btn.config(state=DISABLED)


class UserRegistration(Frame):
    def __init__(self, form):
        Frame.__init__(self, form)

        frame = Frame(self, bg='#f1f1f1')

        Label(frame, text='User Registration Form', font=('Arial Bold', 20), pady=20, bg='#f1f1f1')\
            .grid(row=0, column=0, columnspan=2)

        Label(frame, text='First Name', bg='#f1f1f1').grid(row=1, column=0)
        Entry(frame).grid(row=1, column=1)

        Label(frame, text='Last Name', bg='#f1f1f1').grid(row=2, column=0)
        Entry(frame).grid(row=2, column=1)

        Label(frame, text='Gender', bg='#f1f1f1')\
            .grid(row=3, column=0, pady=(5, 10))
        choices = {'Male', 'Female'}
        tk_var = StringVar(frame)
        tk_var.set('Male')
        OptionMenu(frame, tk_var, *choices) \
            .grid(row=3, column=1, pady=(5, 10), sticky=W)

        Button(frame, text='Sign Up !') \
            .grid(row=4, column=0, sticky=W)

        Button(frame, text='Already User ! Back to Login',
               command=form.show_login_frame) \
            .grid(row=4, column=1, sticky=W)

        frame.place(relx=0.5, rely=0.5, anchor=CENTER)


if __name__ == "__main__":
    app = FormApp()
    app.mainloop()
