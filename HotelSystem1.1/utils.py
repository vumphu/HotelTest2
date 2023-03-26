import datetime


def invalid_id(id, para: str):
    """
    Return 1 if invalid | 0 if valid\n
    Exp: ("S-123", "S-") => Valid\n
        ("a-12", "S-")  => Invalid
    """
    while True:
        try:
            id_num = int(id[-3:])
            if id[:2] != para or len(id) != 5:
                return 1
            else:
                return 0
        except ValueError:
            return 1
        
def invalid_gid(gid, para: str):
    """
    Return 1 if invalid | 0 if valid\n
    Exp: ("S-123", "S-") => Valid\n
        ("a-12", "S-")  => Invalid
    """
    while True:
        try:
            gid_num = int(gid[-3:])
            if gid[:2] != para or len(gid) != 5:
                return 1
            else:
                return 0
        except ValueError:
            return 1
        
def invalid_rid(rid, para: str):
    """
    Return 1 if invalid | 0 if valid\n
    Exp: ("S-123", "S-") => Valid\n
        ("a-12", "S-")  => Invalid
    """
    while True:
        try:
            rid_num = int(rid[-3:])
            if rid[:2] != para or len(rid) != 5:
                return 1
            else:
                return 0
        except ValueError:
            return 1
        
def invalid_no(no):
    while True:
        try:
            no_check = int(no)
            if no_check >= 0:
                return 0
            else: return 1
        except ValueError:
            return 1

def invalid_gend(gend):
    if gend != "Male" and gend != "Female":
        return 1
    else: return 0
    
def invalid_type(type):
    if type != "Luxury" and type != "Gold" and type != "Normal":
        return 1
    else: return 0

def invalid_status(status):
    if status != "Avai" and status != "Unavai":
        return 1
    else:return 0 

def invalid_dob(dob):
    while True:
        try:
            dd_check = int(dob[:2])
            mm_check = int(dob[:5][-2:])
            yyyy_check = int(dob[-4:])
            check1 = dob[:3][-1:]
            check2 = dob[:6][-1:]
            if len(dob) != 10:
                return 1
            elif check1!="/" or check2!="/":
                return 1
            elif dd_check<1 or dd_check>31:
                return 1
            elif mm_check<1 or mm_check>12:
                return 1
            else: return 0
        except ValueError:
            return 1

def invalid_salary(salary):
    while True:
        try:
            salary_check = float(salary)
            if salary_check >= 0:
                return 0
            else: return 1
        except ValueError:
            return 1

def invalid_price(price, type):
    while True:
        try:
            price_check = float(price)
            if price_check == 1000000 and type == "Normal":
                return 0
            elif price_check == 2000000 and type == "Gold":
                return 0
            elif price_check == 3000000 and type == "Luxury":
                return 0
            else: return 1
        except ValueError:
            return 1

def invalid_phone(phone):
    while True:
        try:
            phone_check = float(phone)
            f_check = float(phone[:1])
            if phone_check < 0:
                return 1
            elif f_check != 0:
                return 1
            elif len(phone) != 10:
                return 1
            else:
                return 0
        except ValueError:
            return 1

def sort_people_list_by_column(treeview, arr, col, reverse):
    if(col == "ID"):
        arr.sort(key=lambda x: x.get_gid(),reverse=reverse)
    if(col == "Name"):
        arr.sort(key=lambda x: x.get_name(),reverse=reverse)
    if(col == "Gender"):
        arr.sort(key=lambda x: x.get_gend(),reverse=reverse)
    if(col == "Date of Birth"):
        arr.sort(key=lambda x: datetime.datetime.strptime(x.get_dob(), '%d/%m/%y'),reverse=reverse)
    if(col == "Phone"):
        arr.sort(key=lambda x: x.get_phone(),reverse=reverse)
    if(col == "Email"):
        arr.sort(key=lambda x: x.get_email(),reverse=reverse)
    if(col == "Address"):
        arr.sort(key=lambda x: x.get_address(),reverse=reverse)
    for i in treeview.get_children():
        treeview.delete(i)
    a_count = 0
    for element in arr:
        treeview.insert(parent='', index = 'end', iid=a_count, text='', values=(
            element.get_id(), element.get_name(), element.get_gend(), element.get_dob())
        )
        a_count += 1

    treeview.heading(col, text=col, command=lambda _col=col: \
                 sort_people_list_by_column(treeview, arr, _col, not reverse))

def sort_room_list_by_column(treeview, arr,col, reverse):
    if(col == "ID"):
        arr.sort(key=lambda x: x.get_rid(),reverse=reverse)
    if(col == "Type"):
        arr.sort(key=lambda x: x.get_type(),reverse=reverse)
    if(col == "Price"):
        arr.sort(key=lambda x: x.get_price(),reverse=reverse)
    if(col == "Status"):
        arr.sort(key=lambda x: str(x.get_status()),reverse=reverse)
    for i in treeview.get_children():
        treeview.delete(i)
    a_count = 0
    for element in arr:
        treeview.insert(parent='', index = 'end', iid=a_count, text='', values=(
            element.get_id(), element.get_type(), element.get_price(), element.get_status())
        )
        a_count += 1

    treeview.heading(col, text=col, command=lambda _col=col: \
                 sort_room_list_by_column(treeview, arr, _col, not reverse))
    
def sort_reservation_list_by_column(treeview, arr,col, reverse):
    if(col == "No"):
        arr.sort(key=lambda x: x.get_no(),reverse=reverse)
    if(col == "Room ID"):
        arr.sort(key=lambda x: x.get_rid(),reverse=reverse)
    if(col == "Guest ID"):
        arr.sort(key=lambda x: x.get_gid(),reverse=reverse)
    if(col == "Check in"):
        arr.sort(key=lambda x:  datetime.datetime.strptime(x.get_checkin(), '%d/%m/%y'),reverse=reverse)
    if(col == "Check out"):
        arr.sort(key=lambda x:  datetime.datetime.strptime(x.get_checkout(), '%d/%m/%y'),reverse=reverse)
    if(col == "Payment Date"):
        arr.sort(key=lambda x: datetime.datetime.strptime(x.get_paymentdate(), '%d/%m/%y'),reverse=reverse)
    if(col == "Credit Card"):
        arr.sort(key=lambda x: x.get_creditcard(),reverse=reverse)
    if(col == "Billing"):
        arr.sort(key=lambda x: str(x.get_billing()),reverse=reverse)
    for i in treeview.get_children():
        treeview.delete(i)
    a_count = 0
    for element in arr:
        treeview.insert(parent='', index = 'end', iid=a_count, text='', values=(
            element.get_no(), element.get_rid(), element.get_gid(), element.get_checkin(), element.get_checkout)
        )
        a_count += 1

    treeview.heading(col, text=col, command=lambda _col=col: \
                 sort_reservation_list_by_column(treeview, arr, _col, not reverse))