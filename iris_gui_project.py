import tkinter
from tkinter import Label, Entry, Button
from tkinter import messagebox
import numpy as np
from sklearn import cross_validation, neighbors
import pandas as pd


class iris_flower():
    def rules(self):
        a = """Attribute      Domain
           -- -----------------------------------------
           1. Sepal Length  : cm
           2. Sepal Width   : cm
           3. Petal Length  : cm
           4. Petal Width   : cm
           5. Class         : Setosa | Veginica | Versicolor
         """
        messagebox.showinfo("Guidelines for parameters are as follows:-",a)

    def quit_window(self):
        if messagebox.askokcancel("Quit", "You want to quit now? "):
            root.destroy()

    def actionPerformed(self):

        if ( self.T1.get() == '' or self.T2.get() == '' or self.T3.get() == '' or self.T4.get() == ''):
            messagebox.showerror("error", "Fill All The Fields")

        elif (float(self.T1.get()) > 10 or float(self.T2.get()) > 10 or float(self.T3.get()) > 10 or float(
                self.T4.get()) > 10 ):
            messagebox.showerror("error", "Values should be in range")

        else:
            patient_measures = np.array(
                [self.T1.get(), self.T2.get(), self.T3.get(), self.T4.get()])
            patient_measures = patient_measures.reshape(1, -1)
            prediction = clf.predict(patient_measures)
            print(prediction)

            if (prediction == 'Iris-setosa'):
                self.panel1 = Label(root, bg='red', width=30, height=10)
                self.panel2 = Label(root, text="setosa", font=('arial', 10, 'bold'), width=10, height=1)
                self.panel1.place(x=350, y=390)
                self.panel2.place(x=420, y=550)


            elif (prediction == 'Iris-versicolor'):
                self.panel = Label(root, bg='green', width=30, height=10)
                self.panel2 = Label(root, text="Iris-versicolor", font=('arial', 10, 'bold'), width=7, height=1)
                self.panel.place(x=350, y=390)
                self.panel2.place(x=420, y=550)

            else:
                self.panel = Label(root, bg='yellow', width=30, height=10)
                self.panel2 = Label(root, text="Iris-verginica", font=('arial', 10, 'bold'), width=7, height=1)
                self.panel.place(x=350, y=390)
                self.panel2.place(x=420, y=550)


    def __init__(self, root):

        self.label = Label(root, text='IRIS DATASET', font=('arial', 30, 'bold'), bg='AZURE',fg='black')
        self.label.pack()

        self.label_1 = Label(root, text='SepalLengthCm :',bg="lightseagreen", font=('arial', 10, 'bold'), fg='black')
        self.label_1.place(x=30, y=90)

        self.T1 = Entry(root, textvariable='t1', bd=2)
        self.T1.place(x=180, y=90)

        self.label_1 = Label(root, text='SepalWidthCm :',bg="lightseagreen", font=('arial', 10, 'bold'), fg='black')
        self.label_1.place(x=30, y=140)

        self.T2 = Entry(root, textvariable='t2', bd=2)
        self.T2.place(x=180, y=140)

        self.label_1 = Label(root, text='PetalLengthCm :',bg="lightseagreen", font=('arial', 10, 'bold'), fg='black')
        self.label_1.place(x=30, y=190)

        self.T3 = Entry(root, textvariable='t3', bd=2)
        self.T3.place(x=180, y=190)

        self.label_1 = Label(root, text='PetalWidthCm :',bg="lightseagreen", font=('arial', 10, 'bold'), fg='black')
        self.label_1.place(x=30, y=240)

        self.T4 = Entry(root, textvariable='t4', bd=2)
        self.T4.place(x=180, y=240)


        self.button1 = Button(root, width=6, text='ENTER',bg="AZURE", command=self.actionPerformed, font=('arial', 12), bd=3)
        self.button1.place(x=450, y=200)

        self.button2 = Button(root, width=6, text='QUIT',bg="AZURE", command=self.quit_window, font=('arial', 12), bd=3)
        self.button2.place(x=450, y=300)

        acc_button = Button(root, text="RULES", bg="AZURE", font=('arial', 10), command=self.rules,bd=3)
        acc_button.place(x=450, y=70)

        root.mainloop()


df = pd.read_csv('iris.csv')
df.drop(['Id'], 1, inplace=True)

X = np.array(df.drop(['Species'], 1))
y = np.array(df['Species'])
X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.2)
clf = neighbors.KNeighborsClassifier()
clf.fit(X_train, y_train)
accuracy = clf.score(X_test, y_test)
print(accuracy)


def print_acc():
    accuracy2 = float(accuracy)
    panel_acc = Label(root, text=float(accuracy2),bg="AZURE", font=('arial', 10, 'bold'), width=20, height=2)
    panel_acc.place(x=180, y=350)


root = tkinter.Tk()
root.title("Classification")
path1 = ("py.ico")
root.iconbitmap(path1)
root.minsize(600,600)
root.config(bg="lightseagreen")
acc_button = Button(root, text="CHECK ACCURACY",bg="AZURE", font=('arial', 10), command=print_acc)
acc_button.place(x=30, y=350)

m = iris_flower(root)
root.mainloop()
