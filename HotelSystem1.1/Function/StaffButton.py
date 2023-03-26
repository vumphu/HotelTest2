from domains.Person import *
from tkinter import *
from tkinter import ttk
from tk import *
import utils

def clear_entry(entry_frame, gid_entry, name_entry, gend_entry, dob_entry, phone_entry, email_entry, address_entry, salary_entry, position_entry):
    # Delete all Warnings
    Label(entry_frame, bg='#5E95FF', fg='crimson', text='                                  ', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=0,sticky='w')
    Label(entry_frame, bg='#5E95FF', fg='crimson', text='                   ', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=1,sticky='w')
    Label(entry_frame, bg='#5E95FF', fg='crimson', text='                   ', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=2,sticky='w')
    Label(entry_frame, bg='#5E95FF', fg='crimson', text='                   ', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=3,sticky='w')
    Label(entry_frame, bg='#5E95FF', fg='crimson', text='                   ', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=4,sticky='w')
    Label(entry_frame, bg='#5E95FF', fg='crimson', text='                   ', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=5,sticky='w')
    Label(entry_frame, bg='#5E95FF', fg='crimson', text='                   ', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=6,sticky='w')
    Label(entry_frame, bg='#5E95FF', fg='crimson', text='                   ', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=7,sticky='w')
    Label(entry_frame, bg='#5E95FF', fg='crimson', text='                   ', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=8,sticky='w')
    
    # Empty Entry boxes
    gid_entry.delete(0, END)
    name_entry.delete(0, END)
    gend_entry.delete(0, END)
    dob_entry.delete(0, END)
    phone_entry.delete(0, END)
    email_entry.delete(0, END)
    address_entry.delete(0, END)
    salary_entry.delete(0, END)
    position_entry.delete(0, END)
    
    
   
    # Set selected_staff to -1
    global selected_staff
    selected_staff = -1
    
def staff_add(staff_list, staff_tree, entry_frame, gid_entry, name_entry, gend_entry, dob_entry, phone_entry, email_entry, address_entry, salary_entry, position_entry):
    Label(entry_frame, bg='#5E95FF', fg='crimson', text='                                  ', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=0,sticky='w')
    Label(entry_frame, bg='#5E95FF', fg='crimson', text='                   ', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=1,sticky='w')
    Label(entry_frame, bg='#5E95FF', fg='crimson', text='                   ', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=2,sticky='w')
    Label(entry_frame, bg='#5E95FF', fg='crimson', text='                   ', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=3,sticky='w')
    Label(entry_frame, bg='#5E95FF', fg='crimson', text='                   ', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=4,sticky='w')
    Label(entry_frame, bg='#5E95FF', fg='crimson', text='                   ', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=5,sticky='w')
    Label(entry_frame, bg='#5E95FF', fg='crimson', text='                   ', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=6,sticky='w')
    Label(entry_frame, bg='#5E95FF', fg='crimson', text='                   ', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=7,sticky='w')
    Label(entry_frame, bg='#5E95FF', fg='crimson', text='                   ', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=8,sticky='w')

    gid = gid_entry.get()
    name = name_entry.get()
    gend = gend_entry.get()
    dob = dob_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()
    salary = salary_entry.get()
    position = position_entry.get()

    # Validation
    valid_check = 0
    
    #Validate ID
    if len(gid) == 0:
        Label(entry_frame, bg='#5E95FF', fg='crimson', text='EMPTY', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=0,sticky='w')
        valid_check += 1
    elif utils.invalid_id(gid, "S-") == 1:
        Label(entry_frame, bg='#5E95FF', fg='crimson', text='INVALID', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=0,sticky='w')
        valid_check += 1
    else:
        for staff in staff_list:
            if staff.get_gid() == gid:
                Label(entry_frame, bg='#5E95FF', fg='crimson', text='ID already exist', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=0,sticky='w')
                valid_check += 1
                break
    
    # Validate Name
    if len(name) == 0:
        Label(entry_frame, bg='#5E95FF', fg='crimson', text='EMPTY', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=1,sticky='w')
        valid_check += 1

    # Validate Gender
    if len(gend) == 0:
        Label(entry_frame, bg='#5E95FF', fg='crimson', text='EMPTY', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=2,sticky='w')
        valid_check += 1
    elif utils.invalid_gend(gend) == 1:
        Label(entry_frame, bg='#5E95FF', fg='crimson', text='INVALID', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=2,sticky='w')
        valid_check += 1

    # Validate Date of Birth
    if len(dob) == 0:
        Label(entry_frame, bg='#5E95FF', fg='crimson', text='EMPTY', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=3,sticky='w')
        valid_check += 1
    elif utils.invalid_dob(dob) == 1:
        Label(entry_frame, bg='#5E95FF', fg='crimson', text='INVALID', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=3,sticky='w')
        valid_check += 1
        
    # Validate Phone
    if len(phone) == 0:
        Label(entry_frame, bg='#5E95FF', fg='crimson', text='EMPTY', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=4,sticky='w')
        valid_check += 1
    elif utils.invalid_phone(phone) == 1:
        Label(entry_frame, bg='#5E95FF', fg='crimson', text='INVALID', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=4,sticky='w')
        valid_check += 1
        
    # Validate Email
    if len(email) == 0:
        Label(entry_frame, bg='#5E95FF', fg='crimson', text='EMPTY', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=5,sticky='w')
        valid_check += 1
        
    # Validate Address
    if len(address) == 0:
        Label(entry_frame, bg='#5E95FF', fg='crimson', text='EMPTY', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=6,sticky='w')
        valid_check += 1
        
    # Validate Salary
    if len(salary) == 0:
        Label(entry_frame, bg='#5E95FF', fg='crimson', text='EMPTY', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=7,sticky='w')
        valid_check += 1
    elif utils.invalid_salary(salary) == 1:
        Label(entry_frame, bg='#5E95FF', fg='crimson', text='INVALID', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=7,sticky='w')
        valid_check += 1
        
    # Validate Position
    if len(position) == 0:
        Label(entry_frame, bg='#5E95FF', fg='crimson', text='EMPTY', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=8,sticky='w')
        valid_check += 1
    
    # If All Valid
    if valid_check == 0:
        # Add to staff_list
        new_staff = Staff(gid, name, gend, dob, phone, email , address)
        if len(salary) > 0:
            new_staff.set_salary(salary)
        if len(position) > 0:
            new_staff.set_position(position)
        staff_list.append(new_staff)

        # Display on Treeview
        staff_tree.insert(parent='', index = 'end', iid=gid, text='', values=(gid, name, gend, dob))

        # Empty Entry boxes
        gid_entry.delete(0, END)
        name_entry.delete(0, END)
        gend_entry.delete(0, END)
        dob_entry.delete(0, END)
        phone_entry.delete(0, END)
        email_entry.delete(0, END)
        address_entry.delete(0, END)
        salary_entry.delete(0, END)
        position_entry.delete(0, END)
        

def staff_remove(staff_list, staff_tree):
    if len(staff_tree.selection())>0:
        selected_staff = staff_tree.selection()[0]
        staff_gid = staff_tree.item(selected_staff, 'values')[0]

        for staff in staff_list:
            if staff.get_gid()== staff_gid:
                staff_list.remove(staff)
                break
        staff_tree.delete(selected_staff)

def all_staff_remove(staff_tree, staff_list):
    for staff in staff_tree.get_children():
        staff_tree.delete(staff)
    staff_list.clear()

def staff_select(staff_list, staff_tree, entry_frame, gid_entry, name_entry, gend_entry, dob_entry, phone_entry, email_entry, address_entry, salary_entry, position_entry):
    # Delete all Warnings
    Label(entry_frame, bg='#5E95FF', fg='crimson', text='                                  ', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=0,sticky='w')
    Label(entry_frame, bg='#5E95FF', fg='crimson', text='                   ', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=1,sticky='w')
    Label(entry_frame, bg='#5E95FF', fg='crimson', text='                   ', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=2,sticky='w')
    Label(entry_frame, bg='#5E95FF', fg='crimson', text='                   ', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=3,sticky='w')
    Label(entry_frame, bg='#5E95FF', fg='crimson', text='                   ', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=4,sticky='w')
    Label(entry_frame, bg='#5E95FF', fg='crimson', text='                   ', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=5,sticky='w')
    Label(entry_frame, bg='#5E95FF', fg='crimson', text='                   ', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=6,sticky='w')
    Label(entry_frame, bg='#5E95FF', fg='crimson', text='                   ', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=7,sticky='w')
    Label(entry_frame, bg='#5E95FF', fg='crimson', text='                   ', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=8,sticky='w')
    
    # Empty Entry boxes
    gid_entry.delete(0, END)
    name_entry.delete(0, END)
    gend_entry.delete(0, END)
    dob_entry.delete(0, END)
    phone_entry.delete(0, END)
    email_entry.delete(0, END)
    address_entry.delete(0, END)
    salary_entry.delete(0, END)
    position_entry.delete(0, END)

    # Show Selected staff Info
    if len(staff_tree.selection())>0:
        global selected_staff
        selected_staff = staff_tree.selection()[0]
        staff_gid = staff_tree.item(selected_staff, 'values')[0]
        for staff in staff_list:
            if staff.get_gid()== staff_gid:
                gid_entry.insert(0, staff.get_gid())
                name_entry.insert(0, staff.get_name())
                gend_entry.insert(0, staff.get_gend())
                dob_entry.insert(0, staff.get_dob())
                phone_entry.insert(0, staff.get_phone())
                email_entry.insert(0, staff.get_email())
                address_entry.insert(0, staff.get_address())
                salary_entry.insert(0, staff.get_salary())
                position_entry.insert(0, staff.get_position())
                break

def staff_update(staff_list, staff_tree, entry_frame, gid_entry, name_entry, gend_entry, dob_entry, phone_entry, email_entry, address_entry, salary_entry, position_entry):
    global selected_staff
    if selected_staff != -1:
        Label(entry_frame, bg='#5E95FF', fg='crimson', text='                                  ', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=0,sticky='w')
        Label(entry_frame, bg='#5E95FF', fg='crimson', text='                   ', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=1,sticky='w')
        Label(entry_frame, bg='#5E95FF', fg='crimson', text='                   ', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=2,sticky='w')
        Label(entry_frame, bg='#5E95FF', fg='crimson', text='                   ', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=3,sticky='w')
        Label(entry_frame, bg='#5E95FF', fg='crimson', text='                   ', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=4,sticky='w')
        Label(entry_frame, bg='#5E95FF', fg='crimson', text='                   ', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=5,sticky='w')
        Label(entry_frame, bg='#5E95FF', fg='crimson', text='                   ', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=6,sticky='w')
        Label(entry_frame, bg='#5E95FF', fg='crimson', text='                   ', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=7,sticky='w')
        Label(entry_frame, bg='#5E95FF', fg='crimson', text='                   ', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=8,sticky='w')
        
        gid = gid_entry.get()
        name = name_entry.get()
        gend = gend_entry.get()
        dob = dob_entry.get()
        phone = phone_entry.get()
        email = email_entry.get()
        address = address_entry.get()
        salary = salary_entry.get()
        position = position_entry.get()
        
        # Validation
        valid_check = 0
        
        #Validate ID
        if len(gid) == 0:
            Label(entry_frame, bg='#5E95FF', fg='crimson', text='EMPTY', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=0,sticky='w')
            valid_check += 1
        elif utils.invalid_id(gid, "S-") == 1:
            Label(entry_frame, bg='#5E95FF', fg='crimson', text='INVALID', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=0,sticky='w')
            valid_check += 1
        else:
            # check if new id is different from old id, if yes, check for duplication
            if gid != staff_tree.item(selected_staff, 'values')[0]:
                for staff in staff_list:
                    if staff.get_gid() == gid:
                        Label(entry_frame, bg='#5E95FF', fg='crimson', text='ID already exist', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=0,sticky='w')
                        valid_check += 1
                        break
        
        # Validate Name
        if len(name) == 0:
            Label(entry_frame, bg='#5E95FF', fg='crimson', text='EMPTY', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=1,sticky='w')
            valid_check += 1

        # Validate Gender
        if len(gend) == 0:
            Label(entry_frame, bg='#5E95FF', fg='crimson', text='EMPTY', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=2,sticky='w')
            valid_check += 1
        elif utils.invalid_gend(gend) == 1:
            Label(entry_frame, bg='#5E95FF', fg='crimson', text='INVALID', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=2,sticky='w')
            valid_check += 1

        # Validate Date of Birth
        if len(dob) == 0:
            Label(entry_frame, bg='#5E95FF', fg='crimson', text='EMPTY', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=3,sticky='w')
            valid_check += 1
        elif utils.invalid_dob(dob) == 1:
            Label(entry_frame, bg='#5E95FF', fg='crimson', text='INVALID', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=3,sticky='w')
            valid_check += 1
            
        # Validate Phone
        if len(phone) == 0:
            Label(entry_frame, bg='#5E95FF', fg='crimson', text='EMPTY', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=4,sticky='w')
            valid_check += 1
        elif utils.invalid_phone(phone) == 1:
            Label(entry_frame, bg='#5E95FF', fg='crimson', text='INVALID', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=4,sticky='w')
            valid_check += 1
        
        # Validate Email
        if len(email) == 0:
            Label(entry_frame, bg='#5E95FF', fg='crimson', text='EMPTY', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=5,sticky='w')
            valid_check += 1
        
        # Validate Address
        if len(address) == 0:
            Label(entry_frame, bg='#5E95FF', fg='crimson', text='EMPTY', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=6,sticky='w')
            valid_check += 1
        
        # Validate Salary
        if len(salary) == 0:
            Label(entry_frame, bg='#5E95FF', fg='crimson', text='EMPTY', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=7,sticky='w')
            valid_check += 1
        elif utils.invalid_salary(salary) == 1:
            Label(entry_frame, bg='#5E95FF', fg='crimson', text='INVALID', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=7,sticky='w')
            valid_check += 1
        
        # Validate Position
        if len(position) == 0:
            Label(entry_frame, bg='#5E95FF', fg='crimson', text='EMPTY', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=8,sticky='w')
            valid_check += 1
        

        # If All Valid
        if valid_check == 0:
            for staff in staff_list:
                if staff.get_gid() == staff_tree.item(selected_staff, 'values')[0]:
                    staff.set_gid(gid)
                    staff.set_name(name)
                    staff.set_gend(gend)
                    staff.set_dob(dob)
                    staff.set_phone(phone)
                    staff.set_email(email)
                    staff.set_address(address)
                    staff.set_salary(salary)
                    staff.set_position(position)
                    break
            
            staff_tree.item(selected_staff, text="", values = (gid, name, gend, dob))
            selected_staff = -1
        
            gid_entry.delete(0, END)
            name_entry.delete(0, END)
            gend_entry.delete(0, END)
            dob_entry.delete(0, END)
            phone_entry.delete(0, END)
            email_entry.delete(0, END)
            address_entry.delete(0, END)
            salary_entry.delete(0, END)
            position_entry.delete(0, END)

def staff_press(window, width, height, staff_list):
    global selected_staff
    selected_staff = -1
    staff_subwin = Toplevel(window)
    staff_subwin.title("Staff Information")
    staff_subwin.geometry("%dx%d+0+0" % (width, height))

    #=====================================================================================
    style = ttk.Style()
    style.theme_use('clam')
    style.configure("Treeview",
        background = "silver",
        foreground = "black",
        rowheight = 25,
        font=("Montserrat Bold", 12),
        fieldbackground = "silver"
        )
    style.configure("Treeview.Heading", font=("Montserrat Bold", 16,'bold'))
    
    style.map('Treeview', background=[('selected', 'dark blue')])

    # Create TreeView List
    staff_tree = ttk.Treeview(staff_subwin, selectmode='browse', show='headings')

    # Define columns
    staff_tree['columns'] = ("ID", "Name", "Gender", "Date of Birth")

    # Format columns
    staff_tree.column("#0", width=0, stretch=NO)
    staff_tree.column("ID", anchor='center', width=75)
    staff_tree.column("Name",anchor='w', width=150)
    staff_tree.column("Gender",anchor='center', width=75)
    staff_tree.column("Date of Birth",anchor='center', width=125)

    # Create Headings
    staff_tree.heading("#0", text="")
    staff_tree.heading("ID", text="ID", anchor='center', command= lambda: utils.sort_people_list_by_column(staff_tree, staff_list, "ID", False))
    staff_tree.heading("Name", text="Name", anchor='center', command= lambda: utils.sort_people_list_by_column(staff_tree, staff_list, "Name", False))
    staff_tree.heading("Gender", text="Gender", anchor='center', command= lambda: utils.sort_people_list_by_column(staff_tree, staff_list, "Gender", False))
    staff_tree.heading("Date of Birth", text="Date of Birth", anchor='center', command= lambda: utils.sort_people_list_by_column(staff_tree, staff_list, "Date of Birth", False))

    staff_tree.bind('<Motion>', 'break')
    
    # Insert Data
    for staff in staff_list:
        staff_tree.insert(parent='', index = 'end', iid=staff.get_gid(), text='', values=(staff.get_gid(), staff.get_name(), staff.get_gend(), staff.get_dob()))
        
    staff_tree.place(x=width/2+50, y=50, height=height-250, width=width/2-100)


    #=========================================================================================
    
    # staff Control
    Label(staff_subwin, bg='#5E95FF', fg='white', text='STAFF MANAGEMENT', font=("Montserrat Bold", 20, 'bold')).place(x=50, y=25, width=width/2-100, height=50)
    #Frame(staff_subwin, bg='crimson').place(x=50, y=85, width=width/2-100, height=2)
    entry_frame = Frame(staff_subwin, bg='#5E95FF')
    entry_frame.place(x=50, y=100, width=width/2-100, height=height/2)
    #Frame(staff_subwin, bg='crimson').place(x=50, y=350, width=width/2-100, height=2)
    Label(staff_subwin, text='  - ID must be " S-xxx " ', anchor='w', bg='#5E95FF', fg='white', font=("Montserrat Bold", 12, 'bold')).place(x=50, y=380, height=30)
    Label(staff_subwin, text='  - Gender must be " Male " or " Female " ', anchor='w', bg='#5E95FF', fg='white', font=("Montserrat Bold", 12, 'bold')).place(x=50, y=410, height=30)
    Label(staff_subwin, text='  - Date of Birth must be " dd/mm/yyyy " ', anchor='w', bg='#5E95FF', fg='white', font=("Montserrat Bold", 12, 'bold')).place(x=50, y=440, height=30)
    Label(staff_subwin, text='  - Phone must be " 0xxxxxxxxx " ', anchor='w', bg='#5E95FF', fg='white', font=("Montserrat Bold", 12, 'bold')).place(x=50, y=470, height=30)
    Label(staff_subwin, text='  - Salary must be number ', anchor='w', bg='#5E95FF', fg='white', font=("Montserrat Bold", 12, 'bold')).place(x=50, y=500, height=30)
    # Column 1: |
    Label(entry_frame, bg='#5E95FF', fg='white', text=' | ', font=("Montserrat Bold", 14, 'bold')).grid(column=1, row=0)
    Label(entry_frame, bg='#5E95FF', fg='white', text=' | ', font=("Montserrat Bold", 14, 'bold')).grid(column=1, row=1)
    Label(entry_frame, bg='#5E95FF', fg='white', text=' | ', font=("Montserrat Bold", 14, 'bold')).grid(column=1, row=2)
    Label(entry_frame, bg='#5E95FF', fg='white', text=' | ', font=("Montserrat Bold", 14, 'bold')).grid(column=1, row=3)
    Label(entry_frame, bg='#5E95FF', fg='white', text=' | ', font=("Montserrat Bold", 14, 'bold')).grid(column=1, row=4)
    Label(entry_frame, bg='#5E95FF', fg='white', text=' | ', font=("Montserrat Bold", 14, 'bold')).grid(column=1, row=5)
    Label(entry_frame, bg='#5E95FF', fg='white', text=' | ', font=("Montserrat Bold", 14, 'bold')).grid(column=1, row=6)
    Label(entry_frame, bg='#5E95FF', fg='white', text=' | ', font=("Montserrat Bold", 14, 'bold')).grid(column=1, row=7)
    Label(entry_frame, bg='#5E95FF', fg='white', text=' | ', font=("Montserrat Bold", 14, 'bold')).grid(column=1, row=8)


    # Column 2: Atribute
    Label(entry_frame, bg='#5E95FF', fg='white', text=' - ID - ', font=("Montserrat Bold", 14, 'bold')).grid(column=2, row=0)
    Label(entry_frame, bg='#5E95FF', fg='white', text=' - Name - ', font=("Montserrat Bold", 14, 'bold')).grid(column=2, row=1)
    Label(entry_frame, bg='#5E95FF', fg='white', text=' - Gender - ', font=("Montserrat Bold", 14, 'bold')).grid(column=2, row=2)
    Label(entry_frame, bg='#5E95FF', fg='white', text=' - DoB - ', font=("Montserrat Bold", 14, 'bold')).grid(column=2, row=3)
    Label(entry_frame, bg='#5E95FF', fg='white', text=' - Phone - ', font=("Montserrat Bold", 14, 'bold')).grid(column=2, row=4)
    Label(entry_frame, bg='#5E95FF', fg='white', text=' - Email - ', font=("Montserrat Bold", 14, 'bold')).grid(column=2, row=5)
    Label(entry_frame, bg='#5E95FF', fg='white', text=' - Address - ', font=("Montserrat Bold", 14, 'bold')).grid(column=2, row=6)
    Label(entry_frame, bg='#5E95FF', fg='white', text=' - Salary - ', font=("Montserrat Bold", 14, 'bold')).grid(column=2, row=7)
    Label(entry_frame, bg='#5E95FF', fg='white', text=' - Position - ', font=("Montserrat Bold", 14, 'bold')).grid(column=2, row=8)


    # Column 3: |
    Label(entry_frame, bg='#5E95FF', fg='white', text=' | ', font=("Montserrat Bold", 14, 'bold')).grid(column=3, row=0)
    Label(entry_frame, bg='#5E95FF', fg='white', text=' | ', font=("Montserrat Bold", 14, 'bold')).grid(column=3, row=1)
    Label(entry_frame, bg='#5E95FF', fg='white', text=' | ', font=("Montserrat Bold", 14, 'bold')).grid(column=3, row=2)
    Label(entry_frame, bg='#5E95FF', fg='white', text=' | ', font=("Montserrat Bold", 14, 'bold')).grid(column=3, row=3)
    Label(entry_frame, bg='#5E95FF', fg='white', text=' | ', font=("Montserrat Bold", 14, 'bold')).grid(column=3, row=4)
    Label(entry_frame, bg='#5E95FF', fg='white', text=' | ', font=("Montserrat Bold", 14, 'bold')).grid(column=3, row=5)
    Label(entry_frame, bg='#5E95FF', fg='white', text=' | ', font=("Montserrat Bold", 14, 'bold')).grid(column=3, row=6)
    Label(entry_frame, bg='#5E95FF', fg='white', text=' | ', font=("Montserrat Bold", 14, 'bold')).grid(column=3, row=7)
    Label(entry_frame, bg='#5E95FF', fg='white', text=' | ', font=("Montserrat Bold", 14, 'bold')).grid(column=3, row=8)

    
    # Column 4: Entries
    gid_entry = Entry(entry_frame)
    gid_entry.grid(column=4,row=0)

    name_entry = Entry(entry_frame)
    name_entry.grid(column=4,row=1)

    gend_entry = Entry(entry_frame)
    gend_entry.grid(column=4,row=2)

    dob_entry = Entry(entry_frame)
    dob_entry.grid(column=4,row=3)
    
    phone_entry = Entry(entry_frame)
    phone_entry.grid(column=4,row=4)
    
    email_entry = Entry(entry_frame)
    email_entry.grid(column=4,row=5)
    
    address_entry = Entry(entry_frame)
    address_entry.grid(column=4,row=6)
    
    salary_entry = Entry(entry_frame)
    salary_entry.grid(column=4,row=7)
    
    position_entry = Entry(entry_frame)
    position_entry.grid(column=4,row=8)

    # Column 5: |
    Label(entry_frame, bg='#5E95FF', fg='white', text=' | ', font=("Montserrat Bold", 14, 'bold')).grid(column=5, row=0)
    Label(entry_frame, bg='#5E95FF', fg='white', text=' | ', font=("Montserrat Bold", 14, 'bold')).grid(column=5, row=1)
    Label(entry_frame, bg='#5E95FF', fg='white', text=' | ', font=("Montserrat Bold", 14, 'bold')).grid(column=5, row=2)
    Label(entry_frame, bg='#5E95FF', fg='white', text=' | ', font=("Montserrat Bold", 14, 'bold')).grid(column=5, row=3)
    Label(entry_frame, bg='#5E95FF', fg='white', text=' | ', font=("Montserrat Bold", 14, 'bold')).grid(column=5, row=4)
    Label(entry_frame, bg='#5E95FF', fg='white', text=' | ', font=("Montserrat Bold", 14, 'bold')).grid(column=5, row=5)
    Label(entry_frame, bg='#5E95FF', fg='white', text=' | ', font=("Montserrat Bold", 14, 'bold')).grid(column=5, row=6)
    Label(entry_frame, bg='#5E95FF', fg='white', text=' | ', font=("Montserrat Bold", 14, 'bold')).grid(column=5, row=7)
    Label(entry_frame, bg='#5E95FF', fg='white', text=' | ', font=("Montserrat Bold", 14, 'bold')).grid(column=5, row=8)

    # Buttons
    add_staff_button = Button(staff_subwin, text='ADD STAFF',anchor='center',font=("Montserrat Bold", 12,'bold'), fg='#5E95FF', relief='ridge',
        activebackground='dark blue', activeforeground='white', command=lambda: staff_add(staff_list, staff_tree, entry_frame, gid_entry, name_entry, gend_entry, dob_entry, phone_entry, email_entry, address_entry, salary_entry, position_entry))
    add_staff_button.place(x=50, y=height-75-85-10-50, width=150, height=50)

    update_staff_button = Button(staff_subwin, text='UPDATE',anchor='center',font=("Montserrat Bold", 12,'bold'), fg='#5E95FF', relief='ridge',
        activebackground='dark blue', activeforeground='white', command=lambda: staff_update(staff_list, staff_tree, entry_frame, gid_entry, name_entry, gend_entry, dob_entry, phone_entry, email_entry, address_entry, salary_entry, position_entry))
    update_staff_button.place(x=width/2-50-150, y=height-75-85-10-50, width=150, height=50)

    clear_button = Button(staff_subwin, text='CLEAR',anchor='center',font=("Montserrat Bold", 12,'bold'), fg='red', relief='ridge',
        activebackground='dark blue', activeforeground='white', command=lambda: clear_entry(entry_frame, gid_entry, name_entry, gend_entry, dob_entry, phone_entry, email_entry, address_entry, salary_entry, position_entry))
    clear_button.place(x=width/4*1-100, y=height-75-85-10-50, width=200, height=50)

    remove_staff_button = Button(staff_subwin, text='REMOVE SELECTED',anchor='center',font=("Montserrat Bold", 12,'bold'),bg='red', fg='white', relief='ridge',
        activebackground='crimson', activeforeground='white', command=lambda: staff_remove(staff_list, staff_tree))
    remove_staff_button.place(x=width/4*3-100, y=height-75-85, width=200, height=50)

    remove_all_staff_button = Button(staff_subwin, text='REMOVE ALL',anchor='center',font=("Montserrat Bold", 12,'bold'),bg='red', fg='white', relief='ridge',
        activebackground='crimson', activeforeground='white', command=lambda: all_staff_remove(staff_tree, staff_list))
    remove_all_staff_button.place(x=width-50-150, y=height-75-85, width=150, height=50)

    select_staff_button = Button(staff_subwin, text='SELECT',anchor='center',font=("Montserrat Bold", 12,'bold'), bg='#5E95FF',fg='white', relief='ridge',
        activebackground='dark blue', activeforeground='white', command=lambda: staff_select(staff_list, staff_tree, entry_frame, gid_entry, name_entry, gend_entry, dob_entry, phone_entry, email_entry, address_entry, salary_entry, position_entry))
    select_staff_button.place(x=width/2+50, y=height-75-85, width=150, height=50)
