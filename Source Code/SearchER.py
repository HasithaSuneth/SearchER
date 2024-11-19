import os
import glob
import sqlite3
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from PIL import ImageTk,Image
from tkinter import ttk
from operator import itemgetter

file_name_list = []
film_names_list = []
collection_list = []
print_statue = ''

def clear_txt_files():
	txt_clear_names = open("data/TXT/Film_names.txt","w")
	txt_clear_names.write("")
clear_txt_files()

# Display
root = Tk()
root.title('SeachER - FILM CATEGORY DATABASE')
root.resizable(False, False)
root.iconbitmap('data/image/icon.ico')
#root.geometry("800x600")

conn = sqlite3.connect('data/Database/film_categories.db')
c = conn.cursor()

class Tooltip:
    def __init__(self, widget,
                 *,
                 bg='#424242',
                 pad=(5, 3, 5, 3),
                 text='widget info',
                 waittime=400,
                 wraplength=250,
                 enterimage=None,
                 leaveimage=None):

        self.waittime = waittime  # in miliseconds
        self.wraplength = wraplength  # in pixels
        self.widget = widget
        self.text = text
        self.widget.bind("<Enter>", self.onEnter)
        self.widget.bind("<Leave>", self.onLeave)
        self.widget.bind("<ButtonPress>", self.onLeave)
        self.bg = bg
        self.pad = pad
        self.id = None
        self.tw = None
        self.enterimage = enterimage
        self.leaveimage = leaveimage

    def onEnter(self, event=None):
        self.schedule()
        if self.enterimage != 'None':
        	self.widget.config(image=self.enterimage)

    def onLeave(self, event=None):
        self.unschedule()
        self.hide()
        if self.leaveimage != 'None':
        	self.widget.config(image=self.leaveimage)

    def schedule(self):
        self.unschedule()
        self.id = self.widget.after(self.waittime, self.show)

    def unschedule(self):
    	id_ = self.id
    	self.id = None
    	if id_:
            self.widget.after_cancel(id_)

    def show(self):
        def tip_pos_calculator(widget, label, *, tip_delta=(10, 5), pad=(5, 3, 5, 3)):
            w = widget
            s_width, s_height = w.winfo_screenwidth(), w.winfo_screenheight()
            width, height = (pad[0] + label.winfo_reqwidth() + pad[2],
                             pad[1] + label.winfo_reqheight() + pad[3])
            mouse_x, mouse_y = w.winfo_pointerxy()
            x1, y1 = mouse_x + tip_delta[0], mouse_y + tip_delta[1]
            x2, y2 = x1 + width, y1 + height
            x_delta = x2 - s_width
            if x_delta < 0:
                x_delta = 0
            y_delta = y2 - s_height
            if y_delta < 0:
                y_delta = 0
            offscreen = (x_delta, y_delta) != (0, 0)
            if offscreen:
                if x_delta:
                    x1 = mouse_x - tip_delta[0] - width
                if y_delta:
                    y1 = mouse_y - tip_delta[1] - height
            offscreen_again = y1 < 0  # out on the top
            if offscreen_again:
                y1 = 0
            return x1, y1
        bg = self.bg
        pad = self.pad
        widget = self.widget
        # creates a toplevel window
        self.tw = Toplevel(widget)
        self.tw.wm_overrideredirect(True)
        win = Frame(self.tw,
                       background=bg,
                       borderwidth=0)
        label = Label(win,
                          text=self.text,
                          justify=LEFT,
                          background=bg,
                          relief=SOLID,
                          borderwidth=0,
                          wraplength=self.wraplength,
                          fg="white")
        label.grid(padx=(pad[0], pad[2]),
                   pady=(pad[1], pad[3]),
                   sticky=NSEW)
        win.grid()
        x, y = tip_pos_calculator(widget, label)
        self.tw.wm_geometry("+%d+%d" % (x, y))
    def hide(self):
        tw = self.tw
        if tw:
            tw.destroy()
        self.tw = None

def new_database(event):
	menu_minimize(1)
	response3 = messagebox.askquestion("Warnnig", "Do you really want to create a NEW DATABASE? \n This will lose your existed data !!!")
	if response3 == "yes":
		if os.path.isfile('data/Database/film_categories.db')== False:
			conn = sqlite3.connect('data/Database/film_categories.db')
			c = conn.cursor()
			# Create Table
			c.execute("""CREATE TABLE categories (
				film_name text,
				film_path text,
				language text,
				action integer,
				comedy integer,
				drama integer,
				fantasy integer,
				horror integer,
				mystery integer,
				romance integer,
				thriller integer,
				western integer,
				adventure integer,
				animation integer,
				crime integer,
				documentary integer,
				family integer,
				music integer,
				scifi integer,
				sport integer,
				war integer,
				history integer,
				biography integer,
				collection1 text,
				collection2 text,
				collection3 text,
				collection4 text,
				collection5 text
				)""")
			conn.commit()
			conn.close()			
		else:
			os.remove("data/Database/film_categories.db")
			conn = sqlite3.connect('data/Database/film_categories.db')
			c = conn.cursor()
			# Create Table
			c.execute("""CREATE TABLE categories (
				film_name text,
				film_path text,
				language text,
				action integer,
				comedy integer,
				drama integer,
				fantasy integer,
				horror integer,
				mystery integer,
				romance integer,
				thriller integer,
				western integer,
				adventure integer,
				animation integer,
				crime integer,
				documentary integer,
				family integer,
				music integer,
				scifi integer,
				sport integer,
				war integer,
				history integer,
				biography integer,
				collection1 text,
				collection2 text,
				collection3 text,
				collection4 text,
				collection5 text
				)""")
			conn.commit()
			conn.close()

def deselecting_checkbox():
	action_checkbox.deselect()
	comedy_checkbox.deselect()
	drama_checkbox.deselect()
	fantasy_checkbox.deselect()
	horror_checkbox.deselect()
	mystery_checkbox.deselect()
	romance_checkbox.deselect()
	thriller_checkbox.deselect()
	adventure_checkbox.deselect()
	animation_checkbox.deselect()
	crime_checkbox.deselect()
	documentary_checkbox.deselect()
	family_checkbox.deselect()
	music_checkbox.deselect()
	scifi_checkbox.deselect()
	sport_checkbox.deselect()
	war_checkbox.deselect()
	history_checkbox.deselect()
	biography_checkbox.deselect()
	western_checkbox.deselect()

def combobox_refresh():
	global collection_combobox
	global collection_value
	collection_combobox.pack_forget()
	try:
		collection_combobox = OptionMenu(collection_add_frame, collection_value, *collection_names())
	except:
		collection_combobox = OptionMenu(collection_add_frame, collection_value, "None")
	collection_value.set("Choose Collection")
	collection_combobox.pack(side=LEFT, padx=(10,3))
	collection_combobox.config(width=50, bg='#515A5A', font=("times","9","bold"),activebackground="#2c4c66",activeforeground="white",fg='white',bd=0,highlightthickness=0)
	collection_combobox["menu"].config(bg="#424242", font=("Verdana","8","italic"), fg="White", activebackground="#2c4c66", borderwidth=0)

def file_path_select():
	menu_minimize(1)
	global dirname
	display_film_list.delete(0,END)
	dirname = filedialog.askdirectory(parent=root, initialdir="/", title='SearchER - Select Directory')
	if dirname != "":
		load_film_names()
	else:
		messagebox.showinfo("Information","Select directory path of the movies ")
	
def load_film_names():
	film_paths_list = glob.glob(dirname + "/*")
	film_names_list = [os.path.basename(t) for t in glob.glob(dirname + "/*") ]
	with open("data/TXT/Film_paths.txt","w") as filehandle1:
		for listitems in film_paths_list:
			filehandle1.write('%s\n' % listitems)
	with open("data/TXT/Film_names.txt","w") as filehandle2:
		for listitems in film_names_list:
			filehandle2.write('%s\n' % listitems)
	filehandle1.close()
	filehandle2.close()
	if dirname != "":
		confirm_button["state"]= "normal"
	store_film_names_paths()
	return film_names_list, film_paths_list

def store_film_names_paths():
	film_names = open("data/TXT/Film_names.txt","r")
	film_paths_dir = open("data/TXT/Film_paths.txt","r")
	display_film_list.delete(0,END)
	file_name_list.clear()
	# add film names into list
	for line in film_names:
		stripped_line = line.strip()
		line_list = stripped_line.split()
		file_name_list.append(line_list)
	# insert film names into listbox
	for line in range (len(file_name_list)):
		display_film_list.insert(END, file_name_list[line])
	film_names.close()
	film_paths_dir.close()
	identify_added_films()

def identify_added_films():
	film_names = open("data/TXT/Film_names.txt","r")
	display_film_list.delete(0,END)
	conn = sqlite3.connect('data/Database/film_categories.db')
	c = conn.cursor()
	for line in film_names:
		stripped_line = line.strip()
		c.execute("SELECT *, oid FROM categories WHERE film_name like '%'||?||'%'",(stripped_line,))
		temp_record = c.fetchall()
		if temp_record != []:
			display_film_list.insert(END, str(stripped_line) + " *")
		else:
			display_film_list.insert(END, str(stripped_line))	
	film_names.close()
	conn.close()

def collection_names():
	collection_names = open("data/TXT/Collections.txt","r")
	collection_list.clear()
	for line in collection_names:
		stripped_line = line.strip()
		collection_list.append(stripped_line)
	return collection_list

def collection_main():
	menu_minimize(1)
	collection_main_window = Toplevel()
	collection_main_window.title('SeachER - MOVIE COLLECTION')
	collection_main_window.resizable(False, False)
	collection_main_window.iconbitmap('data/image/icon.ico')
	collection_main_window.grab_set()

	def collection_add_remove():
		def add_to_collection():
			if collection_entry.get() != '':
				if collection_entry.get() != 'None' and collection_entry.get() != 'none':
					name_list.append(collection_entry.get())		
					with open("data/TXT/Collections.txt","w") as filehandle3:
						for listitems in name_list:
							filehandle3.write('%s\n' % listitems)
					collection_entry.delete(0, END)
					show_collection_listbox()
					combobox_refresh()
				else:
					messagebox.showinfo("Information", "Collection name can't be named as 'None' or 'none'", parent=collection_window)	
			else:
				messagebox.showinfo("Information", "Collection name can't be a blank", parent=collection_window)
			
		def delete_from_collection():
			if collection_list_box.curselection() != ():
				response4 = messagebox.askquestion("Warnnig", "Do you really want to DELETE selected collection from database? \nThis will REMOVE selected collection from ALL MOVIES", parent=collection_window)
				if response4 == "yes":
					conn = sqlite3.connect('data/Database/film_categories.db')
					c = conn.cursor()
					c.execute("SELECT *, oid FROM categories WHERE collection1 like '%'||?||'%'",(name_list[collection_list_box.curselection()[0]],))
					search_slot1 = c.fetchall()
					c.execute("SELECT *, oid FROM categories WHERE collection2 like '%'||?||'%'",(name_list[collection_list_box.curselection()[0]],))
					search_slot2 = c.fetchall()
					c.execute("SELECT *, oid FROM categories WHERE collection3 like '%'||?||'%'",(name_list[collection_list_box.curselection()[0]],))
					search_slot3 = c.fetchall()
					c.execute("SELECT *, oid FROM categories WHERE collection4 like '%'||?||'%'",(name_list[collection_list_box.curselection()[0]],))
					search_slot4 = c.fetchall()
					c.execute("SELECT *, oid FROM categories WHERE collection5 like '%'||?||'%'",(name_list[collection_list_box.curselection()[0]],))
					search_slot5 = c.fetchall()

					if search_slot1 != []:
						for search in search_slot1:
							c.execute("""UPDATE categories SET
								collection1 = :collection1
								WHERE oid = :oid""",
								{
								'collection1': "None",
								'oid': itemgetter(28)(search)
								})
					if search_slot2 != []:
						for search in search_slot2:
							c.execute("""UPDATE categories SET
								collection2 = :collection2
								WHERE oid = :oid""",
								{
								'collection2': "None",
								'oid': itemgetter(28)(search)
								})
					if search_slot3 != []:
						for search in search_slot3:
							c.execute("""UPDATE categories SET
								collection3 = :collection3
								WHERE oid = :oid""",
								{
								'collection3': "None",
								'oid': itemgetter(28)(search)
								})
					if search_slot4 != []:
						for search in search_slot4:
							c.execute("""UPDATE categories SET
								collection4 = :collection4
								WHERE oid = :oid""",
								{
								'collection4': "None",
								'oid': itemgetter(28)(search)
								})
					if search_slot5 != []:
						for search in search_slot5:
							c.execute("""UPDATE categories SET
								collection5 = :collection5
								WHERE oid = :oid""",
								{
								'collection5': "None",
								'oid': itemgetter(28)(search)
								})
					conn.commit()
					conn.close()
					del name_list[collection_list_box.curselection()[0]]
					with open("data/TXT/Collections.txt","w") as filehandle4:
						for listitems in name_list:
							filehandle4.write('%s\n' % listitems)
					normal_collection_slots()
					clear_collection_listbox()
					display_collection_list()
					disable_collection_slots()
					show_collection_listbox()
					combobox_refresh()
			else:
				messagebox.showinfo("Information", "Select a collection to delete", parent=collection_window)

		def show_collection_listbox():
			collection_list_box.delete(0, END)
			for show in name_list:
				collection_list_box.insert(END, show)

		def collection_entry_enter(event):
			collection_entry.config(bg='#2c4c66')

		def collection_entry_leave(event):
			collection_entry.config(bg='#515A5A') 

		# Display
		collection_window = Toplevel()
		collection_window.title('ADD / REMOVE COLLECTION')
		collection_window.resizable(False, False)
		collection_window.iconbitmap('data/image/icon.ico')
		collection_window.grab_set()
		#collection_window.attributes("-topmost", True)
		name_list = collection_names()

		# Frame
		collection_list_frame = Frame(collection_window, padx=4, pady=0, bg="#424242")
		collection_list_frame.grid(row=1, column=0)
		collection_add_frame = Frame(collection_window, padx=4, pady=0, bg="#424242")
		collection_add_frame.grid(row=0, column=0, sticky=W+E)
		# Scrollbar
		collection_scrollbar = Scrollbar(collection_list_frame)
		collection_scrollbar.pack(side=RIGHT, fill=Y)
		# Listbox
		collection_list_box = Listbox(collection_list_frame, yscrollcommand=collection_scrollbar.set, width=75, height=15, bg="#424949", font=("Helvetica", "9", "bold"), selectbackground="#408f9b", fg="White", relief='flat' )
		collection_list_box.pack(fill=BOTH, side=LEFT,pady=(0,0))
		# Entry
		collection_entry = Entry(collection_add_frame, bg='#515A5A', relief="flat", fg="white", font=("Times","9","bold italic"), width=47, borderwidth=5)
		collection_entry.grid(row=0, column=0, pady=(7,7), padx=(5,5))
		collection_entry.bind('<Enter>',collection_entry_enter)
		collection_entry.bind('<Leave>',collection_entry_leave)
		collection_entry.bind('<FocusIn>',collection_entry_enter)
		collection_entry.bind('<FocusOut>',collection_entry_leave)
		# Label
		add_collection_state_Label = Label(collection_window, text='Statue  ',relief="flat", fg="white", bg="#424242", pady=3, anchor=E )
		add_collection_state_Label.grid(row=2,column=0, sticky=W+E)
		bar4 = Label(collection_add_frame, image=bar_img, width=2, height=22, bg="#424242")
		bar4.grid(row=0, column=2, padx=5,  pady=(0,0))
		# Button
		collection_add_button = Button(collection_add_frame, command=add_to_collection,image=insert_collection2_img, width=94,height=22, relief="flat", bg="white", font=("Comic", "10", "bold"), fg="#10488d", activebackground ="#515A5A")
		collection_delete_button = Button(collection_add_frame, command=delete_from_collection,image=remove_collection2_img, width=94,height=22, relief="flat", bg="#8593a4", font=("Comic", "10", "bold"), fg="#10488d", activebackground ="#515A5A")
		collection_add_button.grid(row=0, column=1, padx=(10,5), pady=(0,0))
		collection_delete_button.grid(row=0, column=3, padx=5,  pady=(0,0))
		collection_scrollbar.config(command=collection_list_box.yview)
		Tooltip(collection_add_button, text='Create New Collection', wraplength=200, enterimage=insert_collection2_img_enter, leaveimage=insert_collection2_img)
		Tooltip(collection_delete_button, text='Remove Collection', wraplength=200, enterimage=remove_collection2_img_enter, leaveimage=remove_collection2_img)

		show_collection_listbox()
	
	def clear_collection_listbox():
		collection_filmname_list_box.delete(0,END)
		collection_slot1_list_box.delete(0,END)
		collection_slot2_list_box.delete(0,END)
		collection_slot3_list_box.delete(0,END)
		collection_slot4_list_box.delete(0,END)
		collection_slot5_list_box.delete(0,END)
		#collection_combobox.set('')

	def add_movie_to_collection():
		#combo_selection = collection_combobox.get()
		combo_selection = collection_value.get()
		if combo_selection != 'Choose Collection':
			if combo_selection != 'None':
				if collection_filmname_list_box.curselection() != ():
					collection_user_select = collection_filmname_list_box.curselection()[0]
					response5 = messagebox.askquestion("Warnnig", "Do you really want to add selected MOVIE to COLLECTION?", parent=collection_main_window)
					if response5 == 'yes':
						collection_filmname_list_box.config(state='disabled')
						same_collection_detect = itemgetter(23,24,25,26,27)(display_collection_list()[collection_filmname_list_box.curselection()[0]])
						collection_filmname_list_box.config(state='normal')
						if combo_selection in same_collection_detect:
							messagebox.showinfo("Information", " Movie already in selected Collection", parent=collection_main_window)
						else:
							normal_collection_slots()
							conn = sqlite3.connect('data/Database/film_categories.db')
							c = conn.cursor()					
							if itemgetter(23)(display_collection_list()[collection_filmname_list_box.curselection()[0]])=='None':
								c.execute("""UPDATE categories SET
									collection1 = :collection1
									WHERE oid = :oid""",
									{
									'collection1': combo_selection,
									'oid': itemgetter(28)(display_collection_list()[collection_filmname_list_box.curselection()[0]])
									})
							elif itemgetter(24)(display_collection_list()[collection_filmname_list_box.curselection()[0]])=='None':
								c.execute("""UPDATE categories SET
									collection2 = :collection2
									WHERE oid = :oid""",
									{
									'collection2': combo_selection,
									'oid': itemgetter(28)(display_collection_list()[collection_filmname_list_box.curselection()[0]])
									})
							elif itemgetter(25)(display_collection_list()[collection_filmname_list_box.curselection()[0]])=='None':
								c.execute("""UPDATE categories SET
									collection3 = :collection3
									WHERE oid = :oid""",
									{
									'collection3': combo_selection,
									'oid': itemgetter(28)(display_collection_list()[collection_filmname_list_box.curselection()[0]])
									})
							elif itemgetter(26)(display_collection_list()[collection_filmname_list_box.curselection()[0]])=='None':
								c.execute("""UPDATE categories SET
									collection4 = :collection4
									WHERE oid = :oid""",
									{
									'collection4': combo_selection,
									'oid': itemgetter(28)(display_collection_list()[collection_filmname_list_box.curselection()[0]])
									})
							elif itemgetter(27)(display_collection_list()[collection_filmname_list_box.curselection()[0]])=='None':
								c.execute("""UPDATE categories SET
									collection5 = :collection5
									WHERE oid = :oid""",
									{
									'collection5': combo_selection,
									'oid': itemgetter(28)(display_collection_list()[collection_filmname_list_box.curselection()[0]])
									})
							else:
								messagebox.showinfo("Information", " Collection slots are Full !!!", parent=collection_main_window)
							conn.commit()
							conn.close()
							clear_collection_listbox()
							display_collection_list()
							disable_collection_slots()
							collection_filmname_list_box.selection_set(collection_user_select)
							yview_scroll(collection_user_select)
					else:
						return
				else:
					messagebox.showinfo("Information", " Select a movie for add to selected collection ", parent=collection_main_window)
			else:
				messagebox.showinfo("Information", " Movie Collection List Empty! \n First, Create a New Collection ", parent=collection_main_window)
		else:
			messagebox.showinfo("Information", " Select Collection from drop down list", parent=collection_main_window)

	def remove_movie_from_collection():
		add_movie_collection["state"]= "disabled"
		normal_collection_slots()
		collection_filmname_list_box.config(state='disabled')
		collection_value.set("Choose Collection")
		collection_combobox.config(state='disabled')
		remove_movie_collection.grid_forget()
		confirm_delete_movie_collection.grid(row=0, column=3, padx=5, pady=(0,5))
		cancel_delete_movie_collection.grid(row=0, column=4, padx=5, pady=(0,5))
		bar3.grid(row=0, column=2, padx=5, pady=(0,5))

	def confirm_remove_from_collection():
		if collection_slot1_list_box.curselection()==collection_slot2_list_box.curselection()==collection_slot3_list_box.curselection()==collection_slot4_list_box.curselection()==collection_slot5_list_box.curselection()==():
			messagebox.showinfo("Information", " Select Collection want to remove from list", parent=collection_main_window)
		else:
			response6 = messagebox.askquestion("Warnnig", "Do you really want to remove selected MOVIE from COLLECTION?", parent=collection_main_window)
			if response6 == 'yes':
				conn = sqlite3.connect('data/Database/film_categories.db')
				c = conn.cursor()
				if collection_slot1_list_box.curselection() != ():
					collection_user_select_temp = collection_slot1_list_box.curselection()[0]
					c.execute("""UPDATE categories SET
						collection1 = :collection1
						WHERE oid = :oid""",
						{
						'collection1': "None",
						'oid': itemgetter(28)(display_collection_list()[collection_slot1_list_box.curselection()[0]])
						})
				elif collection_slot2_list_box.curselection() != ():
					collection_user_select_temp = collection_slot2_list_box.curselection()[0]
					c.execute("""UPDATE categories SET
						collection2 = :collection2
						WHERE oid = :oid""",
						{
						'collection2': "None",
						'oid': itemgetter(28)(display_collection_list()[collection_slot2_list_box.curselection()[0]])
						})
				elif collection_slot3_list_box.curselection() != ():
					collection_user_select_temp = collection_slot3_list_box.curselection()[0]
					c.execute("""UPDATE categories SET
						collection3 = :collection3
						WHERE oid = :oid""",
						{
						'collection3': "None",
						'oid': itemgetter(28)(display_collection_list()[collection_slot3_list_box.curselection()[0]])
						})
				elif collection_slot4_list_box.curselection() != ():
					collection_user_select_temp = collection_slot4_list_box.curselection()[0]
					c.execute("""UPDATE categories SET
						collection4 = :collection4
						WHERE oid = :oid""",
						{
						'collection4': "None",
						'oid': itemgetter(28)(display_collection_list()[collection_slot4_list_box.curselection()[0]])
						})
				elif collection_slot5_list_box.curselection() != ():
					collection_user_select_temp = collection_slot5_list_box.curselection()[0]
					c.execute("""UPDATE categories SET
						collection5 = :collection5
						WHERE oid = :oid""",
						{
						'collection5': "None",
						'oid': itemgetter(28)(display_collection_list()[collection_slot5_list_box.curselection()[0]])
						})
				conn.commit()
				conn.close()
				clear_collection_listbox()
				display_collection_list()
				cancel_remove()
				collection_filmname_list_box.selection_set(collection_user_select_temp)
				yview_scroll(collection_user_select_temp)
			else:
				return	

	def cancel_remove():
		confirm_delete_movie_collection.grid_forget()
		cancel_delete_movie_collection.grid_forget()
		bar3.grid_forget()
		remove_movie_collection.grid(row=0, column=2, padx=5, pady=(0,5))
		add_movie_collection["state"]= "normal"
		disable_collection_slots()
		collection_filmname_list_box.config(state='normal')
		collection_combobox.config(state='normal')

	def display_collection_list():
		conn = sqlite3.connect('data/Database/film_categories.db')
		c = conn.cursor()
		c.execute("SELECT *, oid FROM categories")
		records = c.fetchall()
		for line in records:
			collection_filmname_list_box.insert(END, itemgetter(0)(line))
			collection_slot1_list_box.insert(END, itemgetter(23)(line))
			collection_slot2_list_box.insert(END, itemgetter(24)(line))
			collection_slot3_list_box.insert(END, itemgetter(25)(line))
			collection_slot4_list_box.insert(END, itemgetter(26)(line))
			collection_slot5_list_box.insert(END, itemgetter(27)(line))
		conn.close()
		return records

	def yview_scroll(*args):
		collection_filmname_list_box.yview(*args)
		collection_slot1_list_box.yview(*args)
		collection_slot2_list_box.yview(*args)
		collection_slot3_list_box.yview(*args)
		collection_slot4_list_box.yview(*args)
		collection_slot5_list_box.yview(*args)

	def disable_collection_slots():
		collection_slot1_list_box.config(state='disabled')
		collection_slot2_list_box.config(state='disabled')
		collection_slot3_list_box.config(state='disabled')
		collection_slot4_list_box.config(state='disabled')
		collection_slot5_list_box.config(state='disabled')

	def normal_collection_slots():
		collection_slot1_list_box.config(state='normal')
		collection_slot2_list_box.config(state='normal')
		collection_slot3_list_box.config(state='normal')
		collection_slot4_list_box.config(state='normal')
		collection_slot5_list_box.config(state='normal')

	def list_focus(event):
		collection_filmname_list_box.selection_set(collection_filmname_list_select)

	def list_focus_get(event):
		global collection_filmname_list_select
		if collection_filmname_list_box.curselection() != ():
			collection_filmname_list_select = collection_filmname_list_box.curselection()[0]

	def mouse_wheel_on(event):
		collection_filmname_list_box.yview("scroll", int(-1*(event.delta/100)),"units")
		collection_slot1_list_box.yview("scroll", int(-1*(event.delta/100)),"units")
		collection_slot2_list_box.yview("scroll", int(-1*(event.delta/100)),"units")
		collection_slot3_list_box.yview("scroll", int(-1*(event.delta/100)),"units")
		collection_slot4_list_box.yview("scroll", int(-1*(event.delta/100)),"units")
		collection_slot5_list_box.yview("scroll", int(-1*(event.delta/100)),"units")
		return "break"

	def key_scroll_down(event):
		if event != ():
			yview_scroll(collection_filmname_list_box.curselection()[0])

	def key_scroll_up(event):
		if event != ():
			yview_scroll(collection_filmname_list_box.curselection()[0]-1)
	def key_scroll_down_collection(event):
		return "break"
	def key_scroll_up_collection(event):
		return "break"

	global collection_filmname_list_select
	collection_filmname_list_select = 0
	# Frame
	global collection_add_frame
	collection_add_frame = Frame(collection_main_window, padx=4, pady=4, bg="#424242")
	movie_collection_list_frame = Frame(collection_main_window, padx=4, bg="#424242")
	collection_add_remove_frame = Frame(collection_main_window, padx=4, pady=4, bg="#424242")
	collection_film_name_frame = Frame(movie_collection_list_frame, pady=4, bg="#424242")
	collection_slot1_frame = Frame(movie_collection_list_frame, bg="#424242")
	collection_slot2_frame = Frame(movie_collection_list_frame, bg="#424242")
	collection_slot3_frame = Frame(movie_collection_list_frame, bg="#424242")
	collection_slot4_frame = Frame(movie_collection_list_frame, bg="#424242")
	collection_slot5_frame = Frame(movie_collection_list_frame, bg="#424242")

	collection_add_frame.grid(row=1, column=0, sticky=W+E)
	movie_collection_list_frame.grid(row=2, column=0)
	collection_add_remove_frame.grid(row=3, column=0, sticky=W+E)
	collection_film_name_frame.pack(side=LEFT)
	collection_slot1_frame.pack(side=LEFT)
	collection_slot2_frame.pack(side=LEFT)
	collection_slot3_frame.pack(side=LEFT)
	collection_slot4_frame.pack(side=LEFT)
	collection_slot5_frame.pack(side=LEFT)
	# Label
	bar3 = Label(collection_add_remove_frame, image=bar_img, width=2, height=24, bg="#424242")
	# Button
	add_remove_collection_button = Button(collection_add_frame,image=new_collection_img, command=collection_add_remove, fg="White", relief="flat", bg="#8593a4", font=("Ariel", "9", "bold"), width=154, height=19,activebackground ="#515A5A")
	add_remove_collection_button.pack(side=RIGHT, padx=10, pady=(5,2))
	add_movie_collection = Button(collection_add_remove_frame, command=add_movie_to_collection,image=insert_collection_img, width=134, height=24, relief="flat", bg="#8593a4", font=("Comic", "10", "bold"), fg="#10488d", activebackground ="#515A5A")
	remove_movie_collection = Button(collection_add_remove_frame, command=remove_movie_from_collection,image=remove_collection_img, width=134, height=24, relief="flat", bg="#8593a4", font=("Comic", "10", "bold"), fg="#10488d", activebackground ="#515A5A")
	cancel_delete_movie_collection = Button(collection_add_remove_frame, command=cancel_remove,image=cancle_img, width=104, height=24,relief="flat", bg="#8593a4", font=("Comic", "10", "bold"), fg="#10488d", activebackground ="#515A5A")
	confirm_delete_movie_collection = Button(collection_add_remove_frame,command=confirm_remove_from_collection,image=second_confirm_img, width=104,height=24, relief="flat", bg="#8593a4", font=("Comic", "10", "bold"), fg="#10488d", activebackground ="#515A5A")
	add_movie_collection.grid(row=0, column=1, padx=5, pady=(0,5))
	remove_movie_collection.grid(row=0, column=2, padx=5, pady=(0,5))
	Tooltip(add_remove_collection_button, text='Create New Collection\nRemove Existed Collection', wraplength=200, enterimage=new_collection_img_enter, leaveimage=new_collection_img)
	Tooltip(add_movie_collection, text='Add Selected Movie to Selected Collection', wraplength=250, enterimage=insert_collection_img_enter, leaveimage=insert_collection_img)
	Tooltip(remove_movie_collection, text='Remove Movie from Selected Collection', wraplength=250, enterimage=remove_collection_img_enter, leaveimage=remove_collection_img)
	Tooltip(confirm_delete_movie_collection, text='Confirm Remove from Collection', wraplength=250, enterimage=second_confirm_img_enter, leaveimage=second_confirm_img)
	Tooltip(cancel_delete_movie_collection, text='Close', wraplength=250, enterimage=cancle_img_enter, leaveimage=cancle_img)
	# Scrollbar
	collection_main_scrollbar = Scrollbar(collection_slot5_frame, command=yview_scroll, relief='flat')
	collection_main_scrollbar.pack(side=RIGHT, fill=Y)
	collection_film_name_scrollbar = Scrollbar(collection_film_name_frame, orient=HORIZONTAL, relief='flat')
	collection_film_name_scrollbar.pack(side=BOTTOM, fill=X)
	collection_slot1_scrollbar = Scrollbar(collection_slot1_frame, orient=HORIZONTAL, relief='flat')
	collection_slot1_scrollbar.pack(side=BOTTOM, fill=X)
	collection_slot2_scrollbar = Scrollbar(collection_slot2_frame, orient=HORIZONTAL, relief='flat')
	collection_slot2_scrollbar.pack(side=BOTTOM, fill=X)
	collection_slot3_scrollbar = Scrollbar(collection_slot3_frame, orient=HORIZONTAL, relief='flat')
	collection_slot3_scrollbar.pack(side=BOTTOM, fill=X)
	collection_slot4_scrollbar = Scrollbar(collection_slot4_frame, orient=HORIZONTAL, relief='flat')
	collection_slot4_scrollbar.pack(side=BOTTOM, fill=X)
	collection_slot5_scrollbar = Scrollbar(collection_slot5_frame, orient=HORIZONTAL, relief='flat')
	collection_slot5_scrollbar.pack(side=BOTTOM, fill=X)
	# Combobox
	global collection_combobox
	global collection_value
	collection_value = StringVar()
	try:
		collection_combobox = OptionMenu(collection_add_frame, collection_value, *collection_names())
	except:
		collection_combobox = OptionMenu(collection_add_frame, collection_value, "None")
	
	collection_combobox.pack(side=LEFT, padx=(10,3))
	collection_combobox.config(width=50, bg='#515A5A', font=("times","9","bold"),activebackground="#2c4c66",activeforeground="white",fg='white',bd=0,highlightthickness=0)
	collection_combobox["menu"].config(bg="#424242", font=("Verdana","8","italic"), fg="White", activebackground="#2c4c66", borderwidth=0)
	collection_combobox.bind('<<ComboboxSelected>>', list_focus)
	collection_value.set("Choose Collection")
	Tooltip(collection_combobox, text='Select Collection for Add Movies Into', wraplength=200)
	# Listbox
	collection_filmname_list_box = Listbox(collection_film_name_frame,xscrollcommand=collection_film_name_scrollbar.set,yscrollcommand=collection_main_scrollbar.set,relief='flat',width=70, height=15, bg="#424949", font=("Helvetica", "9", "bold"), selectbackground="#408f9b", fg="White" )
	collection_filmname_list_box.pack(fill=BOTH, side=LEFT)
	collection_slot1_list_box = Listbox(collection_slot1_frame, xscrollcommand=collection_slot1_scrollbar.set,yscrollcommand=collection_main_scrollbar.set,relief='flat',width=20, height=15, bg="#424949", font=("Helvetica", "9", "bold"), selectbackground="#408f9b", fg="White" )
	collection_slot1_list_box.pack(fill=BOTH, side=LEFT)
	collection_slot2_list_box = Listbox(collection_slot2_frame, xscrollcommand=collection_slot2_scrollbar.set,yscrollcommand=collection_main_scrollbar.set,relief='flat',width=20, height=15, bg="#424949", font=("Helvetica", "9", "bold"), selectbackground="#408f9b", fg="White" )
	collection_slot2_list_box.pack(fill=BOTH, side=LEFT)
	collection_slot3_list_box = Listbox(collection_slot3_frame, xscrollcommand=collection_slot3_scrollbar.set,yscrollcommand=collection_main_scrollbar.set,relief='flat',width=20, height=15, bg="#424949", font=("Helvetica", "9", "bold"), selectbackground="#408f9b", fg="White" )
	collection_slot3_list_box.pack(fill=BOTH, side=LEFT)
	collection_slot4_list_box = Listbox(collection_slot4_frame, xscrollcommand=collection_slot4_scrollbar.set,yscrollcommand=collection_main_scrollbar.set,relief='flat',width=20, height=15, bg="#424949", font=("Helvetica", "9", "bold"), selectbackground="#408f9b", fg="White" )
	collection_slot4_list_box.pack(fill=BOTH, side=LEFT)
	collection_slot5_list_box = Listbox(collection_slot5_frame, xscrollcommand=collection_slot5_scrollbar.set,yscrollcommand=collection_main_scrollbar.set,relief='flat',width=20, height=15, bg="#424949", font=("Helvetica", "9", "bold"), selectbackground="#408f9b", fg="White" )
	collection_slot5_list_box.pack(fill=BOTH, side=LEFT)
	collection_filmname_list_box.bind('<<ListboxSelect>>', list_focus_get)
	collection_filmname_list_box.bind('<MouseWheel>', mouse_wheel_on)
	collection_slot1_list_box.bind('<MouseWheel>', mouse_wheel_on)
	collection_slot2_list_box.bind('<MouseWheel>', mouse_wheel_on)
	collection_slot3_list_box.bind('<MouseWheel>', mouse_wheel_on)
	collection_slot4_list_box.bind('<MouseWheel>', mouse_wheel_on)
	collection_slot5_list_box.bind('<MouseWheel>', mouse_wheel_on)
	collection_filmname_list_box.bind('<Down>', key_scroll_down)
	collection_filmname_list_box.bind('<Up>', key_scroll_up)
	collection_slot1_list_box.bind('<Down>', key_scroll_down_collection)
	collection_slot1_list_box.bind('<Up>', key_scroll_up_collection)
	collection_slot2_list_box.bind('<Down>', key_scroll_down_collection)
	collection_slot2_list_box.bind('<Up>', key_scroll_up_collection)
	collection_slot3_list_box.bind('<Down>', key_scroll_down_collection)
	collection_slot3_list_box.bind('<Up>', key_scroll_up_collection)
	collection_slot4_list_box.bind('<Down>', key_scroll_down_collection)
	collection_slot4_list_box.bind('<Up>', key_scroll_up_collection)
	collection_slot5_list_box.bind('<Down>', key_scroll_down_collection)
	collection_slot5_list_box.bind('<Up>', key_scroll_up_collection)

	collection_film_name_scrollbar.config(command=collection_filmname_list_box.xview)
	collection_slot1_scrollbar.config(command=collection_slot1_list_box.xview)
	collection_slot2_scrollbar.config(command=collection_slot2_list_box.xview)
	collection_slot3_scrollbar.config(command=collection_slot3_list_box.xview)
	collection_slot4_scrollbar.config(command=collection_slot4_list_box.xview)
	collection_slot5_scrollbar.config(command=collection_slot5_list_box.xview)

	display_collection_list()
	disable_collection_slots()
	
def pre_add_data(check):
	menu_minimize(1)
	deselecting_checkbox()
	def pre_confirm():#pre_add_data(k):
		try:
			pre_selected_film=search_record[pre_display_film_list.curselection()[0]]
			deselecting_checkbox()
			if pre_selected_film[2]=="English":
				language.set('English')
			elif pre_selected_film[2]=="Tamil":
				language.set('Tamil')
			elif pre_selected_film[2]=="Hindi":
				language.set('Hindi')
			elif pre_selected_film[2]=="Malayalam":
				language.set('Malayalam')
			elif pre_selected_film[2]=="Korean":
				language.set('Korean')
			elif pre_selected_film[2]=="Chinese":
				language.set('Chinese')
			elif pre_selected_film[2]=="Russian":
				language.set('Russian') 
			elif pre_selected_film[2]=="French":
				language.set('French') 
			elif pre_selected_film[2]=="Spanish":
				language.set('Spanish') 
			elif pre_selected_film[2]=="German":
				language.set('German') 
			elif pre_selected_film[2]=="Japanese":
				language.set('Japanese') 
			elif pre_selected_film[2]=="Italian":
				language.set('Italian') 
			elif pre_selected_film[2]=="Sinhala":
				language.set('Sinhala') 
			elif pre_selected_film[2]=="Telugu":
				language.set('Telugu') 
			elif pre_selected_film[2]=="Kannada":
				language.set('Kannada') 
			elif pre_selected_film[2]=="Thai":
				language.set('Thai') 
			if pre_selected_film[3]==1:
				action_checkbox.select() 
			if pre_selected_film[4]==1:
				comedy_checkbox.select()
			if pre_selected_film[5]==1:
				drama_checkbox.select()
			if pre_selected_film[6]==1:
				fantasy_checkbox.select()
			if pre_selected_film[7]==1:
				horror_checkbox.select()
			if pre_selected_film[8]==1:
				mystery_checkbox.select()
			if pre_selected_film[9]==1:
				romance_checkbox.select()
			if pre_selected_film[10]==1:
				thriller_checkbox.select()
			if pre_selected_film[11]==1:
				western_checkbox.select()
			if pre_selected_film[12]==1:
				adventure_checkbox.select()
			if pre_selected_film[13]==1:
				animation_checkbox.select()
			if pre_selected_film[14]==1:
				crime_checkbox.select()
			if pre_selected_film[15]==1:
				documentary_checkbox.select()
			if pre_selected_film[16]==1:
				family_checkbox.select()
			if pre_selected_film[17]==1:
				music_checkbox.select()
			if pre_selected_film[18]==1:
				scifi_checkbox.select()
			if pre_selected_film[19]==1:
				sport_checkbox.select()
			if pre_selected_film[20]==1:
				war_checkbox.select()
			if pre_selected_film[21]==1:
				history_checkbox.select()
			if pre_selected_film[22]==1:
				biography_checkbox.select()
			pre_data_window.destroy()
			display_film_list.selection_set(selected_film)
			display_film_list.yview(selected_film)
		except:
			messagebox.showerror("Error","Select a FILM to CONFIRM", parent=pre_data_window)

	if display_film_list.curselection() != ():
		pre_select_category_list = []
		selected_film = display_film_list.curselection()[0]
		load_names, load_paths = load_film_names()
		current_select = load_names[selected_film]
		if (' ' in current_select ) == False:
			if ('.' in current_select ) == True:
				current_select=current_select.replace('.',' ')
			if ('_' in current_select ) == True:
				current_select=current_select.replace('_',' ')
			if ('-' in current_select ) == True:
				current_select=current_select.replace('-',' ')

		pre_searchbox_value1 = current_select.split(" ",2)[0]
		try:
			if current_select.split(" ",2)[1] != '':
				pre_searchbox_value2 = current_select.split(" ",2)[1]
			else:
				pre_searchbox_value2 = current_select.split(" ",2)[0]
		except:
			pre_searchbox_value2 = current_select.split(" ",2)[0]
		
		pre_conn = sqlite3.connect('data/Database/pre_film_categories.db')
		pre_c = pre_conn.cursor()
		if len(pre_searchbox_value1) <= 2:
			pre_c.execute("SELECT *, oid FROM categories WHERE film_name like '%'||?||'%'",(pre_searchbox_value2,))
		else:
			if pre_searchbox_value1 == 'the' or pre_searchbox_value1 == 'The':
				pre_c.execute("SELECT *, oid FROM categories WHERE film_name like '%'||?||'%'",(pre_searchbox_value2,))
			else:
				pre_c.execute("SELECT *, oid FROM categories WHERE film_name like '%'||?||'%'",(pre_searchbox_value1,))
			
		search_record = pre_c.fetchall()
		for search in search_record:
			pre_select_category_list.append(itemgetter(0,23)(search))
		pre_conn.commit()
		pre_conn.close()
		if pre_select_category_list != []:
			# Display
			pre_data_window = Toplevel()
			pre_data_window.title('SeachER - Search Results')
			pre_data_window.resizable(False, False)
			pre_data_window.iconbitmap('data/image/icon.ico')
			pre_data_window.grab_set()
			# Frame
			pre_select_frame = LabelFrame(pre_data_window, padx=2, pady=0,  bg="#424242", relief="flat")
			pre_select_frame.grid(row=0, column=0, sticky=W+E)
			pre_select_confirm_frame = LabelFrame(pre_data_window, padx=5, pady=2,  bg="#424242", relief="flat")
			pre_select_confirm_frame.grid(row=1, column=0, sticky=W+E)
			# Scrollbar
			pre_select_scrollbar = Scrollbar(pre_select_frame, relief='flat')
			pre_select_scrollbar.pack(side=RIGHT, fill=Y)
			# Listbox
			pre_display_film_list = Listbox(pre_select_frame, width=75, height=10, yscrollcommand=pre_select_scrollbar.set, bg="#424949", font=("Helvetica", "9"), highlightthickness=0, selectbackground="#408f9b", fg="White", relief="flat", bd=0)
			pre_display_film_list.pack(side=LEFT, fill=BOTH, pady=(3,0))
			pre_display_film_list.delete(0,END)
			pre_select_scrollbar.config(command=pre_display_film_list.yview)
			# Button
			pre_select_button = Button(pre_select_confirm_frame, text="Confirm Select",image=select_img, command=pre_confirm, width=126, height=26, relief="flat", bg="#515a5a", font=("Comic", "10", "bold"), fg="#10488d",activebackground="#515A5A")
			pre_select_button.pack() 
			Tooltip(pre_select_button, text='Confirm', wraplength=200, enterimage=select_img_enter, leaveimage=select_img)
			for show in pre_select_category_list:
				pre_display_film_list.insert(END, itemgetter(0)(show))

		display_film_list.selection_set(selected_film)
		display_film_list.yview(selected_film)

def confirm_add():
	menu_minimize(1)
	try:
		selected_film = display_film_list.curselection()[0]
		load_names, load_paths = load_film_names()

		if action.get()==comedy.get()==drama.get()==fantasy.get()==horror.get()==mystery.get()==romance.get()==thriller.get()==western.get()==adventure.get()==animation.get()==crime.get()==documentary.get()==family.get()==music.get()==scifi.get()==sport.get()==war.get()==0:
			messagebox.showwarning("Database Error","Didn't SELECT Categories for Movie")
		else:
			if language.get()=="Language Options":
				messagebox.showwarning("Database Error","Didn't SELECT a Language for Movie")
			else:
				conn = sqlite3.connect('data/Database/film_categories.db')
				c = conn.cursor()
				c.execute("SELECT *, oid FROM categories WHERE film_name like '%'||?||'%'",(load_names[selected_film],))
				pre_record = c.fetchall()
				conn.close()
				if pre_record != []:
					if load_names[selected_film] != pre_record[0][0]:
						conn = sqlite3.connect('data/Database/film_categories.db')
						c = conn.cursor()
						c.execute("INSERT INTO categories VALUES (:name,:file_dir,:language,:action,:comedy,:drama,:fantasy,:horror,:mystery,:romance,:thriller,:western,:adventure,:animation,:crime,:documentary,:family,:music,:scifi,:sport,:war,:history,:biography,:collection1,:collection2,:collection3,:collection4,:collection4)",
							{
								'name': load_names[selected_film],
								'file_dir': load_paths[selected_film],
								'language': language.get(),
								'action': action.get(),
								'comedy': comedy.get(),
								'drama': drama.get(),
								'fantasy': fantasy.get(),
								'horror': horror.get(),
								'mystery': mystery.get(),
								'romance': romance.get(),
								'thriller': thriller.get(),
								'western': western.get(),
								'adventure': adventure.get(),
								'animation': animation.get(),
								'crime': crime.get(),
								'documentary': documentary.get(),
								'family': family.get(),
								'music': music.get(),
								'scifi': scifi.get(),
								'sport': sport.get(),
								'war': war.get(),
								'history': history.get(),
								'biography': biography.get(),
								'collection1': "None",
								'collection2': "None",
								'collection3': "None",
								'collection4': "None",
								'collection5': "None",
							})
						statue_label = Label(root, text=str(load_names[selected_film]) + " inserted to database", padx=5, bd=2, anchor=W, bg=add_frame_color, fg="White")
						statue_label.grid(row=4, column=0, columnspan=2, sticky=W+E)
						conn.commit()
						conn.close()
					else:
						messagebox.showerror("Database Error"," Selected Film already in the database. \n Use 'Modify Database' for Edit/Remove films in the Database.")
				else:
					conn = sqlite3.connect('data/Database/film_categories.db')
					c = conn.cursor()
					c.execute("INSERT INTO categories VALUES (:name,:file_dir,:language,:action,:comedy,:drama,:fantasy,:horror,:mystery,:romance,:thriller,:western,:adventure,:animation,:crime,:documentary,:family,:music,:scifi,:sport,:war,:history,:biography,:collection1,:collection2,:collection3,:collection4,:collection4)",
						{
							'name': load_names[selected_film],
							'file_dir': load_paths[selected_film],
							'language': language.get(),
							'action': action.get(),
							'comedy': comedy.get(),
							'drama': drama.get(),
							'fantasy': fantasy.get(),
							'horror': horror.get(),
							'mystery': mystery.get(),
							'romance': romance.get(),
							'thriller': thriller.get(),
							'western': western.get(),
							'adventure': adventure.get(),
							'animation': animation.get(),
							'crime': crime.get(),
							'documentary': documentary.get(),
							'family': family.get(),
							'music': music.get(),
							'scifi': scifi.get(),
							'sport': sport.get(),
							'war': war.get(),
							'history': history.get(),
							'biography': biography.get(),
							'collection1': "None",
							'collection2': "None",
							'collection3': "None",
							'collection4': "None",
							'collection5': "None",
						})
					statue_label = Label(root, text=str(load_names[selected_film]) + " inserted to database", padx=5, bd=2, anchor=W, bg=add_frame_color, fg="White")
					statue_label.grid(row=4, column=0, columnspan=2, sticky=W+E)
					conn.commit()
					conn.close()				
				deselecting_checkbox()
		identify_added_films()
		display_film_list.selection_set(selected_film)
		display_film_list.yview(selected_film)
	except:
		messagebox.showerror("Database Error","Didn't SELECT a Movie for add to Database.")

def update_delete():
	display_list = []
	menu_minimize(1)

	# Display
	edit_window = Toplevel()
	edit_window.title('SeachER - FILM DATABASE UPDATE / DELETE')
	edit_window.resizable(False, False)
	edit_window.iconbitmap('data/image/icon.ico')
	edit_window.grab_set()

	conn = sqlite3.connect('data/Database/film_categories.db')
	c = conn.cursor()

	def close_update():
		if update_menu_state == 'maximize':
			update_database_maximize()
		edit_window.destroy()

	def show_database():
		display_database_category_list.config(state=NORMAL)
		display_database_list.delete(0,END)
		display_database_category_list.delete(0,END)
		conn = sqlite3.connect('data/Database/film_categories.db')
		c = conn.cursor()
		c.execute("SELECT *, oid FROM categories")
		records = c.fetchall()
		# insert film names into listbox
		for line in records:
			display_category_list(line)
			display_database_list.insert(END, itemgetter(0)(line))
			display_database_category_list.insert(END,display_list)
			display_list.clear()
		conn.close()
		display_database_category_list.config(state=DISABLED)
		return records

	def display_category_list(display_line):
		if itemgetter(3)(display_line)==1:
			display_list.append('Action,') 
		if itemgetter(4)(display_line)==1:
			display_list.append('Comedy,')
		if itemgetter(5)(display_line)==1:
			display_list.append('Drama,')
		if itemgetter(6)(display_line)==1:
			display_list.append('Fantasy,')
		if itemgetter(7)(display_line)==1:
			display_list.append('Horror,')
		if itemgetter(8)(display_line)==1:
			display_list.append('Mystery,')
		if itemgetter(9)(display_line)==1:
			display_list.append('Romance,')
		if itemgetter(10)(display_line)==1:
			display_list.append('Thriller,')
		if itemgetter(11)(display_line)==1:
			display_list.append('Western,')
		if itemgetter(12)(display_line)==1:
			display_list.append('Adventure,')
		if itemgetter(13)(display_line)==1:
			display_list.append('Animation,')
		if itemgetter(14)(display_line)==1:
			display_list.append('Crime,')
		if itemgetter(15)(display_line)==1:
			display_list.append('Documentary,')
		if itemgetter(16)(display_line)==1:
			display_list.append('Family,')
		if itemgetter(17)(display_line)==1:
			display_list.append('Music,')
		if itemgetter(18)(display_line)==1:
			display_list.append('Sci-Fi,')
		if itemgetter(19)(display_line)==1:
			display_list.append('Sport,')
		if itemgetter(20)(display_line)==1:
			display_list.append('War,')
		if itemgetter(21)(display_line)==1:
			display_list.append('History,')
		if itemgetter(22)(display_line)==1:
			display_list.append('Biography,')
		display_list.append(itemgetter(2)(display_line))

	def update_database_maximize():
		global update_menu_state
		if update_menu_state == 'minimize':
			main_edit_frame.grid(row=3, column=0, sticky=W+E)
			edit_database_button.config(image=update_edit_img_min_enter)
			update_menu_state = 'maximize'
		else:
			main_edit_frame.grid_forget()
			edit_database_button.config(image=update_edit_img_enter)
			update_menu_state = 'minimize'

	def update_database():
		if display_database_list.curselection()==():
			messagebox.showerror("Database Update Error","Didn't SELECT a Movie to UPDATE.", parent=edit_window)
		else:
			if action_update.get()==comedy_update.get()==drama_update.get()==fantasy_update.get()==horror_update.get()==mystery_update.get()==romance_update.get()==thriller_update.get()==western_update.get()==adventure_update.get()==animation_update.get()==crime_update.get()==documentary_update.get()==family_update.get()==music_update.get()==scifi_update.get()==sport_update.get()==war_update.get()==0:
				messagebox.showerror("Database Update Error","Didn't SELECT movie categories.", parent=edit_window)
			else:
				if language_update.get() != 'Language Options':
					if name_edit_entry.get() != "" and path_edit_entry.get() != "":
						response2 = messagebox.askquestion("Warnnig", "Do you really: want to UPDATE this movie categories? ", parent=edit_window)
						if response2 == "yes":
							user_choice_update = display_database_list.curselection()[0]
							conn = sqlite3.connect('data/Database/film_categories.db')
							c = conn.cursor()
							update_film_oid = itemgetter(28)(show_database()[user_choice_update])
							c.execute("""UPDATE categories SET
								film_name = :film_name,
								film_path = :film_path,
								language = :language,
								action = :action,
								comedy = :comedy,
								drama = :drama,
								fantasy = :fantasy,
								horror = :horror ,
								mystery = :mystery,
								romance = :romance,
								thriller = :thriller,
								western = :western,
								adventure = :adventure,
								animation = :animation,
								crime = :crime,
								documentary = :documentary,
								family = :family,
								music = :music,
								scifi = :scifi,
								sport = :sport,
								war = :war,
								history = :history,
								biography = :biography

								WHERE oid = :oid""",
								{
								'film_name': name_edit_entry.get(),
								'film_path': path_edit_entry.get(),
								'language': language_update.get(),
								'action' :action_update.get(),
								'comedy' :comedy_update.get(),
								'drama' :drama_update.get(),
								'fantasy' :fantasy_update.get(),
								'horror' :horror_update.get(),
								'mystery' :mystery_update.get(),
								'romance' :romance_update.get(),
								'thriller' :thriller_update.get(),
								'western' :western_update.get(),
								'adventure' :adventure_update.get(),
								'animation' :animation_update.get(),
								'crime' :crime_update.get(),
								'documentary' :documentary_update.get(),
								'family' :family_update.get(),
								'music' :music_update.get(),
								'scifi' :scifi_update.get(),
								'sport' :sport_update.get(),
								'war' :war_update.get(),
								'history' :history_update.get(),
								'biography' :biography_update.get(),
								'oid': update_film_oid
								})
							conn.commit()
							conn.close()
							show_database()
							deselecting_checkbox_update()
							statue_label = Label(edit_window, text=itemgetter(0)(show_database()[user_choice_update])+" Updated", padx=5, bd=2, anchor=W, bg=update_frame_color, fg="White")
							statue_label.grid(row=4, column=0, columnspan=2, sticky=W+E)
							display_database_list.selection_set(user_choice_update)
							#display_database_list.yview(user_choice_update)
							yview_scroll(user_choice_update)
						else:
							return
					else:
						messagebox.showerror("Database Update Error","Movie Name & Path can't be Empty", parent=edit_window)
				else:
					messagebox.showerror("Database Update Error","Didn't SELECT movie Language.", parent=edit_window)
			
	def delete_database():
		if display_database_list.curselection()==():
			messagebox.showerror("Database Delete Error","Didn't SELECT a Movie to Delete.", parent=edit_window)
		else:
			response = messagebox.askquestion("Warnnig", "Do you really want to REMOVE this movie from database? ", parent=edit_window)
			if response == "yes":
				user_choice_delete = display_database_list.curselection()[0]
				conn = sqlite3.connect('data/Database/film_categories.db')
				c = conn.cursor()
				delete_film_name = itemgetter(0)(show_database()[user_choice_delete])
				delete_film_choise = itemgetter(28)(show_database()[user_choice_delete])
				c.execute("DELETE from categories WHERE oid="+ str(delete_film_choise))
				conn.commit()
				conn.close()
				show_database()
				deselecting_checkbox_update()
				yview_scroll(user_choice_delete)
				statue_label = Label(edit_window, text=delete_film_name+" Deleted", padx=5, bd=2, anchor=W, bg=update_frame_color, fg="White")
				statue_label.grid(row=4, column=0, columnspan=2, sticky=W+E)
				identify_added_films()
			else:
				return

	def deselecting_checkbox_update():
		action_checkbox_update.deselect()
		comedy_checkbox_update.deselect()
		drama_checkbox_update.deselect()
		fantasy_checkbox_update.deselect()
		horror_checkbox_update.deselect()
		mystery_checkbox_update.deselect()
		romance_checkbox_update.deselect()
		thriller_checkbox_update.deselect()
		adventure_checkbox_update.deselect()
		animation_checkbox_update.deselect()
		crime_checkbox_update.deselect()
		documentary_checkbox_update.deselect()
		family_checkbox_update.deselect()
		music_checkbox_update.deselect()
		scifi_checkbox_update.deselect()
		sport_checkbox_update.deselect()
		war_checkbox_update.deselect()
		history_checkbox_update.deselect()
		biography_checkbox_update.deselect()
		western_checkbox_update.deselect()
		name_edit_entry.delete(0,END)
		path_edit_entry.delete(0,END)

	def update_select(event):
		conn = sqlite3.connect('data/Database/film_categories.db')
		c = conn.cursor()
		c.execute("SELECT *, oid FROM categories")
		records = c.fetchall()
		conn.close()
		try:
			select_film_temp=records[display_database_list.curselection()[0]]
			deselecting_checkbox_update()
			name_edit_entry.insert(END, select_film_temp[0])
			path_edit_entry.insert(END, select_film_temp[1])
			if select_film_temp[2]=="English":
				language_update.set('English')
			elif select_film_temp[2]=="Tamil":
				language_update.set('Tamil')
			elif select_film_temp[2]=="Hindi":
				language_update.set('Hindi')
			elif select_film_temp[2]=="Malayalam":
				language_update.set('Malayalam')
			elif select_film_temp[2]=="Korean":
				language_update.set('Korean')
			elif select_film_temp[2]=="Chinese":
				language_update.set('Chinese')
			elif select_film_temp[2]=="Russian":
				language_update.set('Russian') 
			elif select_film_temp[2]=="French":
				language_update.set('French') 
			elif select_film_temp[2]=="Spanish":
				language_update.set('Spanish') 
			elif select_film_temp[2]=="German":
				language_update.set('German') 
			elif select_film_temp[2]=="Japanese":
				language_update.set('Japanese') 
			elif select_film_temp[2]=="Italian":
				language_update.set('Italian') 
			elif select_film_temp[2]=="Sinhala":
				language_update.set('Sinhala') 
			elif select_film_temp[2]=="Telugu":
				language_update.set('Telugu') 
			elif select_film_temp[2]=="Kannada":
				language_update.set('Kannada') 
			elif select_film_temp[2]=="Thai":
				language_update.set('Thai') 
			if select_film_temp[3]==1:
				action_checkbox_update.select() 
			if select_film_temp[4]==1:
				comedy_checkbox_update.select()
			if select_film_temp[5]==1:
				drama_checkbox_update.select()
			if select_film_temp[6]==1:
				fantasy_checkbox_update.select()
			if select_film_temp[7]==1:
				horror_checkbox_update.select()
			if select_film_temp[8]==1:
				mystery_checkbox_update.select()
			if select_film_temp[9]==1:
				romance_checkbox_update.select()
			if select_film_temp[10]==1:
				thriller_checkbox_update.select()
			if select_film_temp[11]==1:
				western_checkbox_update.select()
			if select_film_temp[12]==1:
				adventure_checkbox_update.select()
			if select_film_temp[13]==1:
				animation_checkbox_update.select()
			if select_film_temp[14]==1:
				crime_checkbox_update.select()
			if select_film_temp[15]==1:
				documentary_checkbox_update.select()
			if select_film_temp[16]==1:
				family_checkbox_update.select()
			if select_film_temp[17]==1:
				music_checkbox_update.select()
			if select_film_temp[18]==1:
				scifi_checkbox_update.select()
			if select_film_temp[19]==1:
				sport_checkbox_update.select()
			if select_film_temp[20]==1:
				war_checkbox_update.select()
			if select_film_temp[21]==1:
				history_checkbox_update.select()
			if select_film_temp[22]==1:
				biography_checkbox_update.select()
		except:
			return
	def path_update_folder():
		path_new = filedialog.askdirectory(parent=edit_window, initialdir="/", title='SearchER - Select Directory')
		path_edit_entry.delete(0,END)
		path_edit_entry.insert(END, path_new)

	def path_update_file():
		path_new = filedialog.askopenfilename(parent=edit_window, initialdir="/", title='SearchER - Select Directory')
		path_edit_entry.delete(0,END)
		path_edit_entry.insert(END, path_new)

	def yview_scroll(*args):
		display_database_list.yview(*args)
		display_database_category_list.yview(*args)

	def action_update_enter(event):
		action_checkbox_update.config(selectcolor=update_checkbox_color)
		action_checkbox_update.config(bg=update_checkbox_box_color)
	def action_update_leave(event):
		action_checkbox_update.config(selectcolor=update_checkbox_color)
		action_checkbox_update.config(bg=update_frame_color)
	def comedy_update_enter(event):
		comedy_checkbox_update.config(selectcolor=update_checkbox_color)
		comedy_checkbox_update.config(bg=update_checkbox_box_color)
	def comedy_update_leave(event):
		comedy_checkbox_update.config(selectcolor=update_checkbox_color)
		comedy_checkbox_update.config(bg=update_frame_color)
	def drama_update_enter(event):
		drama_checkbox_update.config(selectcolor=update_checkbox_color)
		drama_checkbox_update.config(bg=update_checkbox_box_color)
	def drama_update_leave(event):
		drama_checkbox_update.config(selectcolor=update_checkbox_color)
		drama_checkbox_update.config(bg=update_frame_color)
	def fantasy_update_enter(event):
		fantasy_checkbox_update.config(selectcolor=update_checkbox_color)
		fantasy_checkbox_update.config(bg=update_checkbox_box_color)
	def fantasy_update_leave(event):
		fantasy_checkbox_update.config(selectcolor=update_checkbox_color)
		fantasy_checkbox_update.config(bg=update_frame_color)
	def horror_update_enter(event):
		horror_checkbox_update.config(selectcolor=update_checkbox_color)
		horror_checkbox_update.config(bg=update_checkbox_box_color)
	def horror_update_leave(event):
		horror_checkbox_update.config(selectcolor=update_checkbox_color)
		horror_checkbox_update.config(bg=update_frame_color)
	def mystery_update_enter(event):
		mystery_checkbox_update.config(selectcolor=update_checkbox_color)
		mystery_checkbox_update.config(bg=update_checkbox_box_color)
	def mystery_update_leave(event):
		mystery_checkbox_update.config(selectcolor=update_checkbox_color)
		mystery_checkbox_update.config(bg=update_frame_color)
	def romance_update_enter(event):
		romance_checkbox_update.config(selectcolor=update_checkbox_color)
		romance_checkbox_update.config(bg=update_checkbox_box_color)
	def romance_update_leave(event):
		romance_checkbox_update.config(selectcolor=update_checkbox_color)
		romance_checkbox_update.config(bg=update_frame_color)
	def thriller_update_enter(event):
		thriller_checkbox_update.config(selectcolor=update_checkbox_color)
		thriller_checkbox_update.config(bg=update_checkbox_box_color)
	def thriller_update_leave(event):
		thriller_checkbox_update.config(selectcolor=update_checkbox_color)
		thriller_checkbox_update.config(bg=update_frame_color)
	def western_update_enter(event):
		western_checkbox_update.config(selectcolor=update_checkbox_color)
		western_checkbox_update.config(bg=update_checkbox_box_color)
	def western_update_leave(event):
		western_checkbox_update.config(selectcolor=update_checkbox_color)
		western_checkbox_update.config(bg=update_frame_color)
	def adventure_update_enter(event):
		adventure_checkbox_update.config(selectcolor=update_checkbox_color)
		adventure_checkbox_update.config(bg=update_checkbox_box_color)
	def adventure_update_leave(event):
		adventure_checkbox_update.config(selectcolor=update_checkbox_color)
		adventure_checkbox_update.config(bg=update_frame_color)
	def animation_update_enter(event):
		animation_checkbox_update.config(selectcolor=update_checkbox_color)
		animation_checkbox_update.config(bg=update_checkbox_box_color)
	def animation_update_leave(event):
		animation_checkbox_update.config(selectcolor=update_checkbox_color)
		animation_checkbox_update.config(bg=update_frame_color)
	def crime_update_enter(event):
		crime_checkbox_update.config(selectcolor=update_checkbox_color)
		crime_checkbox_update.config(bg=update_checkbox_box_color)
	def crime_update_leave(event):
		crime_checkbox_update.config(selectcolor=update_checkbox_color)
		crime_checkbox_update.config(bg=update_frame_color)
	def documentary_update_enter(event):
		documentary_checkbox_update.config(selectcolor=update_checkbox_color)
		documentary_checkbox_update.config(bg=update_checkbox_box_color)
	def documentary_update_leave(event):
		documentary_checkbox_update.config(selectcolor=update_checkbox_color)
		documentary_checkbox_update.config(bg=update_frame_color)
	def family_update_enter(event):
		family_checkbox_update.config(selectcolor=update_checkbox_color)
		family_checkbox_update.config(bg=update_checkbox_box_color)
	def family_update_leave(event):
		family_checkbox_update.config(selectcolor=update_checkbox_color)
		family_checkbox_update.config(bg=update_frame_color)
	def music_update_enter(event):
		music_checkbox_update.config(selectcolor=update_checkbox_color)
		music_checkbox_update.config(bg=update_checkbox_box_color)
	def music_update_leave(event):
		music_checkbox_update.config(selectcolor=update_checkbox_color)
		music_checkbox_update.config(bg=update_frame_color)
	def scifi_update_enter(event):
		scifi_checkbox_update.config(selectcolor=update_checkbox_color)
		scifi_checkbox_update.config(bg=update_checkbox_box_color)
	def scifi_update_leave(event):
		scifi_checkbox_update.config(selectcolor=update_checkbox_color)
		scifi_checkbox_update.config(bg=update_frame_color)
	def sport_update_enter(event):
		sport_checkbox_update.config(selectcolor=update_checkbox_color)
		sport_checkbox_update.config(bg=update_checkbox_box_color)
	def sport_update_leave(event):
		sport_checkbox_update.config(selectcolor=update_checkbox_color)
		sport_checkbox_update.config(bg=update_frame_color)
	def war_update_enter(event):
		war_checkbox_update.config(selectcolor=update_checkbox_color)
		war_checkbox_update.config(bg=update_checkbox_box_color)
	def war_update_leave(event):
		war_checkbox_update.config(selectcolor=update_checkbox_color)
		war_checkbox_update.config(bg=update_frame_color)
	def history_update_enter(event):
		history_checkbox_update.config(selectcolor=update_checkbox_color)
		history_checkbox_update.config(bg=update_checkbox_box_color)
	def history_update_leave(event):
		history_checkbox_update.config(selectcolor=update_checkbox_color)
		history_checkbox_update.config(bg=update_frame_color)
	def biography_update_enter(event):
		biography_checkbox_update.config(selectcolor=update_checkbox_color)
		biography_checkbox_update.config(bg=update_checkbox_box_color)
	def biography_update_leave(event):
		biography_checkbox_update.config(selectcolor=update_checkbox_color)
		biography_checkbox_update.config(bg=update_frame_color)
	def update_edit_min_enter(event):
		if update_menu_state == 'minimize':
			edit_database_button.config(image=update_edit_img_enter)
		if update_menu_state == 'maximize':
			edit_database_button.config(image=update_edit_img_min_enter)	
	def update_edit_min_leave(event):
		if update_menu_state == 'minimize':
			edit_database_button.config(image=update_edit_img)			
		if update_menu_state == 'maximize':
			edit_database_button.config(image=update_edit_img_min)
	def path_edit_fol_enter(event):
		path_edit_button_fol.config(image=path_edit_fol_img_enter)
	def path_edit_fol_leave(event):
		path_edit_button_fol.config(image=path_edit_fol_img)
	def path_edit_fil_enter(event):
		path_edit_button_fil.config(image=path_edit_fil_img_enter)
	def path_edit_fil_leave(event):
		path_edit_button_fil.config(image=path_edit_fil_img)
	def mouse_wheel_edit(event):
		display_database_list.yview("scroll", int((-1*event.delta/100)), "units")
		display_database_category_list.yview("scroll", int((-1*event.delta/100)), "units")
		return "break"
	def key_scroll_down_edit(event):
		if event != ():
			yview_scroll(display_database_list.curselection()[0])

	def key_scroll_up_edit(event):
		if event != ():
			yview_scroll(display_database_list.curselection()[0]-1)

	edit_window.protocol("WM_DELETE_WINDOW", close_update)

	update_frame_color = "#424242"
	update_checkbox_color = "#2c4c66"
	update_checkbox_box_color = "#2c4c66"
	update_checkbox_font = "Comic Sans MS", "9", "bold"
	update_checkbox_width=13

	# Frams
	load_database_frame = LabelFrame(edit_window, bg="#424242",relief='flat', padx=2)
	load_database_name_frame = LabelFrame(load_database_frame, bg="#424242",bd=0)
	load_database_category_frame = LabelFrame(load_database_frame, bg="#424242",bd=0)
	button_frame = LabelFrame(edit_window, padx=5, pady=5, bg="#424242",relief='flat')
	main_edit_frame = LabelFrame(edit_window, padx=5, bg="#424242",relief='flat')
	edit_frame = LabelFrame(main_edit_frame, bg="#424242",relief='flat')
	name_edit_frame = LabelFrame(main_edit_frame, bg="#424242",relief='flat')
	label_frame = LabelFrame(edit_window, bg="#424242",relief='flat')
	load_database_frame.grid(row=1, column=0, sticky=W+E)
	load_database_name_frame.pack(side=LEFT)
	load_database_category_frame.pack(side=LEFT)
	button_frame.grid(row=2, column=0,sticky=W+E)
	label_frame.grid(row=0, column=0,sticky=W+E)
	name_edit_frame.grid(row=0, column=0,sticky=W+E, pady=(0,4))
	edit_frame.grid(row=1, column=0,sticky=W+E)
	
	# Buttons
	edit_database_button = Button(button_frame, text="Update",image=update_edit_img, width=144, height=24, command=update_database_maximize, relief="flat", bg="#424242", font=("Comic", "10", "bold"), fg="#10488d", activebackground ="#515A5A")
	delete_database_button = Button(button_frame, text="Delete",image=remove_movie_img, width=144, height=24, command=delete_database, relief="flat", bg="#8593a4", font=("Comic", "10", "bold"), fg="#10488d", activebackground ="#515A5A")
	confirm_edit_button = Button(edit_frame, text="Confirm Update", image=confirm_img , width=134, height=34, command=update_database, relief="flat", bg="#424242", font=("Comic", "10", "bold"), fg="#10488d", activebackground ="#515A5A")
	path_edit_button_fol = Button(name_edit_frame, text="...", image=path_edit_fol_img,command=path_update_folder, width=24,height=12,relief="flat", bg="#424242", font=("Comic", "10", "bold"), fg="#10488d", activebackground ="#424242")
	path_edit_button_fil = Button(name_edit_frame, text="...", image=path_edit_fil_img, command=path_update_file, width=24,height=12,relief="flat", bg="#424242", font=("Comic", "10", "bold"), fg="#10488d", activebackground ="#424242")
	edit_database_button.grid(row=0, column=1, padx=(170,45))
	confirm_edit_button.grid(row=1, column=5, padx=(15,0), rowspan=2, columnspan=2)
	delete_database_button.grid(row=0, column=2, padx=5)
	path_edit_button_fol.grid(row=0, column=4,padx=(4,0))
	path_edit_button_fil.grid(row=0, column=5)
	Tooltip(confirm_edit_button, text='Confirm update selected movie categories', wraplength=250, enterimage=confirm_img_enter, leaveimage=confirm_img)
	Tooltip(delete_database_button, text='Delete selected movie from database', wraplength=250, enterimage=remove_movie_img_enter, leaveimage=remove_movie_img)
	edit_database_button.bind('<Enter>', update_edit_min_enter)
	edit_database_button.bind('<Leave>', update_edit_min_leave)
	path_edit_button_fol.bind('<Enter>', path_edit_fol_enter)
	path_edit_button_fol.bind('<Leave>', path_edit_fol_leave)
	path_edit_button_fil.bind('<Enter>', path_edit_fil_enter)
	path_edit_button_fil.bind('<Leave>', path_edit_fil_leave)
	Tooltip(path_edit_button_fol, text='Select New Folder Path/Dir for the Movie', wraplength=250, enterimage=path_edit_fol_img_enter, leaveimage=path_edit_fol_img)
	Tooltip(path_edit_button_fil, text='Select New File Path/Dir for the Movie ', wraplength=250, enterimage=path_edit_fil_img_enter, leaveimage=path_edit_fil_img)

	# Scrollbar
	scrollbar_edit = Scrollbar(load_database_category_frame, command=yview_scroll,relief='flat')
	scrollbar_edit_name = Scrollbar(load_database_name_frame,orient=HORIZONTAL, relief='flat')
	scrollbar_edit_category = Scrollbar(load_database_category_frame,orient=HORIZONTAL, relief='flat')
	scrollbar_edit.pack(side=RIGHT, fill=Y)
	scrollbar_edit_name.pack(side=BOTTOM, fill=X)
	scrollbar_edit_category.pack(side=BOTTOM, fill=X)

	# Listbox
	display_database_list = Listbox(load_database_name_frame, xscrollcommand=scrollbar_edit_name.set, yscrollcommand=scrollbar_edit.set, width=60, height=15, bg="#424949", fg="White", font=("Helvetica", "9", "bold"), selectbackground="#408f9b", relief='flat')
	display_database_category_list = Listbox(load_database_category_frame, xscrollcommand=scrollbar_edit_category.set, yscrollcommand=scrollbar_edit.set, width=40, height=15, bg="#424949", fg="White", font=("Helvetica", "9", "bold"), selectbackground="#408f9b", relief='flat')
	display_database_list.pack()
	display_database_category_list.pack()
	display_database_category_list.config(state=DISABLED)
	display_database_list.bind('<<ListboxSelect>>', update_select)
	display_database_list.bind('<MouseWheel>', mouse_wheel_edit)
	display_database_category_list.bind('<MouseWheel>', mouse_wheel_edit)
	display_database_list.bind('<Down>', key_scroll_down_edit)
	display_database_list.bind('<Up>', key_scroll_up_edit)

	# Label
	main_topic_label = Label(label_frame, text="Movie Names\t\t\t\t\t\tCategories", relief=FLAT, bg='#424242', fg="White", font=("Verdana", "8", "italic"))
	statue_label = Label(edit_window, text="Statue", padx=5, bd=2, anchor=E, bg='#424242', fg="White")
	name_edit_label = Label(name_edit_frame, text="Name :", anchor=E, bg='#424242', fg="White")
	path_edit_label = Label(name_edit_frame, text="Path :", anchor=E, bg='#424242', fg="White")
	main_topic_label.pack(pady=(10,0),padx=(30,0))
	statue_label.grid(row=4, column=0, columnspan=2, sticky=W+E)
	name_edit_label.grid(row=0, column=0, padx=(15,0))
	path_edit_label.grid(row=0, column=2, padx=(10,0))

	def on_select(event):
		return "break"

	# Entry
	name_edit_entry = Entry(name_edit_frame, bg='#515A5A', relief="flat", fg="white", font=("Verdana","8"), width=38)
	path_edit_entry = Entry(name_edit_frame, bg='#515A5A', relief="flat", fg="white", font=("Verdana","8"), width=38)
	name_edit_entry.grid(row=0, column=1)
	path_edit_entry.grid(row=0, column=3)
	name_edit_entry.bind("<ButtonPress><Motion>", on_select)
	name_edit_entry.bind("<Double-Button-1>", on_select)
	path_edit_entry.bind("<ButtonPress><Motion>", on_select)
	path_edit_entry.bind("<Double-Button-1>", on_select)

	# Tkinter veriable
	action_update = IntVar()
	comedy_update = IntVar()
	drama_update = IntVar()
	fantasy_update = IntVar()
	horror_update = IntVar()
	mystery_update = IntVar()
	romance_update = IntVar()
	thriller_update = IntVar()
	western_update = IntVar()
	adventure_update = IntVar()
	animation_update = IntVar()
	crime_update = IntVar()
	documentary_update = IntVar()
	family_update = IntVar()
	music_update = IntVar()
	scifi_update = IntVar()
	sport_update = IntVar()
	war_update = IntVar()
	history_update = IntVar()
	biography_update = IntVar()
	language_update = StringVar()

	language_option = ['English','Sinhala','French','Hindi','Tamil','Malayalam','Telugu','Kannada','Korean','Japanese','Spanish','Thai','German','Italian','Chinese','Russian']

	# Dropbox
	language_box_update = OptionMenu(edit_frame, language_update, *language_option)
	language_box_update.config(width=16, bg='#424242', font=("times","9","bold"),activebackground="#2c4c66",activeforeground="white",fg='white',bd=1,highlightthickness=0)
	language_box_update["menu"].config(bg="#424242", font=("times","9","bold italic"), fg="White", activebackground="#2c4c66")
	language_box_update.grid(row=0, column=6)	
	language_update.set('Language Options')
	Tooltip(language_box_update, text='Select Main Language of the Movie', wraplength=200)

	# Checkbox
	action_checkbox_update =  Checkbutton(edit_frame,indicatoron=indic,text=" Action", variable=action_update, width=update_checkbox_width, anchor=W, font=update_checkbox_font, fg="White", bg=update_frame_color, selectcolor=update_checkbox_box_color, activebackground=update_frame_color)
	comedy_checkbox_update  =  Checkbutton(edit_frame,indicatoron=indic,text=" Comedy", variable=comedy_update, width=update_checkbox_width, anchor=W, font=update_checkbox_font, fg="White", bg=update_frame_color, selectcolor=update_checkbox_box_color, activebackground=update_frame_color)
	drama_checkbox_update  =  Checkbutton(edit_frame,indicatoron=indic,text=" Drama", variable=drama_update, width=update_checkbox_width, anchor=W, font=update_checkbox_font, fg="White", bg=update_frame_color, selectcolor=update_checkbox_box_color, activebackground=update_frame_color)
	fantasy_checkbox_update  =  Checkbutton(edit_frame,indicatoron=indic,text=" Fantasy", variable=fantasy_update, width=update_checkbox_width, anchor=W, font=update_checkbox_font, fg="White", bg=update_frame_color, selectcolor=update_checkbox_box_color, activebackground=update_frame_color)
	horror_checkbox_update  =  Checkbutton(edit_frame,indicatoron=indic,text=" Horror", variable=horror_update, width=update_checkbox_width, anchor=W, font=update_checkbox_font, fg="White", bg=update_frame_color, selectcolor=update_checkbox_box_color, activebackground=update_frame_color)
	mystery_checkbox_update  =  Checkbutton(edit_frame,indicatoron=indic,text=" Mystery", variable=mystery_update, width=update_checkbox_width, anchor=W, font=update_checkbox_font, fg="White", bg=update_frame_color, selectcolor=update_checkbox_box_color, activebackground=update_frame_color)
	romance_checkbox_update  =  Checkbutton(edit_frame,indicatoron=indic,text=" Romance", variable=romance_update, width=update_checkbox_width, anchor=W, font=update_checkbox_font, fg="White", bg=update_frame_color, selectcolor=update_checkbox_box_color, activebackground=update_frame_color)
	thriller_checkbox_update  =  Checkbutton(edit_frame,indicatoron=indic,text=" Thriller", variable=thriller_update, width=update_checkbox_width, anchor=W, font=update_checkbox_font, fg="White", bg=update_frame_color, selectcolor=update_checkbox_box_color, activebackground=update_frame_color)
	western_checkbox_update  =  Checkbutton(edit_frame, indicatoron=indic,text=" Western", variable=western_update, width=update_checkbox_width, anchor=W, font=update_checkbox_font, fg="White", bg=update_frame_color, selectcolor=update_checkbox_box_color, activebackground=update_frame_color)
	adventure_checkbox_update  =  Checkbutton(edit_frame,indicatoron=indic,text=" Adventure", variable=adventure_update, width=update_checkbox_width, anchor=W, font=update_checkbox_font, fg="White", bg=update_frame_color, selectcolor=update_checkbox_box_color, activebackground=update_frame_color)
	animation_checkbox_update  =  Checkbutton(edit_frame,indicatoron=indic,text=" Animation", variable=animation_update, width=update_checkbox_width, anchor=W, font=update_checkbox_font, fg="White", bg=update_frame_color, selectcolor=update_checkbox_box_color, activebackground=update_frame_color)
	crime_checkbox_update  =  Checkbutton(edit_frame,indicatoron=indic,text=" Crime", variable=crime_update, width=update_checkbox_width, anchor=W, font=update_checkbox_font, fg="White", bg=update_frame_color, selectcolor=update_checkbox_box_color, activebackground=update_frame_color)
	documentary_checkbox_update  =  Checkbutton(edit_frame,indicatoron=indic,text=" Documentary", variable=documentary_update, width=update_checkbox_width, anchor=W, font=update_checkbox_font, fg="White", bg=update_frame_color, selectcolor=update_checkbox_box_color, activebackground=update_frame_color)
	family_checkbox_update  =  Checkbutton(edit_frame,indicatoron=indic,text=" Family", variable=family_update, width=update_checkbox_width, anchor=W, font=update_checkbox_font, fg="White", bg=update_frame_color, selectcolor=update_checkbox_box_color, activebackground=update_frame_color)
	music_checkbox_update  =  Checkbutton(edit_frame,indicatoron=indic,text=" Music", variable=music_update, width=update_checkbox_width, anchor=W, font=update_checkbox_font, fg="White", bg=update_frame_color, selectcolor=update_checkbox_box_color, activebackground=update_frame_color)
	scifi_checkbox_update  =  Checkbutton(edit_frame,indicatoron=indic,text=" Sci-Fi", variable=scifi_update, width=update_checkbox_width, anchor=W, font=update_checkbox_font, fg="White", bg=update_frame_color, selectcolor=update_checkbox_box_color, activebackground=update_frame_color)
	sport_checkbox_update  =  Checkbutton(edit_frame,indicatoron=indic,text=" Sport", variable=sport_update, width=update_checkbox_width, anchor=W, font=update_checkbox_font, fg="White", bg=update_frame_color, selectcolor=update_checkbox_box_color, activebackground=update_frame_color)
	war_checkbox_update  =  Checkbutton(edit_frame,indicatoron=indic,text=" War", variable=war_update, width=update_checkbox_width, anchor=W, font=update_checkbox_font, fg="White", bg=update_frame_color, selectcolor=update_checkbox_box_color, activebackground=update_frame_color)
	history_checkbox_update  =  Checkbutton(edit_frame,indicatoron=indic,text=" History", variable=history_update, width=update_checkbox_width, anchor=W, font=update_checkbox_font, fg="White", bg=update_frame_color, selectcolor=update_checkbox_box_color, activebackground=update_frame_color)
	biography_checkbox_update  =  Checkbutton(edit_frame,indicatoron=indic,text=" Biography", variable=biography_update, width=update_checkbox_width, anchor=W, font=update_checkbox_font, fg="White", bg=update_frame_color, selectcolor=update_checkbox_box_color, activebackground=update_frame_color)

	action_checkbox_update.grid(row=0, column=0, padx=(15,2), pady=2)
	comedy_checkbox_update.grid(row=0, column=4, padx=2, pady=2)
	drama_checkbox_update.grid(row=1, column=2, padx=2, pady=2)
	fantasy_checkbox_update.grid(row=1, column=4, padx=2, pady=2)
	horror_checkbox_update.grid(row=2, column=0, padx=(15,2), pady=2)
	mystery_checkbox_update.grid(row=2, column=2, padx=2, pady=2)
	romance_checkbox_update.grid(row=2, column=4, padx=2, pady=2)
	thriller_checkbox_update.grid(row=3, column=2, padx=2, pady=2)
	western_checkbox_update.grid(row=3, column=4, padx=2, pady=2)
	adventure_checkbox_update .grid(row=0, column=1, padx=2, pady=2)
	animation_checkbox_update.grid(row=0, column=2, padx=2, pady=2)
	crime_checkbox_update.grid(row=1, column=0, padx=(15,2), pady=2)
	documentary_checkbox_update.grid(row=1, column=1, padx=2, pady=2)
	family_checkbox_update.grid(row=1, column=3, padx=2, pady=2)
	music_checkbox_update.grid(row=2, column=3, padx=2, pady=2)
	scifi_checkbox_update.grid(row=3, column=0, padx=(15,2), pady=2)
	sport_checkbox_update.grid(row=3, column=1, padx=2, pady=2)
	war_checkbox_update.grid(row=3, column=3, padx=2, pady=2)
	history_checkbox_update .grid(row=2, column=1, padx=2, pady=2)
	biography_checkbox_update.grid(row=0, column=3, padx=2, pady=2)

	action_checkbox_update.bind("<Enter>", action_update_enter)
	action_checkbox_update.bind("<Leave>", action_update_leave)
	comedy_checkbox_update.bind("<Enter>", comedy_update_enter)
	comedy_checkbox_update.bind("<Leave>", comedy_update_leave)
	drama_checkbox_update.bind("<Enter>", drama_update_enter)
	drama_checkbox_update.bind("<Leave>", drama_update_leave)
	fantasy_checkbox_update.bind("<Enter>", fantasy_update_enter)
	fantasy_checkbox_update.bind("<Leave>", fantasy_update_leave)
	horror_checkbox_update.bind("<Enter>", horror_update_enter)
	horror_checkbox_update.bind("<Leave>", horror_update_leave)
	mystery_checkbox_update.bind("<Enter>", mystery_update_enter)
	mystery_checkbox_update.bind("<Leave>", mystery_update_leave)
	romance_checkbox_update.bind("<Enter>", romance_update_enter)
	romance_checkbox_update.bind("<Leave>", romance_update_leave)
	thriller_checkbox_update.bind("<Enter>", thriller_update_enter)
	thriller_checkbox_update.bind("<Leave>", thriller_update_leave)
	western_checkbox_update.bind("<Enter>", western_update_enter)
	western_checkbox_update.bind("<Leave>", western_update_leave)
	adventure_checkbox_update.bind("<Enter>", adventure_update_enter)
	adventure_checkbox_update.bind("<Leave>", adventure_update_leave)
	animation_checkbox_update.bind("<Enter>", animation_update_enter)
	animation_checkbox_update.bind("<Leave>", animation_update_leave)
	crime_checkbox_update.bind("<Enter>", crime_update_enter)
	crime_checkbox_update.bind("<Leave>", crime_update_leave)
	documentary_checkbox_update.bind("<Enter>", documentary_update_enter)
	documentary_checkbox_update.bind("<Leave>", documentary_update_leave)
	family_checkbox_update.bind("<Enter>", family_update_enter)
	family_checkbox_update.bind("<Leave>", family_update_leave)
	music_checkbox_update.bind("<Enter>", music_update_enter)
	music_checkbox_update.bind("<Leave>", music_update_leave)
	scifi_checkbox_update.bind("<Enter>", scifi_update_enter)
	scifi_checkbox_update.bind("<Leave>", scifi_update_leave)
	sport_checkbox_update.bind("<Enter>", sport_update_enter)
	sport_checkbox_update.bind("<Leave>", sport_update_leave)
	war_checkbox_update.bind("<Enter>", war_update_enter)
	war_checkbox_update.bind("<Leave>", war_update_leave)
	history_checkbox_update.bind("<Enter>", history_update_enter)
	history_checkbox_update.bind("<Leave>", history_update_leave)
	biography_checkbox_update.bind("<Enter>", biography_update_enter)
	biography_checkbox_update.bind("<Leave>", biography_update_leave)

	scrollbar_edit_name.config(command=display_database_list.xview)
	scrollbar_edit_category.config(command=display_database_category_list.xview)
	show_database()
	conn.close()
	#edit_window.mainloop()

def about_funtion(event):
	messagebox.showinfo("About"," Contact : Hasitha Suneth \n Email : hasisuneth@gmail.com \n Blog : hasisuneth.blogspot.com")
	menu_minimize(1)

def menu_show(event):
	global menu_state
	if menu_state == 'minimize':
		menu_label.grid(row=0, column=0, padx=(5,0), sticky=W)
		create_new_database.grid(row=1, column=0, padx=(5,0), pady=1)
		menu_state = 'maximize'
	else:
		menu_label.grid(row=0, column=0, padx=(5,0), sticky=W)
		create_new_database.grid_forget()
		menu_state = 'minimize'

def menu_minimize(event):
	global menu_state
	menu_label.grid(row=0, column=0, padx=(5,0), sticky=W)
	create_new_database.grid_forget()
	menu_state = 'minimize'

def action_enter(event):
	action_checkbox.config(selectcolor=add_checkbox_box_enter_color)
	action_checkbox.config(bg=add_checkbox_box_enter_color)
def action_leave(event):
	action_checkbox.config(selectcolor=add_checkbox_box_color)
	action_checkbox.config(bg=add_frame_color)
def comedy_enter(event):
	comedy_checkbox.config(selectcolor=add_checkbox_box_enter_color)
	comedy_checkbox.config(bg=add_checkbox_box_enter_color)
def comedy_leave(event):
	comedy_checkbox.config(selectcolor=add_checkbox_box_color)
	comedy_checkbox.config(bg=add_frame_color)
def drama_enter(event):
	drama_checkbox.config(selectcolor=add_checkbox_box_enter_color)
	drama_checkbox.config(bg=add_checkbox_box_enter_color)
def drama_leave(event):
	drama_checkbox.config(selectcolor=add_checkbox_box_color)
	drama_checkbox.config(bg=add_frame_color)
def fantasy_enter(event):
	fantasy_checkbox.config(selectcolor=add_checkbox_box_enter_color)
	fantasy_checkbox.config(bg=add_checkbox_box_enter_color)
def fantasy_leave(event):
	fantasy_checkbox.config(selectcolor=add_checkbox_box_color)
	fantasy_checkbox.config(bg=add_frame_color)
def horror_enter(event):
	horror_checkbox.config(selectcolor=add_checkbox_box_enter_color)
	horror_checkbox.config(bg=add_checkbox_box_enter_color)
def horror_leave(event):
	horror_checkbox.config(selectcolor=add_checkbox_box_color)
	horror_checkbox.config(bg=add_frame_color)
def mystery_enter(event):
	mystery_checkbox.config(selectcolor=add_checkbox_box_enter_color)
	mystery_checkbox.config(bg=add_checkbox_box_enter_color)
def mystery_leave(event):
	mystery_checkbox.config(selectcolor=add_checkbox_box_color)
	mystery_checkbox.config(bg=add_frame_color)
def romance_enter(event):
	romance_checkbox.config(selectcolor=add_checkbox_box_enter_color)
	romance_checkbox.config(bg=add_checkbox_box_enter_color)
def romance_leave(event):
	romance_checkbox.config(selectcolor=add_checkbox_box_color)
	romance_checkbox.config(bg=add_frame_color)
def thriller_enter(event):
	thriller_checkbox.config(selectcolor=add_checkbox_box_enter_color)
	thriller_checkbox.config(bg=add_checkbox_box_enter_color)
def thriller_leave(event):
	thriller_checkbox.config(selectcolor=add_checkbox_box_color)
	thriller_checkbox.config(bg=add_frame_color)
def western_enter(event):
	western_checkbox.config(selectcolor=add_checkbox_box_enter_color)
	western_checkbox.config(bg=add_checkbox_box_enter_color)
def western_leave(event):
	western_checkbox.config(selectcolor=add_checkbox_box_color)
	western_checkbox.config(bg=add_frame_color)
def adventure_enter(event):
	adventure_checkbox.config(selectcolor=add_checkbox_box_enter_color)
	adventure_checkbox.config(bg=add_checkbox_box_enter_color)
def adventure_leave(event):
	adventure_checkbox.config(selectcolor=add_checkbox_box_color)
	adventure_checkbox.config(bg=add_frame_color)
def animation_enter(event):
	animation_checkbox.config(selectcolor=add_checkbox_box_enter_color)
	animation_checkbox.config(bg=add_checkbox_box_enter_color)
def animation_leave(event):
	animation_checkbox.config(selectcolor=add_checkbox_box_color)
	animation_checkbox.config(bg=add_frame_color)
def crime_enter(event):
	crime_checkbox.config(selectcolor=add_checkbox_box_enter_color)
	crime_checkbox.config(bg=add_checkbox_box_enter_color)
def crime_leave(event):
	crime_checkbox.config(selectcolor=add_checkbox_box_color)
	crime_checkbox.config(bg=add_frame_color)
def documentary_enter(event):
	documentary_checkbox.config(selectcolor=add_checkbox_box_enter_color)
	documentary_checkbox.config(bg=add_checkbox_box_enter_color)
def documentary_leave(event):
	documentary_checkbox.config(selectcolor=add_checkbox_box_color)
	documentary_checkbox.config(bg=add_frame_color)
def family_enter(event):
	family_checkbox.config(selectcolor=add_checkbox_box_enter_color)
	family_checkbox.config(bg=add_checkbox_box_enter_color)
def family_leave(event):
	family_checkbox.config(selectcolor=add_checkbox_box_color)
	family_checkbox.config(bg=add_frame_color)
def music_enter(event):
	music_checkbox.config(selectcolor=add_checkbox_box_enter_color)
	music_checkbox.config(bg=add_checkbox_box_enter_color)
def music_leave(event):
	music_checkbox.config(selectcolor=add_checkbox_box_color)
	music_checkbox.config(bg=add_frame_color)
def scifi_enter(event):
	scifi_checkbox.config(selectcolor=add_checkbox_box_enter_color)
	scifi_checkbox.config(bg=add_checkbox_box_enter_color)
def scifi_leave(event):
	scifi_checkbox.config(selectcolor=add_checkbox_box_color)
	scifi_checkbox.config(bg=add_frame_color)
def sport_enter(event):
	sport_checkbox.config(selectcolor=add_checkbox_box_enter_color)
	sport_checkbox.config(bg=add_checkbox_box_enter_color)
def sport_leave(event):
	sport_checkbox.config(selectcolor=add_checkbox_box_color)
	sport_checkbox.config(bg=add_frame_color)
def war_enter(event):
	war_checkbox.config(selectcolor=add_checkbox_box_enter_color)
	war_checkbox.config(bg=add_checkbox_box_enter_color)
def war_leave(event):
	war_checkbox.config(selectcolor=add_checkbox_box_color)
	war_checkbox.config(bg=add_frame_color)
def history_enter(event):
	history_checkbox.config(selectcolor=add_checkbox_box_enter_color)
	history_checkbox.config(bg=add_checkbox_box_enter_color)
def history_leave(event):
	history_checkbox.config(selectcolor=add_checkbox_box_color)
	history_checkbox.config(bg=add_frame_color)
def biography_enter(event):
	biography_checkbox.config(selectcolor=add_checkbox_box_enter_color)
	biography_checkbox.config(bg=add_checkbox_box_enter_color)
def biography_leave(event):
	biography_checkbox.config(selectcolor=add_checkbox_box_color)
	biography_checkbox.config(bg=add_frame_color)
def menu_enter(event):
	menu_label.config(bg="#2c4c66")
def menu_leave(event):
	menu_label.config(bg="#8593a4")
def new_database_enter(event):
	create_new_database.config(bg="#2c4c66")
def new_database_leave(event):
	create_new_database.config(bg="#8593a4")

menu_state = 'minimize'
update_menu_state = 'minimize'
add_frame_color = "#424242"
add_checkbox_color = "#408f9b"
add_checkbox_box_color = "#2c4c66"
add_checkbox_box_enter_color = "#2c4c66"
add_checkbox_font = "Comic Sans MS", "9", "bold"
indic=0
checkbox_width=13

open_img = ImageTk.PhotoImage(Image.open("data/image/open_button.jpg"))
open_img_enter = ImageTk.PhotoImage(Image.open("data/image/open_button_enter.jpg"))
collection_img = ImageTk.PhotoImage(Image.open("data/image/collection_button.jpg"))
collection_img_enter = ImageTk.PhotoImage(Image.open("data/image/collection_enter_button.jpg"))
update_img = ImageTk.PhotoImage(Image.open("data/image/update_button.jpg"))
update_img_enter = ImageTk.PhotoImage(Image.open("data/image/update_button_enter.jpg"))
bar_img = ImageTk.PhotoImage(Image.open("data/image/bar.jpg"))
confirm_img = ImageTk.PhotoImage(Image.open("data/image/confirm_button.jpg"))
confirm_img_enter = ImageTk.PhotoImage(Image.open("data/image/confirm_button_enter.jpg"))
select_img = ImageTk.PhotoImage(Image.open("data/image/select_button.jpg"))
select_img_enter = ImageTk.PhotoImage(Image.open("data/image/select_button_enter.jpg"))
new_collection_img = ImageTk.PhotoImage(Image.open("data/image/new_collection_button.jpg"))
new_collection_img_enter = ImageTk.PhotoImage(Image.open("data/image/new_collection_button_enter.jpg"))
insert_collection_img = ImageTk.PhotoImage(Image.open("data/image/insert_collection_button.jpg"))
insert_collection_img_enter = ImageTk.PhotoImage(Image.open("data/image/insert_collection_button_enter.jpg"))
remove_collection_img = ImageTk.PhotoImage(Image.open("data/image/remove_collection_button.jpg"))
remove_collection_img_enter = ImageTk.PhotoImage(Image.open("data/image/remove_collection_button_enter.jpg"))
second_confirm_img = ImageTk.PhotoImage(Image.open("data/image/2nd_confirm_button.jpg"))
second_confirm_img_enter = ImageTk.PhotoImage(Image.open("data/image/2nd_confirm_button_enter.jpg"))
cancle_img = ImageTk.PhotoImage(Image.open("data/image/cancle_button.jpg"))
cancle_img_enter = ImageTk.PhotoImage(Image.open("data/image/cancle_button_enter.jpg"))
insert_collection2_img = ImageTk.PhotoImage(Image.open("data/image/insert_button2.jpg"))
insert_collection2_img_enter = ImageTk.PhotoImage(Image.open("data/image/insert_button2_enter.jpg"))
remove_collection2_img = ImageTk.PhotoImage(Image.open("data/image/remove_button2.jpg"))
remove_collection2_img_enter = ImageTk.PhotoImage(Image.open("data/image/remove_button2_enter.jpg"))
update_edit_img = ImageTk.PhotoImage(Image.open("data/image/update_edit_button.jpg"))
update_edit_img_enter = ImageTk.PhotoImage(Image.open("data/image/update_edit_button_enter.jpg"))
update_edit_img_min = ImageTk.PhotoImage(Image.open("data/image/update_edit_button_min.jpg"))
update_edit_img_min_enter = ImageTk.PhotoImage(Image.open("data/image/update_edit_button_min_enter.jpg"))
remove_movie_img = ImageTk.PhotoImage(Image.open("data/image/remove_movie_button.jpg"))
remove_movie_img_enter = ImageTk.PhotoImage(Image.open("data/image/remove_movie_button_enter.jpg"))
path_edit_fol_img = ImageTk.PhotoImage(Image.open("data/image/path_edit_fol_button.jpg"))
path_edit_fol_img_enter = ImageTk.PhotoImage(Image.open("data/image/path_edit_fol_button_enter.jpg"))
path_edit_fil_img = ImageTk.PhotoImage(Image.open("data/image/path_edit_fil_button.jpg"))
path_edit_fil_img_enter = ImageTk.PhotoImage(Image.open("data/image/path_edit_fil_button_enter.jpg"))

# Frams
menu_frame = LabelFrame(root, padx=1, pady=1, bg='#424242', relief="flat")
open_path_frame = LabelFrame(root, padx=2, pady=2, bg='#515A5A', relief="flat")
display_film_frame = LabelFrame(root, padx=5, pady=5, bg="#424242", relief="flat")
select_category_frame = LabelFrame(root, padx=5, pady=5, bg="#424242", relief="flat")
menu_frame.grid(row=0, column=0, sticky=W+E)
open_path_frame.grid(row=1, column=0, sticky=W+E)
display_film_frame.grid(row=2, column=0)
select_category_frame.grid(row=3, column=0, sticky=W+E)
menu_frame.bind('<Button-1>', menu_minimize)
open_path_frame.bind('<Button-1>', menu_minimize)
display_film_frame.bind('<Button-1>', menu_minimize)
select_category_frame.bind('<Button-1>', menu_minimize)

# Buttons
open_path_button = Button(open_path_frame, text="Open", image=open_img, command=file_path_select, width=134,height=39, padx=8, relief="flat", font=("Comic", "10", "bold"), fg="#10488d", activebackground ="#515A5A")
confirm_button = Button(select_category_frame,image=confirm_img , width=134, height=34, command=confirm_add, relief="flat", bg="#424242", font=("Comic", "10", "bold"), fg="#10488d", activebackground ="#515A5A")
collection_button = Button(open_path_frame, text="Open", image=collection_img, command=collection_main, width=154,height=39, padx=8, relief="flat", font=("Comic", "10", "bold"), fg="#10488d", activebackground ="#515A5A")
database_update_button = Button(open_path_frame, text="Open", image=update_img, command=update_delete, width=154,height=39, padx=8, relief="flat", font=("Comic", "10", "bold"), fg="#10488d", activebackground ="#515A5A")

open_path_button.grid(row=0, column=2, padx=(10,5))
collection_button.grid(row=0, column=4, padx=(5,5))
database_update_button.grid(row=0, column=6, padx=(5,5))
confirm_button.grid(row=1, column=5, columnspan=2, rowspan=2)
confirm_button["state"]= "disabled"
Tooltip(open_path_button, text='Open All Movies Directory Path', wraplength=250, enterimage=open_img_enter, leaveimage=open_img)
Tooltip(collection_button, text='Create/Remove Collections\nAdd/Remove Movies to Collections', wraplength=200, enterimage=collection_img_enter, leaveimage=collection_img)
Tooltip(database_update_button, text='Change Movies Categories & Language\nRemove Movies from the Database', wraplength=300, enterimage=update_img_enter, leaveimage=update_img)
Tooltip(confirm_button, text='Add Selected Movie to the Database', wraplength=200, enterimage=confirm_img_enter, leaveimage=confirm_img)

# Scrollbar
scrollbar = Scrollbar(display_film_frame)
scrollbar.pack(side=RIGHT, fill=Y)

# Listbox
display_film_list = Listbox(display_film_frame, relief="flat", yscrollcommand=scrollbar.set, width=96, height=15, bg="#424949", font=("Helvetica", "9"), selectbackground="#408f9b", fg="White") # bg="#8593a4"
display_film_list.pack(side=LEFT, fill=BOTH)
display_film_list.bind('<<ListboxSelect>>', pre_add_data)
display_film_list.bind('<Up>',lambda e: "break")
display_film_list.bind('<Down>',lambda e: "break")

store_film_names_paths()

# Label
about_upadte = Label(root, text="Created by Hasitha Suneth", padx=5, bg='#515A5A', fg="white", relief="flat",font=("Comic Sans MS", "8", "italic"))
statue_label = Label(root, text="Statue", padx=5, bd=2, anchor=E, bg=add_frame_color, fg="White")
menu_label = Label(menu_frame, text="Menu", width=10, fg="White", relief="flat", bg="#8593a4", font=("Ariel", "9", "bold") )
create_new_database = Label(menu_frame, text="Create New Database", fg="White", relief="flat", bg="#8593a4", font=("Ariel", "8", "bold"), width=20)
bar1 = Label(open_path_frame, image=bar_img, width=2, height=38, bg='#515A5A')
bar1.grid(row=0, column=3)
bar2 = Label(open_path_frame, image=bar_img, width=2, height=38, bg='#515A5A')
bar2.grid(row=0, column=5)
menu_label.grid(row=0, column=0, padx=(5,0), sticky=W)
statue_label.grid(row=4, column=0, columnspan=2, sticky=W+E)
about_upadte.grid(row=5, column=0, columnspan=2, sticky=W+E)
about_upadte.bind('<Button-1>', about_funtion)
menu_label.bind('<Button-1>', menu_show)
menu_label.bind('<Enter>', menu_enter)
menu_label.bind('<Leave>', menu_leave)
create_new_database.bind('<Button-1>', new_database)
create_new_database.bind('<Enter>', new_database_enter)
create_new_database.bind('<Leave>', new_database_leave)

# Tkinter veriable
action = IntVar()
comedy = IntVar()
drama = IntVar()
fantasy = IntVar()
horror = IntVar()
mystery = IntVar()
romance = IntVar()
thriller = IntVar()
western = IntVar()
adventure = IntVar()
animation = IntVar()
crime = IntVar()
documentary = IntVar()
family = IntVar()
music = IntVar()
scifi = IntVar()
sport = IntVar()
war = IntVar()
history = IntVar()
biography = IntVar()
language = StringVar()

language_option = ['English','Sinhala','French','Hindi','Tamil','Malayalam','Telugu','Kannada','Korean','Japanese','Spanish','Thai','German','Italian','Chinese','Russian']

# Dropbox
language_box = OptionMenu(select_category_frame, language, *language_option)
language_box.config(width=16, bg=add_frame_color, font=("times","9","bold"),activebackground="#2c4c66",activeforeground="white",fg='white',bd=1,highlightthickness=0)
language_box["menu"].config(bg="#424242", font=("times","9","bold italic"), fg="White", activebackground="#2c4c66")
language_box.grid(row=0, column=5, padx=13)
language.set('Language Options')
Tooltip(language_box, text='Select Main Language of the Movie', wraplength=200)

# Checkbox
action_checkbox =  Checkbutton(select_category_frame, indicatoron=indic,text=" Action", variable=action, width=checkbox_width, anchor=W, bg=add_frame_color, font=add_checkbox_font, fg="White", selectcolor=add_checkbox_box_color, activebackground=add_frame_color)
comedy_checkbox =  Checkbutton(select_category_frame, indicatoron=indic,text=" Comedy", variable=comedy, width=checkbox_width, anchor=W, bg=add_frame_color, font=add_checkbox_font, fg="White", selectcolor=add_checkbox_box_color, activebackground=add_frame_color)
drama_checkbox =  Checkbutton(select_category_frame,indicatoron=indic, text=" Drama", variable=drama, width=checkbox_width, anchor=W, bg=add_frame_color, font=add_checkbox_font, fg="White", selectcolor=add_checkbox_box_color, activebackground=add_frame_color)
fantasy_checkbox =  Checkbutton(select_category_frame, indicatoron=indic,text=" Fantasy", variable=fantasy, width=checkbox_width, anchor=W, bg=add_frame_color, font=add_checkbox_font, fg="White", selectcolor=add_checkbox_box_color, activebackground=add_frame_color)
horror_checkbox =  Checkbutton(select_category_frame, indicatoron=indic,text=" Horror", variable=horror, width=checkbox_width, anchor=W, bg=add_frame_color, font=add_checkbox_font, fg="White", selectcolor=add_checkbox_box_color, activebackground=add_frame_color)
mystery_checkbox =  Checkbutton(select_category_frame,indicatoron=indic, text=" Mystery", variable=mystery, width=checkbox_width, anchor=W, bg=add_frame_color, font=add_checkbox_font, fg="White", selectcolor=add_checkbox_box_color, activebackground=add_frame_color)
romance_checkbox =  Checkbutton(select_category_frame, indicatoron=indic,text=" Romance", variable=romance, width=checkbox_width, anchor=W, bg=add_frame_color, font=add_checkbox_font, fg="White", selectcolor=add_checkbox_box_color, activebackground=add_frame_color)
thriller_checkbox =  Checkbutton(select_category_frame,indicatoron=indic, text=" Thriller", variable=thriller, width=checkbox_width, anchor=W, bg=add_frame_color, font=add_checkbox_font, fg="White", selectcolor=add_checkbox_box_color, activebackground=add_frame_color)
western_checkbox =  Checkbutton(select_category_frame, indicatoron=indic,text=" Western", variable=western, width=checkbox_width, anchor=W, bg=add_frame_color, font=add_checkbox_font, fg="White", selectcolor=add_checkbox_box_color, activebackground=add_frame_color)
adventure_checkbox =  Checkbutton(select_category_frame,indicatoron=indic, text=" Adventure", variable=adventure, width=checkbox_width, anchor=W, bg=add_frame_color, font=add_checkbox_font, fg="White", selectcolor=add_checkbox_box_color, activebackground=add_frame_color)
animation_checkbox =  Checkbutton(select_category_frame,indicatoron=indic, text=" Animation", variable=animation, width=checkbox_width, anchor=W, bg=add_frame_color, font=add_checkbox_font, fg="White", selectcolor=add_checkbox_box_color, activebackground=add_frame_color)
crime_checkbox =  Checkbutton(select_category_frame,indicatoron=indic, text=" Crime", variable=crime, width=checkbox_width, anchor=W, bg=add_frame_color, font=add_checkbox_font, fg="White", selectcolor=add_checkbox_box_color, activebackground=add_frame_color)
documentary_checkbox =  Checkbutton(select_category_frame,indicatoron=indic, text=" Documentary", variable=documentary, width=checkbox_width, anchor=W, bg=add_frame_color, font=add_checkbox_font, fg="White", selectcolor=add_checkbox_box_color, activebackground=add_frame_color)
family_checkbox =  Checkbutton(select_category_frame, indicatoron=indic,text=" Family", variable=family, width=checkbox_width, anchor=W, bg=add_frame_color, font=add_checkbox_font, fg="White", selectcolor=add_checkbox_box_color, activebackground=add_frame_color)
music_checkbox =  Checkbutton(select_category_frame, indicatoron=indic,text=" Music", variable=music, width=checkbox_width, anchor=W, bg=add_frame_color, font=add_checkbox_font, fg="White", selectcolor=add_checkbox_box_color, activebackground=add_frame_color)
scifi_checkbox =  Checkbutton(select_category_frame,indicatoron=indic, text=" Sci-Fi", variable=scifi, width=checkbox_width, anchor=W, bg=add_frame_color, font=add_checkbox_font, fg="White", selectcolor=add_checkbox_box_color, activebackground=add_frame_color)
sport_checkbox =  Checkbutton(select_category_frame, indicatoron=indic,text=" Sport", variable=sport, width=checkbox_width, anchor=W, bg=add_frame_color, font=add_checkbox_font, fg="White", selectcolor=add_checkbox_box_color, activebackground=add_frame_color)
war_checkbox =  Checkbutton(select_category_frame, indicatoron=indic,text=" War", variable=war, width=checkbox_width, anchor=W, bg=add_frame_color, font=add_checkbox_font, fg="White", selectcolor=add_checkbox_box_color, activebackground=add_frame_color)
history_checkbox =  Checkbutton(select_category_frame,indicatoron=indic, text=" History", variable=history, width=checkbox_width, anchor=W, bg=add_frame_color, font=add_checkbox_font, fg="White", selectcolor=add_checkbox_box_color, activebackground=add_frame_color)
biography_checkbox =  Checkbutton(select_category_frame, indicatoron=indic,text=" Biography", variable=biography, width=checkbox_width, anchor=W, bg=add_frame_color, font=add_checkbox_font, fg="White", selectcolor=add_checkbox_box_color, activebackground=add_frame_color)

action_checkbox.bind("<Enter>", action_enter)
action_checkbox.bind("<Leave>", action_leave)
comedy_checkbox.bind("<Enter>", comedy_enter)
comedy_checkbox.bind("<Leave>", comedy_leave)
drama_checkbox.bind("<Enter>", drama_enter)
drama_checkbox.bind("<Leave>", drama_leave)
fantasy_checkbox.bind("<Enter>", fantasy_enter)
fantasy_checkbox.bind("<Leave>", fantasy_leave)
horror_checkbox.bind("<Enter>", horror_enter)
horror_checkbox.bind("<Leave>", horror_leave)
mystery_checkbox.bind("<Enter>", mystery_enter)
mystery_checkbox.bind("<Leave>", mystery_leave)
romance_checkbox.bind("<Enter>", romance_enter)
romance_checkbox.bind("<Leave>", romance_leave)
thriller_checkbox.bind("<Enter>", thriller_enter)
thriller_checkbox.bind("<Leave>", thriller_leave)
western_checkbox.bind("<Enter>", western_enter)
western_checkbox.bind("<Leave>", western_leave)
adventure_checkbox.bind("<Enter>", adventure_enter)
adventure_checkbox.bind("<Leave>", adventure_leave)
animation_checkbox.bind("<Enter>", animation_enter)
animation_checkbox.bind("<Leave>", animation_leave)
crime_checkbox.bind("<Enter>", crime_enter)
crime_checkbox.bind("<Leave>", crime_leave)
documentary_checkbox.bind("<Enter>", documentary_enter)
documentary_checkbox.bind("<Leave>", documentary_leave)
family_checkbox.bind("<Enter>", family_enter)
family_checkbox.bind("<Leave>", family_leave)
music_checkbox.bind("<Enter>", music_enter)
music_checkbox.bind("<Leave>", music_leave)
scifi_checkbox.bind("<Enter>", scifi_enter)
scifi_checkbox.bind("<Leave>", scifi_leave)
sport_checkbox.bind("<Enter>", sport_enter)
sport_checkbox.bind("<Leave>", sport_leave)
war_checkbox.bind("<Enter>", war_enter)
war_checkbox.bind("<Leave>", war_leave)
history_checkbox.bind("<Enter>", history_enter)
history_checkbox.bind("<Leave>", history_leave)
biography_checkbox.bind("<Enter>", biography_enter)
biography_checkbox.bind("<Leave>", biography_leave)

action_checkbox.grid(row=0, column=0, padx=2, pady=2)
comedy_checkbox.grid(row=0, column=4, padx=2, pady=2)
drama_checkbox.grid(row=1, column=2, padx=2, pady=2)
fantasy_checkbox.grid(row=1, column=4, padx=2, pady=2)
horror_checkbox.grid(row=2, column=0, padx=2, pady=2)
mystery_checkbox.grid(row=2, column=2, padx=2, pady=2)
romance_checkbox.grid(row=2, column=4, padx=2, pady=2)
thriller_checkbox.grid(row=3, column=2, padx=2, pady=2)
western_checkbox.grid(row=3, column=4, padx=2, pady=2)
adventure_checkbox.grid(row=0, column=1, padx=2, pady=2)
animation_checkbox.grid(row=0, column=2, padx=2, pady=2)
crime_checkbox.grid(row=1, column=0, padx=2, pady=2)
documentary_checkbox.grid(row=1, column=1, padx=2, pady=2)
family_checkbox.grid(row=1, column=3, padx=2, pady=2)
music_checkbox.grid(row=2, column=3, padx=2, pady=2)
scifi_checkbox.grid(row=3, column=0, padx=2, pady=2)
sport_checkbox.grid(row=3, column=1, padx=2, pady=2)
war_checkbox.grid(row=3, column=3, padx=2, pady=2)
history_checkbox.grid(row=2, column=1, padx=2, pady=2)
biography_checkbox.grid(row=0, column=3, padx=2, pady=2)

scrollbar.config(command=display_film_list.yview)

conn.close()
mainloop()