from domains.Room import *
from tkinter import *
from tkinter import ttk
from tk import *
import utils

def clear_entry(entry_frame, rid_entry, type_entry, price_entry, status_entry):
    # Delete all Warnings
    Label(entry_frame, bg='#5E95FF', fg='crimson', text='                                  ', font=("Times New Roman", 14, 'bold')).grid(column=6,row=0,sticky='w')
    Label(entry_frame, bg='#5E95FF', fg='crimson', text='                   ', font=("Times New Roman", 14, 'bold')).grid(column=6,row=1,sticky='w')
    Label(entry_frame, bg='#5E95FF', fg='crimson', text='                   ', font=("Times New Roman", 14, 'bold')).grid(column=6,row=2,sticky='w')
    Label(entry_frame, bg='#5E95FF', fg='crimson', text='                   ', font=("Times New Roman", 14, 'bold')).grid(column=6,row=3,sticky='w')

    # Empty Entry boxes
    rid_entry.delete(0, END)
    type_entry.delete(0, END)
    price_entry.delete(0, END)
    status_entry.delete(0, END)

   
    # Set selected_room to -1
    global selected_room
    selected_room = -1
    
def room_add(room_list, room_tree, entry_frame, rid_entry, type_entry, price_entry, status_entry):
    Label(entry_frame, bg='#5E95FF', fg='crimson', text='                                  ', font=("Times New Roman", 14, 'bold')).grid(column=6,row=0,sticky='w')
    Label(entry_frame, bg='#5E95FF', fg='crimson', text='                   ', font=("Times New Roman", 14, 'bold')).grid(column=6,row=1,sticky='w')
    Label(entry_frame, bg='#5E95FF', fg='crimson', text='                   ', font=("Times New Roman", 14, 'bold')).grid(column=6,row=2,sticky='w')
    Label(entry_frame, bg='#5E95FF', fg='crimson', text='                   ', font=("Times New Roman", 14, 'bold')).grid(column=6,row=3,sticky='w')

    rid = rid_entry.get()
    type = type_entry.get()
    price = price_entry.get()
    status = status_entry.get()

    # Validation
    valid_check = 0
    
    #Validate ID
    if len(rid) == 0:
        Label(entry_frame, bg='#5E95FF', fg='crimson', text='EMPTY', font=("Times New Roman", 14, 'bold')).grid(column=6,row=0,sticky='w')
        valid_check += 1
    elif utils.invalid_id(rid, "R-") == 1:
        Label(entry_frame, bg='#5E95FF', fg='crimson', text='INVALID', font=("Times New Roman", 14, 'bold')).grid(column=6,row=0,sticky='w')
        valid_check += 1
    else:
        for room in room_list:
            if room.get_rid() == rid:
                Label(entry_frame, bg='#5E95FF', fg='crimson', text='ID already exist', font=("Times New Roman", 14, 'bold')).grid(column=6,row=0,sticky='w')
                valid_check += 1
                break

    # Validate Type
    if len(type) == 0:
        Label(entry_frame, bg='#5E95FF', fg='crimson', text='EMPTY', font=("Times New Roman", 14, 'bold')).grid(column=6,row=1,sticky='w')
        valid_check += 1
    elif utils.invalid_type(type) == 1:
        Label(entry_frame, bg='#5E95FF', fg='crimson', text='INVALID', font=("Times New Roman", 14, 'bold')).grid(column=6,row=1,sticky='w')
        valid_check += 1

    # Validate Price
    if len(price) == 0:
        Label(entry_frame, bg='#5E95FF', fg='crimson', text='EMPTY', font=("Times New Roman", 14, 'bold')).grid(column=6,row=2,sticky='w')
        valid_check += 1
    elif utils.invalid_price(price, type) == 1:
        Label(entry_frame, bg='#5E95FF', fg='crimson', text='INVALID', font=("Times New Roman", 14, 'bold')).grid(column=6,row=2,sticky='w')
        valid_check += 1
        
    # Validate Status
    if len(status) == 0:
        Label(entry_frame, bg='#5E95FF', fg='crimson', text='EMPTY', font=("Times New Roman", 14, 'bold')).grid(column=6,row=3,sticky='w')
        valid_check += 1
    elif utils.invalid_status(status) == 1:
        Label(entry_frame, bg='#5E95FF', fg='crimson', text='INVALID', font=("Times New Roman", 14, 'bold')).grid(column=6,row=3,sticky='w')
        valid_check += 1
        
    # If All Valid
    if valid_check == 0:
        # Add to room_list
        new_room = Room(rid, type, price, status)
        room_list.append(new_room)

        # Display on Treeview
        room_tree.insert(parent='', index = 'end', iid=rid, text='', values=(rid, type, price, status))

        # Empty Entry boxes
        rid_entry.delete(0, END)
        type_entry.delete(0, END)
        price_entry.delete(0, END)
        status_entry.delete(0, END)


def room_remove(room_list, room_tree):
    if len(room_tree.selection())>0:
        selected_room = room_tree.selection()[0]
        room_rid = room_tree.item(selected_room, 'values')[0]

        for room in room_list:
            if room.get_rid()== room_rid:
                room_list.remove(room)
                break
        room_tree.delete(selected_room)

def all_room_remove(room_tree, room_list):
    for room in room_tree.get_children():
        room_tree.delete(room)
    room_list.clear()

def room_select(room_list, room_tree, entry_frame, rid_entry, type_entry, price_entry, status_entry):
    # Delete all Warnings
    Label(entry_frame, bg='#5E95FF', fg='crimson', text='                                  ', font=("Times New Roman", 14, 'bold')).grid(column=6,row=0,sticky='w')
    Label(entry_frame, bg='#5E95FF', fg='crimson', text='                   ', font=("Times New Roman", 14, 'bold')).grid(column=6,row=1,sticky='w')
    Label(entry_frame, bg='#5E95FF', fg='crimson', text='                   ', font=("Times New Roman", 14, 'bold')).grid(column=6,row=2,sticky='w')
    Label(entry_frame, bg='#5E95FF', fg='crimson', text='                   ', font=("Times New Roman", 14, 'bold')).grid(column=6,row=3,sticky='w')
    
    # Empty Entry boxes
    rid_entry.delete(0, END)
    type_entry.delete(0, END)
    price_entry.delete(0, END)
    status_entry.delete(0, END)

    # Show Selected room Info
    if len(room_tree.selection())>0:
        global selected_room
        selected_room = room_tree.selection()[0]
        room_rid = room_tree.item(selected_room, 'values')[0]
        for room in room_list:
            if room.get_rid()== room_rid:
                rid_entry.insert(0, room.get_rid())
                type_entry.insert(0, room.get_type())
                price_entry.insert(0, room.get_price())
                status_entry.insert(0, room.get_status())
                break

def room_update(room_list, room_tree, entry_frame, rid_entry, type_entry, price_entry, status_entry):
    global selected_room
    if selected_room != -1:
        Label(entry_frame, bg='#5E95FF', fg='crimson', text='                                  ', font=("Times New Roman", 14, 'bold')).grid(column=6,row=0,sticky='w')
        Label(entry_frame, bg='#5E95FF', fg='crimson', text='                   ', font=("Times New Roman", 14, 'bold')).grid(column=6,row=1,sticky='w')
        Label(entry_frame, bg='#5E95FF', fg='crimson', text='                   ', font=("Times New Roman", 14, 'bold')).grid(column=6,row=2,sticky='w')
        Label(entry_frame, bg='#5E95FF', fg='crimson', text='                   ', font=("Times New Roman", 14, 'bold')).grid(column=6,row=3,sticky='w')
        
        rid = rid_entry.get()
        type = type_entry.get()
        price = price_entry.get()
        status = status_entry.get()

        # Validation
        valid_check = 0
        
        #Validate ID
        if len(rid) == 0:
            Label(entry_frame, bg='#5E95FF', fg='crimson', text='EMPTY', font=("Times New Roman", 14, 'bold')).grid(column=6,row=0,sticky='w')
            valid_check += 1
        elif utils.invalid_id(rid, "R-") == 1:
            Label(entry_frame, bg='#5E95FF', fg='crimson', text='INVALID', font=("Times New Roman", 14, 'bold')).grid(column=6,row=0,sticky='w')
            valid_check += 1
        else:
            # check if new id is different from old id, if yes, check for duplication
            if rid != room_tree.item(selected_room, 'values')[0]:
                for room in room_list:
                    if room.get_rid() == rid:
                        Label(entry_frame, bg='#5E95FF', fg='crimson', text='ID already exist', font=("Times New Roman", 14, 'bold')).grid(column=6,row=0,sticky='w')
                        valid_check += 1
                        break
        # Validate Type
        if len(type) == 0:
            Label(entry_frame, bg='#5E95FF', fg='crimson', text='EMPTY', font=("Times New Roman", 14, 'bold')).grid(column=6,row=1,sticky='w')
            valid_check += 1
        elif utils.invalid_type(type) == 1:
            Label(entry_frame, bg='#5E95FF', fg='crimson', text='INVALID', font=("Times New Roman", 14, 'bold')).grid(column=6,row=1,sticky='w')
            valid_check += 1

        # Validate Price
        if len(price) == 0:
            Label(entry_frame, bg='#5E95FF', fg='crimson', text='EMPTY', font=("Times New Roman", 14, 'bold')).grid(column=6,row=2,sticky='w')
            valid_check += 1
        elif utils.invalid_price(price, type) == 1:
            Label(entry_frame, bg='#5E95FF', fg='crimson', text='INVALID', font=("Times New Roman", 14, 'bold')).grid(column=6,row=2,sticky='w')
            valid_check += 1
        
        # Validate Status
        if len(status) == 0:
            Label(entry_frame, bg='#5E95FF', fg='crimson', text='EMPTY', font=("Times New Roman", 14, 'bold')).grid(column=6,row=3,sticky='w')
            valid_check += 1
        elif utils.invalid_status(status) == 1:
            Label(entry_frame, bg='#5E95FF', fg='crimson', text='INVALID', font=("Times New Roman", 14, 'bold')).grid(column=6,row=3,sticky='w')
            valid_check += 1
        
        # If All Valid
        if valid_check == 0:
            for room in room_list:
                if room.get_rid() == room_tree.item(selected_room, 'values')[0]:
                    room.set_rid(rid)
                    room.set_type(type)
                    room.set_price(price)
                    room.set_status(status)
                    break
            
            room_tree.item(selected_room, text="", values = (rid, type, price, status))
            selected_room = -1
        
            rid_entry.delete(0, END)
            type_entry.delete(0, END)
            price_entry.delete(0, END)
            status_entry.delete(0, END)

def room_press(window, width, height, room_list):
    global selected_room
    selected_room = -1
    room_subwin = Toplevel(window)
    room_subwin.title("Room Information")
    room_subwin.geometry("%dx%d+0+0" % (width, height))

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
    room_tree = ttk.Treeview(room_subwin, selectmode='browse', show='headings')

    # Define columns
    room_tree['columns'] = ("ID", "Type", "Price", "Status")

    # Format columns
    room_tree.column("#0", width=0, stretch=NO)
    room_tree.column("ID", anchor='center', width=75)
    room_tree.column("Type",anchor='w', width=100)
    room_tree.column("Price",anchor='center', width=80)
    room_tree.column("Status",anchor='center', width=150)

    # Create Headings
    room_tree.heading("#0", text="")
    room_tree.heading("ID", text="ID", anchor='center', command= lambda: utils.sort_room_list_by_column(room_tree, room_list, "ID", False))
    room_tree.heading("Type", text="Type", anchor='center', command= lambda: utils.sort_room_list_by_column(room_tree, room_list, "Type", False))
    room_tree.heading("Price", text="Price", anchor='center', command= lambda: utils.sort_room_list_by_column(room_tree, room_list, "Price", False))
    room_tree.heading("Status", text="Status", anchor='center', command= lambda: utils.sort_room_list_by_column(room_tree, room_list, "Status", False))

    room_tree.bind('<Motion>', 'break')
    
    # Insert Data
    for room in room_list:
        room_tree.insert(parent='', index = 'end', iid=room.get_rid(), text='', values=(room.get_rid(), room.get_type(), room.get_price(), room.get_status()))
        
    room_tree.place(x=width/2+50, y=50, height=height-250, width=width/2-100)


    #=========================================================================================
    
    # room Control
    Label(room_subwin, bg='#5E95FF', fg='white', text='ROOMS MANAGEMENT', font=("Times New Roman", 20, 'bold')).place(x=50, y=25, width=width/2-100, height=50)
    #Frame(room_subwin, bg='crimson').place(x=50, y=85, width=width/2-100, height=2)
    entry_frame = Frame(room_subwin, bg='#5E95FF')
    entry_frame.place(x=50, y=100, width=width/2-100, height=height/2)
    #Frame(room_subwin, bg='crimson').place(x=50, y=350, width=width/2-100, height=2)
    Label(room_subwin, text='  - ID must be " R-xxx " ', anchor='w', bg='#5E95FF', fg='white', font=("Times New Roman", 12, 'bold')).place(x=50, y=380, height=30)
    Label(room_subwin, text='  - Type must be " Normal " or " Gold " or " Luxury "', anchor='w', bg='#5E95FF', fg='white', font=("Times New Roman", 12, 'bold')).place(x=50, y=410, height=30)
    Label(room_subwin, text='  - Price must be " 1000000 " or " 2000000 " or " 3000000 " based on type', anchor='w', bg='#5E95FF', fg='white', font=("Times New Roman", 12, 'bold')).place(x=50, y=440, height=30)
    Label(room_subwin, text='  - Status must be " Avai " or " Unavai "', anchor='w', bg='#5E95FF', fg='white', font=("Times New Roman", 12, 'bold')).place(x=50, y=470, height=30)

    # Column 0: Atribute
    Label(entry_frame, bg='#5E95FF', fg='white', text=' - ID - ', font=("Times New Roman", 14, 'bold')).grid(column=0, row=0)
    Label(entry_frame, bg='#5E95FF', fg='white', text=' - Type - ', font=("Times New Roman", 14, 'bold')).grid(column=0, row=1)
    Label(entry_frame, bg='#5E95FF', fg='white', text=' - Price - ', font=("Times New Roman", 14, 'bold')).grid(column=0, row=2)
    Label(entry_frame, bg='#5E95FF', fg='white', text=' - Status - ', font=("Times New Roman", 14, 'bold')).grid(column=0, row=3)


    # Column 2: |
    Label(entry_frame, bg='#5E95FF', fg='white', text=' | ', font=("Times New Roman", 14, 'bold')).grid(column=3, row=0)
    Label(entry_frame, bg='#5E95FF', fg='white', text=' | ', font=("Times New Roman", 14, 'bold')).grid(column=3, row=1)
    Label(entry_frame, bg='#5E95FF', fg='white', text=' | ', font=("Times New Roman", 14, 'bold')).grid(column=3, row=2)
    Label(entry_frame, bg='#5E95FF', fg='white', text=' | ', font=("Times New Roman", 14, 'bold')).grid(column=3, row=3)
    
    # Column 3: Entries
    rid_entry = Entry(entry_frame)
    rid_entry.grid(column=4,row=0)

    type_entry = Entry(entry_frame)
    type_entry.grid(column=4,row=1)

    price_entry = Entry(entry_frame)
    price_entry.grid(column=4,row=2)

    status_entry = Entry(entry_frame)
    status_entry.grid(column=4,row=3)
    
    # Column 5: |
    Label(entry_frame, bg='#5E95FF', fg='white', text=' | ', font=("Times New Roman", 14, 'bold')).grid(column=5, row=0)
    Label(entry_frame, bg='#5E95FF', fg='white', text=' | ', font=("Times New Roman", 14, 'bold')).grid(column=5, row=1)
    Label(entry_frame, bg='#5E95FF', fg='white', text=' | ', font=("Times New Roman", 14, 'bold')).grid(column=5, row=2)
    Label(entry_frame, bg='#5E95FF', fg='white', text=' | ', font=("Times New Roman", 14, 'bold')).grid(column=5, row=3)

    # Buttons
    add_room_button = Button(room_subwin, text='ADD ROOM',anchor='center',font=("Times New Roman", 12,'bold'), fg='#5E95FF', relief='ridge',
        activebackground='dark blue', activeforeground='white', command=lambda: room_add(room_list, room_tree, entry_frame, rid_entry, type_entry, price_entry, status_entry))
    add_room_button.place(x=50, y=height-75-85-10-50, width=150, height=50)

    update_room_button = Button(room_subwin, text='UPDATE',anchor='center',font=("Times New Roman", 12,'bold'), fg='#5E95FF', relief='ridge',
        activebackground='dark blue', activeforeground='white', command=lambda: room_update(room_list, room_tree, entry_frame, rid_entry, type_entry, price_entry, status_entry))
    update_room_button.place(x=width/2-50-150, y=height-75-85-10-50, width=150, height=50)

    clear_button = Button(room_subwin, text='CLEAR',anchor='center',font=("Times New Roman", 12,'bold'), fg='red', relief='ridge',
        activebackground='dark blue', activeforeground='white', command=lambda: clear_entry(entry_frame, rid_entry, type_entry, price_entry, status_entry))
    clear_button.place(x=width/4*1-100, y=height-75-85-10-50, width=200, height=50)

    remove_room_button = Button(room_subwin, text='REMOVE SELECTED',anchor='center',font=("Times New Roman", 12,'bold'),bg='red', fg='white', relief='ridge',
        activebackground='crimson', activeforeground='white', command=lambda: room_remove(room_list, room_tree))
    remove_room_button.place(x=width/4*3-100, y=height-75-85, width=200, height=50)

    remove_all_room_button = Button(room_subwin, text='REMOVE ALL',anchor='center',font=("Times New Roman", 12,'bold'),bg='red', fg='white', relief='ridge',
        activebackground='crimson', activeforeground='white', command=lambda: all_room_remove(room_tree, room_list))
    remove_all_room_button.place(x=width-50-150, y=height-75-85, width=150, height=50)

    select_room_button = Button(room_subwin, text='SELECT',anchor='center',font=("Times New Roman", 12,'bold'), bg='#5E95FF',fg='white', relief='ridge',
        activebackground='dark blue', activeforeground='white', command=lambda: room_select(room_list, room_tree, entry_frame, rid_entry, type_entry, price_entry, status_entry))
    select_room_button.place(x=width/2+50, y=height-75-85, width=150, height=50)
