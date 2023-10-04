from tkinter import *
import math, random, os
from tkinter import messagebox
import keyboard
import datetime
class Bill_App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Super Market App")
        bg_color = "#3b5998"
        date_time = datetime.datetime.now()
        date_now = date_time.strftime("%d/%m/%Y")
        time_now = date_time.strftime("%H:%M:%S")

        # Date and time
        dateTimeFrame = Frame(root)

        NowDate = Label(dateTimeFrame, text="Date: " + date_now, bg=bg_color, fg="gold",
                        font=("times new roman", 18, "bold"))
        NowDate.pack(side=RIGHT, fill=BOTH)
        NowTime = Label(dateTimeFrame, text="LogIn Time: " + time_now, bg=bg_color, fg="gold",
                        font=("times new roman", 18, "bold"))
        NowTime.pack(side=LEFT, fill=BOTH)
        title_lbl = Label(dateTimeFrame, text="SUPER MARKET", bg=bg_color, fg="white",
                          font=("times new roman", 60, "bold"))
        title_lbl.pack(fill=BOTH)
        dateTimeFrame.pack(side=TOP, fill=BOTH)
        # ============Menu Bar

        # DropDownMenuToShowcase = Menu(root)
        # self.root.configure(menu=DropDownMenuToShowcase)
        # WhatWeDo = Menu(DropDownMenuToShowcase)
        # DropDownMenuToShowcase.add_cascade(label="Check", menu=WhatWeDo)
        # DropDownMenuToShowcase.add_command(label="Calculator")
        # DropDownMenuToShowcase.add_command(label="Credits")
        # DropDownMenuToShowcase.add_command(label="Help")
        # WhatWeDo.add_command(label="Check Stock of Cosmetics")
        # WhatWeDo.add_command(label="Check Stock of Grocery")
        # WhatWeDo.add_command(label="Check Stock of Cold Drinks")

        # ============Cosmetics
        self.soap = IntVar()
        self.face_cream = IntVar()
        self.face_wash = IntVar()
        self.spray = IntVar()
        self.gell = IntVar()
        self.loshan = IntVar()
        # ============Grocery
        self.rice = IntVar()
        self.food_oil = IntVar()
        self.daal = IntVar()
        self.wheat = IntVar()
        self.sugar = IntVar()
        self.tea = IntVar()
        # ============Cold Drinks
        self.maza = IntVar()
        self.cock = IntVar()
        self.frooti = IntVar()
        self.thumbsup = IntVar()
        self.limca = IntVar()
        self.sprite = IntVar()
        # ============Total Product Price & Tax variables
        self.cosmetic_price = StringVar()
        self.grocery_price = StringVar()
        self.cold_drink_price = StringVar()
        self.cosmetic_tax = StringVar()
        self.grocery_tax = StringVar()
        self.cold_drink_tax = StringVar()
        # ============Customer
        self.c_name = StringVar()
        self.c_phon = StringVar()
        self.bill_no = StringVar()
        self.x = 1
        self.bill_no.set((datetime.datetime.now()).strftime("%d%m%H%M")+str(self.x))
        self.search_bill = StringVar()

        # ============Customer Detail Frame

        F1 = LabelFrame(self.root, relief=GROOVE, text="Customer Details", font=("times new roman", 15, "bold"),
                        fg="gold", bg=bg_color)
        F1.place(x=0, y=90, relwidth=1)

        cname_lbl = Label(F1, text="Cumtomer Name", bg=bg_color, fg="white", font=("times new roman", 15, "bold")).grid(
            row=0, column=0, padx=20, pady=5)
        cname_txt = Entry(F1, width=15, textvariable=self.c_name, font="arial 15", bd=7, relief=SUNKEN).grid(row=0,
                                                                                                             column=1,
                                                                                                             pady=5,
                                                                                                             padx=10)

        cphn_lbl = Label(F1, text="Phone No.", bg=bg_color, fg="white", font=("times new roman", 15, "bold")).grid(
            row=0, column=2, padx=20, pady=5)
        cphn_txt = Entry(F1, width=15, textvariable=self.c_phon, font="arial 15", bd=7, relief=SUNKEN).grid(row=0,
                                                                                                            column=3,
                                                                                                            pady=5,
                                                                                                            padx=10)

        c_bill_lbl = Label(F1, text="Bill Number", bg=bg_color, fg="white", font=("times new roman", 15, "bold")).grid(
            row=0, column=4, padx=20, pady=5)
        c_bill_txt = Entry(F1, width=15, textvariable=self.search_bill, font="arial 15", bd=7, relief=SUNKEN).grid(
            row=0, column=5, pady=5, padx=10)

        bill_btn = Button(F1, text="Search", command=self.find_bill, width=10, bd=7, bg="LightGray",
                          font="arial 12 bold").grid(row=0, column=6,
                                                     padx=10,
                                                     pady=10)
        bill_btn = Button(F1, text="Print", command=self.print_bill, width=10, bd=7, bg="LightGray",
                          font="arial 12 bold").grid(row=0, column=7,
                                                     padx=10,
                                                     pady=10)
        # ===============Cosmetics Frame
        F2 = LabelFrame(self.root, relief=GROOVE, text="Cosmetics", font=("times new roman", 15, "bold"), fg="gold",
                        bg=bg_color)
        F2.place(x=1, y=180, width=380, height=380)

        bath_lbl = Label(F2, text="Bath Soap", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(
            row=0, column=0, padx=10, pady=10, sticky="w")
        bath_txt = Entry(F2, width=10, textvariable=self.soap, font=("times new roman", 16, "bold"), bd=5,
                         relief=SUNKEN).grid(row=0, column=1, padx=10, pady=10)

        Face_cream_lbl = Label(F2, text="Face Cream", font=("times new roman", 16, "bold"), bg=bg_color,
                               fg="lightgreen").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        Face_cream_txt = Entry(F2, textvariable=self.face_cream, width=10, font=("times new roman", 16, "bold"), bd=5,
                               relief=SUNKEN).grid(row=1, column=1, padx=10, pady=10)

        Face_w_lbl = Label(F2, text="Face Wash", font=("times new roman", 16, "bold"), bg=bg_color,
                           fg="lightgreen").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        Face_w_txt = Entry(F2, width=10, textvariable=self.face_wash, font=("times new roman", 16, "bold"), bd=5,
                           relief=SUNKEN).grid(row=2, column=1, padx=10, pady=10)

        Hair_s_lbl = Label(F2, text="Hair Spray", font=("times new roman", 16, "bold"), bg=bg_color,
                           fg="lightgreen").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        Hair_s_txt = Entry(F2, width=10, textvariable=self.spray, font=("times new roman", 16, "bold"), bd=5,
                           relief=SUNKEN).grid(row=3, column=1, padx=10, pady=10)

        Hair_g_lbl = Label(F2, text="Hair Gel", font=("times new roman", 16, "bold"), bg=bg_color,
                           fg="lightgreen").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        Hair_g_txt = Entry(F2, width=10, textvariable=self.gell, font=("times new roman", 16, "bold"), bd=5,
                           relief=SUNKEN).grid(row=4, column=1, padx=10, pady=10)

        body_lbl = Label(F2, text="Body Lotion", font=("times new roman", 16, "bold"), bg=bg_color,
                         fg="lightgreen").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        body_txt = Entry(F2, width=10, textvariable=self.loshan, font=("times new roman", 16, "bold"), bd=5,
                         relief=SUNKEN).grid(row=5, column=1, padx=10, pady=10)

        # ===============Grocery Frame
        F3 = LabelFrame(self.root, relief=GROOVE, text="Grocery", font=("times new roman", 15, "bold"), fg="gold",
                        bg=bg_color)
        F3.place(x=338, y=180, width=380, height=380)

        g1_lbl = Label(F3, text="Rice", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=0,
                                                                                                                 column=0,
                                                                                                                 padx=10,
                                                                                                                 pady=10,
                                                                                                                 sticky="w")
        g1_txt = Entry(F3, width=10, textvariable=self.rice, font=("times new roman", 16, "bold"), bd=5,
                       relief=SUNKEN).grid(row=0, column=1, padx=10, pady=10)

        g2_lbl = Label(F3, text="Food Oil", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(
            row=1, column=0, padx=10, pady=10, sticky="w")
        g2_txt = Entry(F3, width=10, textvariable=self.food_oil, font=("times new roman", 16, "bold"), bd=5,
                       relief=SUNKEN).grid(row=1, column=1, padx=10, pady=10)

        g3_lbl = Label(F3, text="Daal", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=2,
                                                                                                                 column=0,
                                                                                                                 padx=10,
                                                                                                                 pady=10,
                                                                                                                 sticky="w")
        g3_txt = Entry(F3, width=10, textvariable=self.daal, font=("times new roman", 16, "bold"), bd=5,
                       relief=SUNKEN).grid(row=2, column=1, padx=10, pady=10)

        g4_lbl = Label(F3, text="Wheat", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=3,
                                                                                                                  column=0,
                                                                                                                  padx=10,
                                                                                                                  pady=10,
                                                                                                                  sticky="w")
        g4_txt = Entry(F3, width=10, textvariable=self.wheat, font=("times new roman", 16, "bold"), bd=5,
                       relief=SUNKEN).grid(row=3, column=1, padx=10, pady=10)

        g5_lbl = Label(F3, text="Sugar", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=4,
                                                                                                                  column=0,
                                                                                                                  padx=10,
                                                                                                                  pady=10,
                                                                                                                  sticky="w")
        g5_txt = Entry(F3, width=10, textvariable=self.sugar, font=("times new roman", 16, "bold"), bd=5,
                       relief=SUNKEN).grid(row=4, column=1, padx=10, pady=10)

        g6_lbl = Label(F3, text="Tea", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=5,
                                                                                                                column=0,
                                                                                                                padx=10,
                                                                                                                pady=10,
                                                                                                                sticky="w")
        g6_txt = Entry(F3, width=10, textvariable=self.tea, font=("times new roman", 16, "bold"), bd=5,
                       relief=SUNKEN).grid(row=5, column=1, padx=10, pady=10)

        # ===============Cold Drink Frame
        F4 = LabelFrame(self.root, relief=GROOVE, text="Cold Drinks", font=("times new roman", 15, "bold"), fg="gold",
                        bg=bg_color)
        F4.place(x=675, y=180, width=380, height=380)

        c1_lbl = Label(F4, text="Maza", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=0,
                                                                                                                 column=0,
                                                                                                                 padx=10,
                                                                                                                 pady=10,
                                                                                                                 sticky="w")
        c1_txt = Entry(F4, width=10, textvariable=self.maza, font=("times new roman", 16, "bold"), bd=5,
                       relief=SUNKEN).grid(row=0, column=1, padx=10, pady=10)

        c2_lbl = Label(F4, text="Coca-Cola", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(
            row=1, column=0, padx=10, pady=10, sticky="w")
        c2_txt = Entry(F4, width=10, textvariable=self.cock, font=("times new roman", 16, "bold"), bd=5,
                       relief=SUNKEN).grid(row=1, column=1, padx=10, pady=10)

        c3_lbl = Label(F4, text="Frooti", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(
            row=2, column=0, padx=10, pady=10, sticky="w")
        c3_txt = Entry(F4, width=10, textvariable=self.frooti, font=("times new roman", 16, "bold"), bd=5,
                       relief=SUNKEN).grid(row=2, column=1, padx=10, pady=10)

        c4_lbl = Label(F4, text="Thumbs up", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(
            row=3, column=0, padx=10, pady=10, sticky="w")
        c4_txt = Entry(F4, width=10, textvariable=self.thumbsup, font=("times new roman", 16, "bold"), bd=5,
                       relief=SUNKEN).grid(row=3, column=1, padx=10, pady=10)

        c5_lbl = Label(F4, text="Limca", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=4,
                                                                                                                  column=0,
                                                                                                                  padx=10,
                                                                                                                  pady=10,
                                                                                                                  sticky="w")
        c5_txt = Entry(F4, width=10, textvariable=self.limca, font=("times new roman", 16, "bold"), bd=5,
                       relief=SUNKEN).grid(row=4, column=1, padx=10, pady=10)

        c6_lbl = Label(F4, text="Sprite", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(
            row=5, column=0, padx=10, pady=10, sticky="w")
        c6_txt = Entry(F4, width=10, textvariable=self.sprite, font=("times new roman", 16, "bold"), bd=5,
                       relief=SUNKEN).grid(row=5, column=1, padx=10, pady=10)

        # ===============Bill Area
        F5 = Frame(self.root, bd=10, relief=GROOVE, bg="LightGray", cursor="dot")
        F5.place(x=1012, y=180, width=340, height=380)
        bill_title = Label(F5, text="Bill", font="arial 15 bold", bd=7, relief=GROOVE).pack(fill=X)
        scrol_y = Scrollbar(F5, orient=VERTICAL)
        self.txtarea = Text(F5, yscrollcommand=scrol_y.set , cursor="dot")
        scrol_y.pack(side=RIGHT, fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH, expand=1)

        # ===============Button Frame
        F6 = LabelFrame(self.root, relief=GROOVE, text="Bill Menu", font=("times new roman", 15, "bold"), fg="gold",
                        bg=bg_color)
        F6.place(x=0, y=560, relwidth=1, height=140)

        m1 = Label(F6, text="Total Cosmetics price", bg=bg_color, fg="white",
                   font=("times new roman", 14, "bold")).grid(row=0, column=0, padx=20, pady=1, sticky="w")
        m1_txt = Entry(F6, width=18, textvariable=self.cosmetic_price, font="arial 10 bold", bd=7, relief=SUNKEN).grid(
            row=0, column=1, padx=10, pady=1)

        m2 = Label(F6, text="Total Grocery price", bg=bg_color, fg="white", font=("times new roman", 14, "bold")).grid(
            row=1, column=0, padx=20, pady=1, sticky="w")
        m2_txt = Entry(F6, width=18, textvariable=self.grocery_price, font="arial 10 bold", bd=7, relief=SUNKEN).grid(
            row=1, column=1, padx=10, pady=1)

        m3 = Label(F6, text="Total Cold Drinks price", bg=bg_color, fg="white",
                   font=("times new roman", 14, "bold")).grid(row=2, column=0, padx=20, pady=1, sticky="w")
        m3_txt = Entry(F6, width=18, textvariable=self.cold_drink_price, font="arial 10 bold", bd=7,
                       relief=SUNKEN).grid(row=2, column=1, padx=10, pady=1)

        c1 = Label(F6, text="Cosmetics Tax", bg=bg_color, fg="white", font=("times new roman", 14, "bold")).grid(row=0,
                                                                                                                 column=2,
                                                                                                                 padx=20,
                                                                                                                 pady=1,
                                                                                                                 sticky="w")
        c1_txt = Entry(F6, width=18, textvariable=self.cosmetic_tax, font="arial 10 bold", bd=7, relief=SUNKEN).grid(
            row=0, column=3, padx=10, pady=1)

        c2 = Label(F6, text="Grocery Tax", bg=bg_color, fg="white", font=("times new roman", 14, "bold")).grid(row=1,
                                                                                                               column=2,
                                                                                                               padx=20,
                                                                                                               pady=1,
                                                                                                               sticky="w")
        c2_txt = Entry(F6, width=18, textvariable=self.grocery_tax, font="arial 10 bold", bd=7, relief=SUNKEN).grid(
            row=1, column=3, padx=10, pady=1)

        c3 = Label(F6, text="Cold Drinks Tax", bg=bg_color, fg="white", font=("times new roman", 14, "bold")).grid(
            row=2, column=2, padx=20, pady=1, sticky="w")
        c3_txt = Entry(F6, width=18, textvariable=self.cold_drink_tax, font="arial 10 bold", bd=7, relief=SUNKEN).grid(
            row=2, column=3, padx=10, pady=1)

        btn_F = Frame(F6, relief=GROOVE, bg=bg_color)
        btn_F.place(x=760, relwidth=1, height=140)

        total_btn = Button(btn_F, command=self.total, text="Total", bg="LightGray", fg="Black", bd=5, pady=10, width=10,
                           font="arial 15 bold").grid(row=0, column=0, padx=3, pady=5)
        GBill_btn = Button(btn_F, text="Generate Bill", command=self.bill_area, bg="LightGray", fg="Black", bd=5,
                           pady=10, width=10, font="arial 15 bold").grid(row=0, column=1, padx=3, pady=5)
        Clear_btn = Button(btn_F, text="Clear", command=self.clear_data, bg="LightGray", fg="Black", bd=5, pady=10,
                           width=10, font="arial 15 bold").grid(row=0, column=2, padx=3, pady=5)
        Exit_btn = Button(btn_F, text="Exit", command=self.Exit_App, bg="LightGray", fg="Black", bd=5, pady=10,
                          width=10, font="arial 15 bold").grid(row=0, column=3, padx=3, pady=5)

        my_lbl = Label(self.root, text="Credits:- Shreyans Mutha.", bg=bg_color, fg="darkgray",
                       font=("times new roman", 20, "bold")).place(x=1010,y=660)


        self.welcome_bill()
        keyboard.add_hotkey('enter', self.total)
    def total(self):
                
        self.c_s_p = self.soap.get() * 40
        self.c_fc_p = self.face_cream.get() * 120
        self.c_fw_p = self.face_wash.get() * 60
        self.c_hs_p = self.spray.get() * 180
        self.c_hg_p = self.gell.get() * 140
        self.c_bl_p = self.loshan.get() * 180
        self.total_cosmetic_price = float(
            self.c_s_p +
            self.c_fc_p +
            self.c_fw_p +
            self.c_hs_p +
            self.c_hg_p +
            self.c_bl_p
        )
        self.cosmetic_price.set("Rs. " + str(self.total_cosmetic_price))
        self.c_tax = round((self.total_cosmetic_price * 0.05), 2)
        self.cosmetic_tax.set("Rs. " + str(self.c_tax))

        self.g_r_p = self.rice.get() * 80
        self.g_f_p = self.food_oil.get() * 180
        self.g_d_p = self.daal.get() * 60
        self.g_w_p = self.wheat.get() * 240
        self.g_s_p = self.sugar.get() * 45
        self.g_t_p = self.tea.get() * 150
        self.total_grocery_price = float(
            self.g_r_p +
            self.g_f_p +
            self.g_d_p +
            self.g_w_p +
            self.g_s_p +
            self.g_t_p
        )
        self.grocery_price.set("Rs. " + str(self.total_grocery_price))
        self.g_tax = round((self.total_grocery_price * 0.10), 2)
        self.grocery_tax.set("Rs. " + str(self.g_tax))

        self.d_m_p = self.maza.get() * 40
        self.d_c_p = self.cock.get() * 120
        self.d_f_p = self.frooti.get() * 60
        self.d_t_p = self.thumbsup.get() * 180
        self.d_l_p = self.limca.get() * 140
        self.d_s_p = self.sprite.get() * 180
        self.total_cold_drink_price = float(
            self.d_m_p +
            self.d_c_p +
            self.d_f_p +
            self.d_t_p +
            self.d_l_p +
            self.d_s_p
        )
        self.cold_drink_price.set("Rs. " + str(self.total_cold_drink_price))
        self.d_tax = round((self.total_cold_drink_price * 0.07), 2)
        self.cold_drink_tax.set("Rs. " + str(self.d_tax))

        self.Total_bill = float(self.total_cosmetic_price +
                                self.total_grocery_price +
                                self.total_cold_drink_price +
                                self.c_tax +
                                self.g_tax +
                                self.d_tax
                                )

    def welcome_bill(self):
        self.txtarea.delete('1.0', END)
        self.txtarea.insert(END, f"\tWelcome To Super Market\t")
        self.txtarea.insert(END, f"\nDate : {(datetime.datetime.now()).strftime("%d:%m:%y")} \t\t Time : {(datetime.datetime.now()).strftime("%H:%M:%S")}")
        self.txtarea.insert(END, f"\nBill Number : {self.bill_no.get()}")
        self.txtarea.insert(END, f"\nCustomer Name : {self.c_name.get()}")
        self.txtarea.insert(END, f"\nPhone Number : {self.c_phon.get()}")
        self.txtarea.insert(END, "\n=====================================")
        self.txtarea.insert(END, "\nProducts        \t\tQTY\t\tPrice")
        self.txtarea.insert(END, "\n=====================================")

    def bill_area(self):

        if self.c_name.get() == "" or self.c_phon.get() == "":
            messagebox.showerror("Error...", "Customer Details are Must...!!!")
        elif self.cosmetic_price.get() == "Rs. 0.0" and self.grocery_price.get() == "Rs. 0.0" and self.cold_drink_price.get() == "Rs. 0.0":
            messagebox.showerror("Error...", "No Product Selected")
        elif self.cosmetic_price.get() == "" or self.grocery_price.get() == "" or self.cold_drink_price.get() == "":
            messagebox.showerror("Error...", "Calculate the Total amount First")
        else:
            self.welcome_bill()
            # ===============Cosmetics
            if self.soap.get() != 0:
                self.txtarea.insert(END, f"\nBath Soap        \t\t{self.soap.get()}\t\t{self.c_s_p}")
            if self.face_cream.get() != 0:
                self.txtarea.insert(END, f"\nFace Cream       \t\t{self.face_cream.get()}\t\t{self.c_fc_p}")
            if self.face_wash.get() != 0:
                self.txtarea.insert(END, f"\nFace Wash        \t\t{self.face_wash.get()}\t\t{self.c_fw_p}")
            if self.spray.get() != 0:
                self.txtarea.insert(END, f"\nHair Spray       \t\t{self.spray.get()}\t\t{self.c_hs_p}")
            if self.gell.get() != 0:
                self.txtarea.insert(END, f"\nHair Gel         \t\t{self.gell.get()}\t\t{self.c_hg_p}")
            if self.loshan.get() != 0:
                self.txtarea.insert(END, f"\nBody Lotion      \t\t{self.loshan.get()}\t\t{self.c_bl_p}")

            # ===============Grocery
            if self.rice.get() != 0:
                self.txtarea.insert(END, f"\nRice             \t\t{self.rice.get()}\t\t{self.g_r_p}")
            if self.food_oil.get() != 0:
                self.txtarea.insert(END, f"\nFood Oil         \t\t{self.food_oil.get()}\t\t{self.g_f_p}")
            if self.daal.get() != 0:
                self.txtarea.insert(END, f"\nDaal             \t\t{self.daal.get()}\t\t{self.g_d_p}")
            if self.wheat.get() != 0:
                self.txtarea.insert(END, f"\nWheat            \t\t{self.wheat.get()}\t\t{self.g_w_p}")
            if self.sugar.get() != 0:
                self.txtarea.insert(END, f"\nSugar            \t\t{self.sugar.get()}\t\t{self.g_s_p}")
            if self.tea.get() != 0:
                self.txtarea.insert(END, f"\nTea              \t\t{self.tea.get()}\t\t{self.g_t_p}")

            # ===============Coid Drinks
            if self.maza.get() != 0:
                self.txtarea.insert(END, f"\nMaza             \t\t{self.maza.get()}\t\t{self.d_m_p}")
            if self.cock.get() != 0:
                self.txtarea.insert(END, f"\nCoca-cola        \t\t{self.cock.get()}\t\t{self.d_c_p}")
            if self.frooti.get() != 0:
                self.txtarea.insert(END, f"\nFrooti           \t\t{self.frooti.get()}\t\t{self.d_f_p}")
            if self.thumbsup.get() != 0:
                self.txtarea.insert(END, f"\nThumbs up        \t\t{self.thumbsup.get()}\t\t{self.d_t_p}")
            if self.limca.get() != 0:
                self.txtarea.insert(END, f"\nLimca            \t\t{self.limca.get()}\t\t{self.d_l_p}")
            if self.sprite.get() != 0:
                self.txtarea.insert(END, f"\nSprite           \t\t{self.sprite.get()}\t\t{self.d_s_p}")

            self.txtarea.insert(END, "\n-------------------------------------")
            if self.cosmetic_tax.get() != "Rs. 0.0":
                self.txtarea.insert(END, f"\nCosmetic Tax          \t\t{self.cosmetic_tax.get()}")
                self.txtarea.insert(END, "\n-------------------------------------")
            if self.grocery_tax.get() != "Rs. 0.0":
                self.txtarea.insert(END, f"\nGrocery Tax           \t\t{self.grocery_tax.get()}")
                self.txtarea.insert(END, "\n-------------------------------------")
            if self.cold_drink_tax.get() != "Rs. 0.0":
                self.txtarea.insert(END, f"\nCold Drinks Tax       \t\t{self.cold_drink_tax.get()}")
                self.txtarea.insert(END, "\n=====================================")

            self.txtarea.insert(END, f"\nTotal Bill            \t\tRs. {self.Total_bill}")
            self.txtarea.insert(END, "\n_____________________________________")
            self.txtarea.insert(END, "\nThank You...Visit Again...!!!")
            self.save_bill()

    def clear_data(self):
        op = messagebox.askyesno("Clear Bill", "Do you want to Clear the Data")
        if op > 0:
            # ============Cosmetics
            self.soap.set(0)
            self.face_cream.set(0)
            self.face_wash.set(0)
            self.spray.set(0)
            self.gell.set(0)
            self.loshan.set(0)
            # ============Grocery
            self.rice.set(0)
            self.food_oil.set(0)
            self.daal.set(0)
            self.wheat.set(0)
            self.sugar.set(0)
            self.tea.set(0)
            # ============Cold Drinks
            self.maza.set(0)
            self.cock.set(0)
            self.frooti.set(0)
            self.thumbsup.set(0)
            self.limca.set(0)
            self.sprite.set(0)
            # ============Total Product Price & Tax variables
            self.cosmetic_price.set("")
            self.grocery_price.set("")
            self.cold_drink_price.set("")
            self.cosmetic_tax.set("")
            self.grocery_tax.set("")
            self.cold_drink_tax.set("")
            # ============Customer
            self.c_name.set("")
            self.c_phon.set("")
            self.bill_no.set("")
            self.bill_no.set((datetime.datetime.now()).strftime("%d%m%H%M")+str(self.x))
            self.search_bill.set("")
            self.welcome_bill()

    def save_bill(self):
        op = messagebox.askyesno("Save Bill", "Do you want to save the Bill?")
        if op > 0:
            self.bill_data = self.txtarea.get('1.0', END)
            f1 = open("bills/" + str(self.bill_no.get()) + ".txt", "w")
            f1.write(self.bill_data)
            self.x = self.x+1
            f1.close()
        else:
            return

    def Exit_App(self):
        op = messagebox.askyesno("Exit", "Do you really want to Exit?")
        if op > 0:
            self.root.destroy()

    def find_bill(self):
        present = "no"
        for i in os.listdir("bills/"):
            if i.split('.')[0] == self.search_bill.get():
                f1 = open(f"bills/{i}", "r")
                self.txtarea.delete('1.0', END)
                for d in f1:
                    self.txtarea.insert(END, d)
                f1.close()
                present = "Yes"
        if present == "no":
            messagebox.showerror("Error", "Bill Not Found")
            self.clear_data()

    def print_bill(self):
        present = "no"
        for i in os.listdir("bills/"):
            if i.split('.')[0] == self.search_bill.get():
                f1 = open(f"bills/{i}", "r")
                self.txtarea.delete('1.0', END)
                for d in f1:
                    self.txtarea.insert(END, d)
                f1.close()
                present = "Yes"
        if present == "no":
            messagebox.showerror("Error", "First Search with bill No.")
    
    


root = Tk()
root.resizable(width=False, height=False)
obj = Bill_App(root)
root.mainloop()
