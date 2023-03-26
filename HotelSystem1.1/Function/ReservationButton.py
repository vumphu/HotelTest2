from domains.Reservation import *
from domains.Room import *
from domains.Person import *
from tkinter import *
from tkinter import ttk
from tk import *
import utils

def clear_entry(entry_frame, no_entry, rid_entry, gid_entry, checkin_entry, checkout_entry, paymentdate_entry, creditcard_entry, billing_entry):
    # Delete all Warnings
    Label(entry_frame, bg='#5E95FF', fg='crimson', text='                                  ', font=("Times New Roman", 14, 'bold')).grid(column=6,row=0,sticky='w')
    Label(entry_frame, bg='#5E95FF', fg='crimson', text='                   ', font=("Times New Roman", 14, 'bold')).grid(column=6,row=1,sticky='w')
    Label(entry_frame, bg='#5E95FF', fg='crimson', text='                   ', font=("Times New Roman", 14, 'bold')).grid(column=6,row=2,sticky='w')
    Label(entry_frame, bg='#5E95FF', fg='crimson', text='                   ', font=("Times New Roman", 14, 'bold')).grid(column=6,row=3,sticky='w')
    Label(entry_frame, bg='#5E95FF', fg='crimson', text='                   ', font=("Times New Roman", 14, 'bold')).grid(column=6,row=4,sticky='w')
    Label(entry_frame, bg='#5E95FF', fg='crimson', text='                   ', font=("Times New Roman", 14, 'bold')).grid(column=6,row=5,sticky='w')
    Label(entry_frame, bg='#5E95FF', fg='crimson', text='                   ', font=("Times New Roman", 14, 'bold')).grid(column=6,row=6,sticky='w')
    Label(entry_frame, bg='#5E95FF', fg='crimson', text='                   ', font=("Times New Roman", 14, 'bold')).grid(column=6,row=7,sticky='w')

    # Empty Entry boxes
    no_entry.delete(0, END)
    rid_entry.delete(0, END)
    gid_entry.delete(0, END)
    checkin_entry.delete(0, END)
    checkout_entry.delete(0, END)
    paymentdate_entry.delete(0, END)
    creditcard_entry.delete(0, END)
    billing_entry.delete(0, END)
   
    # Set selected_reservation to -1
    global selected_reservation
    selected_reservation= -1
    """global selected_room
    selected_room= -1
    global selected_guest
    selected_guest= -1"""
    
def reservation_add(reservation_list, room_list, guest_list, reservation_tree, entry_frame, no_entry, rid_entry, gid_entry, checkin_entry, checkout_entry, paymentdate_entry, creditcard_entry, billing_entry):
    Label(entry_frame, bg='#5E95FF', fg='crimson', text='                                  ', font=("Times New Roman", 14, 'bold')).grid(column=6,row=0,sticky='w')
    Label(entry_frame, bg='#5E95FF', fg='crimson', text='                                  ', font=("Times New Roman", 14, 'bold')).grid(column=6,row=1,sticky='w')
    Label(entry_frame, bg='#5E95FF', fg='crimson', text='                                  ', font=("Times New Roman", 14, 'bold')).grid(column=6,row=2,sticky='w')
    Label(entry_frame, bg='#5E95FF', fg='crimson', text='                   ', font=("Times New Roman", 14, 'bold')).grid(column=6,row=3,sticky='w')
    Label(entry_frame, bg='#5E95FF', fg='crimson', text='                   ', font=("Times New Roman", 14, 'bold')).grid(column=6,row=4,sticky='w')
    Label(entry_frame, bg='#5E95FF', fg='crimson', text='                   ', font=("Times New Roman", 14, 'bold')).grid(column=6,row=5,sticky='w')
    Label(entry_frame, bg='#5E95FF', fg='crimson', text='                   ', font=("Times New Roman", 14, 'bold')).grid(column=6,row=6,sticky='w')
    Label(entry_frame, bg='#5E95FF', fg='crimson', text='                   ', font=("Times New Roman", 14, 'bold')).grid(column=6,row=7,sticky='w')

    no = no_entry.get()
    rid = rid_entry.get()
    gid = gid_entry.get()
    checkin = checkin_entry.get()
    checkout = checkout_entry.get()
    paymentdate = paymentdate_entry.get()
    creditcard = creditcard_entry.get()
    billing = billing_entry.get()

    # Validation
    valid_check = 0
    
    #Validate No
    if len(no) == 0:
        Label(entry_frame, bg='#5E95FF', fg='crimson', text='EMPTY', font=("Times New Roman", 14, 'bold')).grid(column=6,row=0,sticky='w')
        valid_check += 1
    elif utils.invalid_no(no) == 1:
        Label(entry_frame, bg='#5E95FF', fg='crimson', text='INVALID', font=("Times New Roman", 14, 'bold')).grid(column=6,row=0,sticky='w')
        valid_check += 1
    else:
        for reservation in reservation_list:
            if reservation.get_no() == no:
                Label(entry_frame, bg='#5E95FF', fg='crimson', text='No already exist', font=("Times New Roman", 14, 'bold')).grid(column=6,row=0,sticky='w')
                valid_check += 1
                break
    
    # Validate Room ID
    if len(rid) == 0:
        Label(entry_frame, bg='#5E95FF', fg='crimson', text='EMPTY', font=("Times New Roman", 14, 'bold')).grid(column=6,row=1,sticky='w')
        valid_check += 1
    elif utils.invalid_id(rid, "R-") == 1:
        Label(entry_frame, bg='#5E95FF', fg='crimson', text='INVALID', font=("Times New Roman", 14, 'bold')).grid(column=6,row=1,sticky='w')
        valid_check += 1
    else:
    # check if new id is different from old id, if yes, check for duplication
            for room in room_list:
                if room.get_rid() == rid:
                    break
            else:
                    Label(entry_frame, bg='#5E95FF', fg='crimson', text='Room not exist', font=("Times New Roman", 14, 'bold')).grid(column=6,row=1,sticky='w')
                    valid_check += 1

    # Validate Guest ID 
    if len(gid) == 0:
        Label(entry_frame, bg='#5E95FF', fg='crimson', text='EMPTY', font=("Times New Roman", 14, 'bold')).grid(column=6,row=2,sticky='w')
        valid_check += 1
    elif utils.invalid_id(gid, "G-") == 1:
        Label(entry_frame, bg='#5E95FF', fg='crimson', text='INVALID', font=("Times New Roman", 14, 'bold')).grid(column=6,row=2,sticky='w')
        valid_check += 1
    else:
    # check if new id is different from old id, if yes, check for duplication
            for guest in guest_list:
                if guest.get_gid() == gid:
                    break
            else:
                    Label(entry_frame, bg='#5E95FF', fg='crimson', text='Guest not exist', font=("Times New Roman", 14, 'bold')).grid(column=6,row=2,sticky='w')
                    valid_check += 1

    # Validate Checkin
    if len(checkin) == 0:
        Label(entry_frame, bg='#5E95FF', fg='crimson', text='EMPTY', font=("Times New Roman", 14, 'bold')).grid(column=6,row=3,sticky='w')
        valid_check += 1
    elif utils.invalid_dob(checkin) == 1:
        Label(entry_frame, bg='#5E95FF', fg='crimson', text='INVALID', font=("Times New Roman", 14, 'bold')).grid(column=6,row=3,sticky='w')
        valid_check += 1
            
    # Validate Checkout
    if len(checkout) == 0:
        Label(entry_frame, bg='#5E95FF', fg='crimson', text='EMPTY', font=("Times New Roman", 14, 'bold')).grid(column=6,row=4,sticky='w')
        valid_check += 1
    elif utils.invalid_dob(checkout) == 1:
        Label(entry_frame, bg='#5E95FF', fg='crimson', text='INVALID', font=("Times New Roman", 14, 'bold')).grid(column=6,row=4,sticky='w')
        valid_check += 1
        
    # Validate paymentdate
    if len(paymentdate) == 0:
        Label(entry_frame, bg='#5E95FF', fg='crimson', text='EMPTY', font=("Times New Roman", 14, 'bold')).grid(column=6,row=5,sticky='w')
        valid_check += 1
    elif utils.invalid_dob(paymentdate) == 1:
        Label(entry_frame, bg='#5E95FF', fg='crimson', text='INVALID', font=("Times New Roman", 14, 'bold')).grid(column=6,row=5,sticky='w')
        valid_check += 1
        
    # Validation Billing
    if len(billing) == 0:
        Label(entry_frame, bg='#5E95FF', fg='crimson', text='EMPTY', font=("Times New Roman", 14, 'bold')).grid(column=6,row=7,sticky='w')
        valid_check += 1
        
    # If All Valid
    if valid_check == 0:
        # Add to guest_list
        new_reservation= Reservation(no, rid, gid, checkin, checkout,paymentdate ,creditcard , billing)
        reservation_list.append(new_reservation)

        # Display on Treeview
        reservation_tree.insert(parent='', index = 'end', iid=no, text='', values=(no, rid, gid, checkin, checkout))

        # Empty Entry boxes
        no_entry.delete(0, END)
        rid_entry.delete(0, END)
        gid_entry.delete(0, END)
        checkin_entry.delete(0, END)
        checkout_entry.delete(0, END)
        paymentdate_entry.delete(0, END)
        creditcard_entry.delete(0, END)
        billing_entry.delete(0, END)

def reservation_remove(reservation_list, reservation_tree):
    if len(reservation_tree.selection())>0:
        selected_reservation= reservation_tree.selection()[0]
        reservation_no = reservation_tree.item(selected_reservation, 'values')[0]

        for reservation in reservation_list:
            if reservation.get_no()== reservation_no:
                reservation_list.remove(reservation)
                break
        reservation_tree.delete(selected_reservation)

def all_reservation_remove(reservation_tree, reservation_list):
    for reservation in reservation_tree.get_children():
        reservation_tree.delete(reservation)
    reservation_list.clear()

def reservation_select(reservation_list, room_list, guest_list, reservation_tree, entry_frame, no_entry, rid_entry, gid_entry, checkin_entry, checkout_entry, paymentdate_entry, creditcard_entry, billing_entry):
    # Delete all Warnings
    Label(entry_frame, bg='#5E95FF', fg='crimson', text='                                  ', font=("Times New Roman", 14, 'bold')).grid(column=6,row=0,sticky='w')
    Label(entry_frame, bg='#5E95FF', fg='crimson', text='                                  ', font=("Times New Roman", 14, 'bold')).grid(column=6,row=1,sticky='w')
    Label(entry_frame, bg='#5E95FF', fg='crimson', text='                                  ', font=("Times New Roman", 14, 'bold')).grid(column=6,row=2,sticky='w')
    Label(entry_frame, bg='#5E95FF', fg='crimson', text='                   ', font=("Times New Roman", 14, 'bold')).grid(column=6,row=3,sticky='w')
    Label(entry_frame, bg='#5E95FF', fg='crimson', text='                   ', font=("Times New Roman", 14, 'bold')).grid(column=6,row=4,sticky='w')
    Label(entry_frame, bg='#5E95FF', fg='crimson', text='                   ', font=("Times New Roman", 14, 'bold')).grid(column=6,row=5,sticky='w')
    Label(entry_frame, bg='#5E95FF', fg='crimson', text='                   ', font=("Times New Roman", 14, 'bold')).grid(column=6,row=6,sticky='w')
    Label(entry_frame, bg='#5E95FF', fg='crimson', text='                   ', font=("Times New Roman", 14, 'bold')).grid(column=6,row=7,sticky='w')
    
    # Empty Entry boxes
    no_entry.delete(0, END)
    rid_entry.delete(0, END)
    gid_entry.delete(0, END)
    checkin_entry.delete(0, END)
    checkout_entry.delete(0, END)
    paymentdate_entry.delete(0, END)
    creditcard_entry.delete(0, END)
    billing_entry.delete(0, END)

    # Show Selected reservationInfo
    if len(reservation_tree.selection())>0:
        global selected_reservation
        selected_reservation= reservation_tree.selection()[0]
        reservation_no = reservation_tree.item(selected_reservation, 'values')[0]
        for reservation in reservation_list:
                 if reservation.get_no()== reservation_no:
                  no_entry.insert(0, reservation.get_no())
                  rid_entry.insert(0, reservation.get_rid())
                  gid_entry.insert(0, reservation.get_gid())
                  checkin_entry.insert(0, reservation.get_checkin())
                  checkout_entry.insert(0, reservation.get_checkout())
                  paymentdate_entry.insert(0, reservation.get_paymentdate())
                  creditcard_entry.insert(0, reservation.get_creditcard())
                  billing_entry.insert(0, reservation.get_billing())
                  break

def reservation_update(reservation_list, reservation_tree, guest_list, room_list, entry_frame, no_entry, rid_entry, gid_entry, checkin_entry, checkout_entry, paymentdate_entry, creditcard_entry, billing_entry):
 global selected_reservation
 if selected_reservation!= -1:
    #if selected_guest!= -1:
     #if selected_room!= -1:
        
        Label(entry_frame, bg='#5E95FF', fg='crimson', text='                                  ', font=("Times New Roman", 14, 'bold')).grid(column=6,row=0,sticky='w')
        Label(entry_frame, bg='#5E95FF', fg='crimson', text='                                  ', font=("Times New Roman", 14, 'bold')).grid(column=6,row=1,sticky='w')
        Label(entry_frame, bg='#5E95FF', fg='crimson', text='                                  ', font=("Times New Roman", 14, 'bold')).grid(column=6,row=2,sticky='w')
        Label(entry_frame, bg='#5E95FF', fg='crimson', text='                   ', font=("Times New Roman", 14, 'bold')).grid(column=6,row=3,sticky='w')
        Label(entry_frame, bg='#5E95FF', fg='crimson', text='                   ', font=("Times New Roman", 14, 'bold')).grid(column=6,row=4,sticky='w')
        Label(entry_frame, bg='#5E95FF', fg='crimson', text='                   ', font=("Times New Roman", 14, 'bold')).grid(column=6,row=5,sticky='w')
        Label(entry_frame, bg='#5E95FF', fg='crimson', text='                   ', font=("Times New Roman", 14, 'bold')).grid(column=6,row=6,sticky='w')
        Label(entry_frame, bg='#5E95FF', fg='crimson', text='                   ', font=("Times New Roman", 14, 'bold')).grid(column=6,row=7,sticky='w')
        
        no = no_entry.get()
        rid = rid_entry.get()
        gid = gid_entry.get()
        checkin = checkin_entry.get()
        checkout = checkout_entry.get()
        paymentdate = paymentdate_entry.get()
        creditcard = creditcard_entry.get()
        billing = billing_entry.get()

        # Validation
        valid_check = 0
        
        #Validate No
        if len(no) == 0:
            Label(entry_frame, bg='#5E95FF', fg='crimson', text='EMPTY', font=("Times New Roman", 14, 'bold')).grid(column=6,row=0,sticky='w')
            valid_check += 1
        elif utils.invalid_no(no) == 1:
            Label(entry_frame, bg='#5E95FF', fg='crimson', text='INVALID', font=("Times New Roman", 14, 'bold')).grid(column=6,row=0,sticky='w')
            valid_check += 1
        else:
            # check if new id is different from old id, if yes, check for duplication
            if no != reservation_tree.item(selected_reservation, 'values')[0]:
                for reservation in reservation_list:
                    if reservation.get_no() == no:
                        Label(entry_frame, bg='#5E95FF', fg='crimson', text='ID already exist', font=("Times New Roman", 14, 'bold')).grid(column=6,row=0,sticky='w')
                        valid_check += 1
                        break
        
        # Validate Room ID
        if len(rid) == 0:
            Label(entry_frame, bg='#5E95FF', fg='crimson', text='EMPTY', font=("Times New Roman", 14, 'bold')).grid(column=6,row=1,sticky='w')
            valid_check += 1
        elif utils.invalid_id(id, "R-") == 1:
            Label(entry_frame, bg='#5E95FF', fg='crimson', text='INVALID', font=("Times New Roman", 14, 'bold')).grid(column=6,row=1,sticky='w')
            valid_check += 1
        else:
        # check if new id is different from old id, if yes, check for duplication
            if rid != reservation_tree.item(selected_reservation, 'values')[1]:
                for room in room_list:
                    if room.get_rid() == rid:
                        break
            else:
                    Label(entry_frame, bg='#5E95FF', fg='crimson', text='Room not exist', font=("Times New Roman", 14, 'bold')).grid(column=6,row=1,sticky='w')
                    valid_check += 1
        # Validate Guest ID 
        if len(gid) == 0:
            Label(entry_frame, bg='#5E95FF', fg='crimson', text='EMPTY', font=("Times New Roman", 14, 'bold')).grid(column=6,row=2,sticky='w')
            valid_check += 1
        elif utils.invalid_id(id, "G-") == 1:
            Label(entry_frame, bg='#5E95FF', fg='crimson', text='INVALID', font=("Times New Roman", 14, 'bold')).grid(column=6,row=2,sticky='w')
            valid_check += 1
        else:
        # check if new id is different from old id, if yes, check for duplication
            if gid != reservation_tree.item(selected_reservation, 'values')[2]:
                for guest in guest_list:
                    if guest.get_gid() == gid:
                        break
            else:
                    Label(entry_frame, bg='#5E95FF', fg='crimson', text='Guest not exist', font=("Times New Roman", 14, 'bold')).grid(column=6,row=2,sticky='w')
                    valid_check += 1

        # Validate Checkin
        if len(checkin) == 0:
            Label(entry_frame, bg='#5E95FF', fg='crimson', text='EMPTY', font=("Times New Roman", 14, 'bold')).grid(column=6,row=3,sticky='w')
            valid_check += 1
        elif utils.invalid_dob(checkin) == 1:
            Label(entry_frame, bg='#5E95FF', fg='crimson', text='INVALID', font=("Times New Roman", 14, 'bold')).grid(column=6,row=3,sticky='w')
            valid_check += 1
            
        # Validate Checkout
        if len(checkout) == 0:
            Label(entry_frame, bg='#5E95FF', fg='crimson', text='EMPTY', font=("Times New Roman", 14, 'bold')).grid(column=6,row=4,sticky='w')
            valid_check += 1
        elif utils.invalid_dob(checkout) == 1:
            Label(entry_frame, bg='#5E95FF', fg='crimson', text='INVALID', font=("Times New Roman", 14, 'bold')).grid(column=6,row=4,sticky='w')
            valid_check += 1
        
        # Validate paymentdate
        if len(paymentdate) == 0:
            Label(entry_frame, bg='#5E95FF', fg='crimson', text='EMPTY', font=("Times New Roman", 14, 'bold')).grid(column=6,row=5,sticky='w')
            valid_check += 1
        elif utils.invalid_dob(paymentdate) == 1:
            Label(entry_frame, bg='#5E95FF', fg='crimson', text='INVALID', font=("Times New Roman", 14, 'bold')).grid(column=6,row=5,sticky='w')
            valid_check += 1
        
        # Validation Billing
        if len(billing) == 0:
            Label(entry_frame, bg='#5E95FF', fg='crimson', text='EMPTY', font=("Times New Roman", 14, 'bold')).grid(column=6,row=7,sticky='w')
            valid_check += 1
        
        # If All Valid
        if valid_check == 0:
            for reservation in reservation_list:
                        if reservation.get_no() == reservation_tree.item(selected_reservation, 'values')[0]:
                            reservation.set_no(no)
                            reservation.set_rid(rid)
                            reservation.set_gid(gid)
                            reservation.set_checkin(checkin)
                            reservation.set_checkout(checkout)
                            reservation.set_paymentdate(paymentdate)
                            reservation.set_creditcard(creditcard)
                            reservation.set_billing(billing)
                            break
            
            reservation_tree.item(selected_reservation, text="", values = (no, rid, gid, checkin, checkout, paymentdate, creditcard, billing))
            selected_reservation= -1
        
            no_entry.delete(0, END)
            rid_entry.delete(0, END)
            gid_entry.delete(0, END)
            checkin_entry.delete(0, END)
            checkout_entry.delete(0, END)
            paymentdate_entry.delete(0, END)
            creditcard_entry.delete(0, END)
            billing_entry.delete(0, END)

def reservation_press(window, width, height, reservation_list, guest_list, room_list):
    global selected_reservation
    selected_reservation= -1
    reservation_subwin = Toplevel(window)
    reservation_subwin.title("reservationInformation")
    reservation_subwin.geometry("%dx%d+0+0" % (width, height))

    #=====================================================================================
    style = ttk.Style()
    style.theme_use('clam')
    style.configure("Treeview",
        background = "silver",
        foreground = "black",
        rowheight = 25,
        font=("Times New Roman", 12),
        fieldbackground = "silver"
        )
    style.configure("Treeview.Heading", font=("Times New Roman", 16,'bold'))
    
    style.map('Treeview', background=[('selected', 'dark blue')])

    # Create TreeView List
    reservation_tree = ttk.Treeview(reservation_subwin, selectmode='browse', show='headings')

    # Define columns
    reservation_tree['columns'] = ("No", "Room ID", "Guest ID", "Check In", "Check Out")

    # Format columns
    reservation_tree.column("#0", width=0, stretch=NO)
    reservation_tree.column("No", anchor='center', width=75)
    reservation_tree.column("Room ID",anchor='w', width=100)
    reservation_tree.column("Guest ID",anchor='center', width=100)
    reservation_tree.column("Check In",anchor='center', width=150)
    reservation_tree.column("Check Out",anchor='center', width=150)

    # Create Headings
    reservation_tree.heading("#0", text="")
    reservation_tree.heading("No", text="No", anchor='center', command= lambda: utils.sort_reservation_list_by_column(reservation_tree, reservation_list, "No", False))
    reservation_tree.heading("Room ID", text="Room ID", anchor='center', command= lambda: utils.sort_reservation_list_by_column(reservation_tree, reservation_list, "Room ID", False))
    reservation_tree.heading("Guest ID", text="Guest ID", anchor='center', command= lambda: utils.sort_reservation_list_by_column(reservation_tree, reservation_list, "Guest ID", False))
    reservation_tree.heading("Check In", text="Check In", anchor='center', command= lambda: utils.sort_reservation_list_by_column(reservation_tree, reservation_list, "Check In", False))
    reservation_tree.heading("Check Out", text="Check Out", anchor='center', command= lambda: utils.sort_reservation_list_by_column(reservation_tree, reservation_list, "Check Out", False))

    reservation_tree.bind('<Motion>', 'break')
    
    # Insert Data
    for reservation in reservation_list:
        reservation_tree.insert(parent='', index = 'end', iid=reservation.get_no(), text='', values=(reservation.get_no(), reservation.get_rid(), reservation.get_gid(), reservation.get_checkin(), reservation.get_checkout()))
        
    reservation_tree.place(x=width/2+50, y=50, height=height-250, width=width/2-100)


    #=========================================================================================
    
    # reservationControl
    Label(reservation_subwin, bg='#5E95FF', fg='white', text='RESERVATIONS MANAGEMENT', font=("Times New Roman", 20, 'bold')).place(x=50, y=25, width=width/2-100, height=50)
    #Frame(reservation_subwin, bg='crimson').place(x=50, y=85, width=width/2-100, height=2)
    entry_frame = Frame(reservation_subwin, bg='#5E95FF')
    entry_frame.place(x=50, y=100, width=width/2-100, height=height/2)
    #Frame(reservation_subwin, bg='crimson').place(x=50, y=350, width=width/2-100, height=2)
    Label(reservation_subwin, text='  - No must be number ', anchor='w', bg='#5E95FF', fg='white', font=("Times New Roman", 12, 'bold')).place(x=50, y=380, height=30)
    Label(reservation_subwin, text='  - Room ID must be " R-xxx " ', anchor='w', bg='#5E95FF', fg='white', font=("Times New Roman", 12, 'bold')).place(x=50, y=410, height=30)
    Label(reservation_subwin, text='  - Duest must be " G-xxx " ', anchor='w', bg='#5E95FF', fg='white', font=("Times New Roman", 12, 'bold')).place(x=50, y=440, height=30)
    Label(reservation_subwin, text='  - Check in/out must be " dd/mm/yyyy " ', anchor='w', bg='#5E95FF', fg='white', font=("Times New Roman", 12, 'bold')).place(x=50, y=470, height=30)


    # Column 0:  * 
    Label(entry_frame, bg='#5E95FF', fg='red', text=' * ', font=("Times New Roman", 14, 'bold')).grid(column=0, row=0)
    Label(entry_frame, bg='#5E95FF', fg='red', text=' * ', font=("Times New Roman", 14, 'bold')).grid(column=0, row=1)
    Label(entry_frame, bg='#5E95FF', fg='red', text=' * ', font=("Times New Roman", 14, 'bold')).grid(column=0, row=2)
    Label(entry_frame, bg='#5E95FF', fg='red', text=' * ', font=("Times New Roman", 14, 'bold')).grid(column=0, row=3)
    Label(entry_frame, bg='#5E95FF', fg='red', text=' * ', font=("Times New Roman", 14, 'bold')).grid(column=0, row=4)
    Label(entry_frame, bg='#5E95FF', fg='red', text=' * ', font=("Times New Roman", 14, 'bold')).grid(column=0, row=5)
    Label(entry_frame, bg='#5E95FF', fg='red', text=' * ', font=("Times New Roman", 14, 'bold')).grid(column=0, row=7)
    
    # Column 1: |
    Label(entry_frame, bg='#5E95FF', fg='white', text=' | ', font=("Times New Roman", 14, 'bold')).grid(column=1, row=0)
    Label(entry_frame, bg='#5E95FF', fg='white', text=' | ', font=("Times New Roman", 14, 'bold')).grid(column=1, row=1)
    Label(entry_frame, bg='#5E95FF', fg='white', text=' | ', font=("Times New Roman", 14, 'bold')).grid(column=1, row=2)
    Label(entry_frame, bg='#5E95FF', fg='white', text=' | ', font=("Times New Roman", 14, 'bold')).grid(column=1, row=3)
    Label(entry_frame, bg='#5E95FF', fg='white', text=' | ', font=("Times New Roman", 14, 'bold')).grid(column=1, row=4)
    Label(entry_frame, bg='#5E95FF', fg='white', text=' | ', font=("Times New Roman", 14, 'bold')).grid(column=1, row=5)
    Label(entry_frame, bg='#5E95FF', fg='white', text=' | ', font=("Times New Roman", 14, 'bold')).grid(column=1, row=6)
    Label(entry_frame, bg='#5E95FF', fg='white', text=' | ', font=("Times New Roman", 14, 'bold')).grid(column=1, row=7)


    # Column 2: Atribute
    Label(entry_frame, bg='#5E95FF', fg='white', text=' - No - ', font=("Times New Roman", 14, 'bold')).grid(column=2, row=0)
    Label(entry_frame, bg='#5E95FF', fg='white', text=' - Room ID - ', font=("Times New Roman", 14, 'bold')).grid(column=2, row=1)
    Label(entry_frame, bg='#5E95FF', fg='white', text=' - Guest ID - ', font=("Times New Roman", 14, 'bold')).grid(column=2, row=2)
    Label(entry_frame, bg='#5E95FF', fg='white', text=' - Check In- ', font=("Times New Roman", 14, 'bold')).grid(column=2, row=3)
    Label(entry_frame, bg='#5E95FF', fg='white', text=' - Check Out - ', font=("Times New Roman", 14, 'bold')).grid(column=2, row=4)
    Label(entry_frame, bg='#5E95FF', fg='white', text=' - Payment Date - ', font=("Times New Roman", 14, 'bold')).grid(column=2, row=5)
    Label(entry_frame, bg='#5E95FF', fg='white', text=' - Credit Card - ', font=("Times New Roman", 14, 'bold')).grid(column=2, row=6)
    Label(entry_frame, bg='#5E95FF', fg='white', text=' - Billing - ', font=("Times New Roman", 14, 'bold')).grid(column=2, row=7)

    # Column 3: |
    Label(entry_frame, bg='#5E95FF', fg='white', text=' | ', font=("Times New Roman", 14, 'bold')).grid(column=3, row=0)
    Label(entry_frame, bg='#5E95FF', fg='white', text=' | ', font=("Times New Roman", 14, 'bold')).grid(column=3, row=1)
    Label(entry_frame, bg='#5E95FF', fg='white', text=' | ', font=("Times New Roman", 14, 'bold')).grid(column=3, row=2)
    Label(entry_frame, bg='#5E95FF', fg='white', text=' | ', font=("Times New Roman", 14, 'bold')).grid(column=3, row=3)
    Label(entry_frame, bg='#5E95FF', fg='white', text=' | ', font=("Times New Roman", 14, 'bold')).grid(column=3, row=4)
    Label(entry_frame, bg='#5E95FF', fg='white', text=' | ', font=("Times New Roman", 14, 'bold')).grid(column=3, row=5)
    Label(entry_frame, bg='#5E95FF', fg='white', text=' | ', font=("Times New Roman", 14, 'bold')).grid(column=3, row=6)
    Label(entry_frame, bg='#5E95FF', fg='white', text=' | ', font=("Times New Roman", 14, 'bold')).grid(column=3, row=7)

    
    # Column 4: Entries
    no_entry = Entry(entry_frame)
    no_entry.grid(column=4,row=0)

    rid_entry = Entry(entry_frame)
    rid_entry.grid(column=4,row=1)

    gid_entry = Entry(entry_frame)
    gid_entry.grid(column=4,row=2)

    checkin_entry = Entry(entry_frame)
    checkin_entry.grid(column=4,row=3)
    
    checkout_entry = Entry(entry_frame)
    checkout_entry.grid(column=4,row=4)

    paymentdate_entry = Entry(entry_frame)
    paymentdate_entry.grid(column=4,row=5)

    creditcard_entry = Entry(entry_frame)
    creditcard_entry.grid(column=4,row=6)
    
    billing_entry = Entry(entry_frame)
    billing_entry.grid(column=4,row=7)

    # Column 5: |
    Label(entry_frame, bg='#5E95FF', fg='white', text=' | ', font=("Times New Roman", 14, 'bold')).grid(column=5, row=0)
    Label(entry_frame, bg='#5E95FF', fg='white', text=' | ', font=("Times New Roman", 14, 'bold')).grid(column=5, row=1)
    Label(entry_frame, bg='#5E95FF', fg='white', text=' | ', font=("Times New Roman", 14, 'bold')).grid(column=5, row=2)
    Label(entry_frame, bg='#5E95FF', fg='white', text=' | ', font=("Times New Roman", 14, 'bold')).grid(column=5, row=3)
    Label(entry_frame, bg='#5E95FF', fg='white', text=' | ', font=("Times New Roman", 14, 'bold')).grid(column=5, row=4)
    Label(entry_frame, bg='#5E95FF', fg='white', text=' | ', font=("Times New Roman", 14, 'bold')).grid(column=5, row=5)
    Label(entry_frame, bg='#5E95FF', fg='white', text=' | ', font=("Times New Roman", 14, 'bold')).grid(column=5, row=6)
    Label(entry_frame, bg='#5E95FF', fg='white', text=' | ', font=("Times New Roman", 14, 'bold')).grid(column=5, row=7)

    # Buttons
    add_reservation_button = Button(reservation_subwin, text='ADD RESERVATION',anchor='center',font=("Times New Roman", 12,'bold'), fg='#5E95FF', relief='ridge',
        activebackground='dark blue', activeforeground='white', command=lambda: reservation_add(reservation_list, room_list, guest_list, reservation_tree, entry_frame, no_entry, rid_entry, gid_entry, checkin_entry, checkout_entry, paymentdate_entry, creditcard_entry, billing_entry))
    add_reservation_button.place(x=50, y=height-75-85-10-50, width=150, height=50)

    update_reservation_button = Button(reservation_subwin, text='UPDATE',anchor='center',font=("Times New Roman", 12,'bold'), fg='#5E95FF', relief='ridge',
        activebackground='dark blue', activeforeground='white', command=lambda: reservation_update(reservation_list, guest_list, room_list , reservation_tree, entry_frame, no_entry, rid_entry, gid_entry, checkin_entry, checkout_entry, paymentdate_entry, creditcard_entry, billing_entry))
    update_reservation_button.place(x=width/2-50-150, y=height-75-85-10-50, width=150, height=50)

    clear_button = Button(reservation_subwin, text='CLEAR',anchor='center',font=("Times New Roman", 12,'bold'), fg='red', relief='ridge',
        activebackground='dark blue', activeforeground='white', command=lambda: clear_entry(entry_frame, no_entry, rid_entry, gid_entry, checkin_entry, checkout_entry, paymentdate_entry, creditcard_entry, billing_entry))
    clear_button.place(x=width/4*1-100, y=height-75-85-10-50, width=200, height=50)

    remove_reservation_button = Button(reservation_subwin, text='REMOVE SELECTED',anchor='center',font=("Times New Roman", 12,'bold'),bg='red', fg='white', relief='ridge',
        activebackground='crimson', activeforeground='white', command=lambda: reservation_remove(reservation_list, reservation_tree))
    remove_reservation_button.place(x=width/4*3-100, y=height-75-85, width=200, height=50)

    remove_all_reservation_button = Button(reservation_subwin, text='REMOVE ALL',anchor='center',font=("Times New Roman", 12,'bold'),bg='red', fg='white', relief='ridge',
        activebackground='crimson', activeforeground='white', command=lambda: all_reservation_remove(reservation_tree, reservation_list))
    remove_all_reservation_button.place(x=width-50-150, y=height-75-85, width=150, height=50)

    select_reservation_button = Button(reservation_subwin, text='SELECT',anchor='center',font=("Times New Roman", 12,'bold'), bg='#5E95FF',fg='white', relief='ridge',
        activebackground='dark blue', activeforeground='white', command=lambda: reservation_select(reservation_list, guest_list, room_list, reservation_tree, entry_frame, no_entry, rid_entry, gid_entry, checkin_entry, checkout_entry, paymentdate_entry, creditcard_entry, billing_entry))
    select_reservation_button.place(x=width/2+50, y=height-75-85, width=150, height=50)