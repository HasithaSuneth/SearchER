import os
import glob
import sqlite3
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from PIL import ImageTk,Image
from operator import itemgetter
from tkinter import ttk

select_category_list = []
select_category_list2 = []
collection_list_search = []
movies_collection_list = []
searchbox = 0
search_category = 0
search_collection = 0
show_menu_state = 'minimize'

# Display
root = Tk()
root.title('SearchER - FILM CATEGORY DATABASE')
root.resizable(False, False)
root.iconbitmap('data/image/icon.ico')
#root.geometry("800x600")

conn = sqlite3.connect('data/Database/film_categories.db')
c = conn.cursor()

def statue_searched_category():
	user_select_funtion()
	print_searched_statue = ''
	if select_category_list[1]==1:
		print_searched_statue += "Action, "
	if select_category_list[2]==1:
		print_searched_statue += "Comedy, "
	if select_category_list[3]==1:
		print_searched_statue += "Drama, "
	if select_category_list[4]==1:
		print_searched_statue += "Fantasy, "
	if select_category_list[5]==1:
		print_searched_statue += "Horror, "
	if select_category_list[6]==1:
		print_searched_statue += "Mystery, "
	if select_category_list[7]==1:
		print_searched_statue += "Romance, "
	if select_category_list[8]==1:
		print_searched_statue += "Thriller, "
	if select_category_list[9]==1:
		print_searched_statue += "Western, "
	if select_category_list[10]==1:
		print_searched_statue += "Adventure, "
	if select_category_list[11]==1:
		print_searched_statue += "Animation, "
	if select_category_list[12]==1:
		print_searched_statue += "Crime, "
	if select_category_list[13]==1:
		print_searched_statue += "Documentary, "
	if select_category_list[14]==1:
		print_searched_statue += "Family, "
	if select_category_list[15]==1:
		print_searched_statue += "Music, "
	if select_category_list[16]==1:
		print_searched_statue += "Sci-Fi, "
	if select_category_list[17]==1:
		print_searched_statue += "Sport, "
	if select_category_list[18]==1:
		print_searched_statue += "War, "
	if select_category_list[19]==1:
		print_searched_statue += "History, "
	if select_category_list[20]==1:
		print_searched_statue += "Biography, "
	if csr.get()==1:
		print_searched_statue = print_searched_statue[:len(print_searched_statue)-2] + print_searched_statue[len(print_searched_statue)-1:]
		print_searched_statue += " (Combined Result) ("+ str(language_search.get()) + ")"
	else:
		print_searched_statue = print_searched_statue[:len(print_searched_statue)-2] + print_searched_statue[len(print_searched_statue)-1:]
		print_searched_statue += " (Non Combined Result) ("+ str(language_search.get()) + ")"
	statue_label_search.config(text="Filtered: "+ print_searched_statue, anchor=W)

def user_select_funtion():
	select_category_list.insert(0, language_search.get())
	if ac.get()==1:
		select_category_list.insert(1, 1)
	else:
		select_category_list.insert(1, 0)
	if co.get()==1:
		select_category_list.insert(2, 1)
	else:
		select_category_list.insert(2, 0)
	if dr.get()==1:
		select_category_list.insert(3, 1)
	else:
		select_category_list.insert(3, 0)
	if fa.get()==1:
		select_category_list.insert(4, 1)
	else:
		select_category_list.insert(4, 0)
	if ho.get()==1:
		select_category_list.insert(5, 1)
	else:
		select_category_list.insert(5, 0)
	if my.get()==1:
		select_category_list.insert(6, 1)
	else:
		select_category_list.insert(6, 0)
	if ro.get()==1:
		select_category_list.insert(7, 1)
	else:
		select_category_list.insert(7, 0)
	if th.get()==1:
		select_category_list.insert(8, 1)
	else:
		select_category_list.insert(8, 0)
	if we.get()==1:
		select_category_list.insert(9, 1)
	else:
		select_category_list.insert(9, 0)
	if ad.get()==1:
		select_category_list.insert(10, 1)
	else:
		select_category_list.insert(10, 0)
	if an.get()==1:
		select_category_list.insert(11, 1)
	else:
		select_category_list.insert(11, 0)
	if cr.get()==1:
		select_category_list.insert(12, 1)
	else:
		select_category_list.insert(12, 0)
	if do.get()==1:
		select_category_list.insert(13, 1)
	else:
		select_category_list.insert(13, 0)
	if fam.get()==1:
		select_category_list.insert(14, 1)
	else:
		select_category_list.insert(14, 0)
	if mu.get()==1:
		select_category_list.insert(15, 1)
	else:
		select_category_list.insert(15, 0)
	if sc.get()==1:
		select_category_list.insert(16, 1)
	else:
		select_category_list.insert(16, 0)
	if sp.get()==1:
		select_category_list.insert(17, 1)
	else:
		select_category_list.insert(17, 0)
	if wa.get()==1:
		select_category_list.insert(18, 1)
	else:
		select_category_list.insert(18, 0)
	if hi.get()==1:
		select_category_list.insert(19, 1)
	else:
		select_category_list.insert(19, 0)
	if bi.get()==1:
		select_category_list.insert(20, 1)
	else:
		select_category_list.insert(20, 0)

# Search all language combined
def search_films():
	user_select_funtion()
	statue_searched_category()
	searchbox_entry.delete(0,END)
	global search_category
	global searchbox
	global search_collection
	global statue_label_search
	display_search_result.delete(0,END)
	select_category_list2=[]
	conn = sqlite3.connect('data/Database/film_categories.db')
	c = conn.cursor()
	c.execute("SELECT *, oid FROM categories")
	records = c.fetchall()
	
	if select_category_list[0]=='All':
		if itemgetter(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)(select_category_list) == (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0):
			statue_label_search.config(text="All Movies (All Languages) ", anchor=W)
			for remove in records:
				record_select = itemgetter(3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22)(remove)
				user_select = itemgetter(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)(select_category_list)
				select_category_list2.append(itemgetter(1,28)(remove))
				display_search_result.insert(END, ' '+ itemgetter(0)(remove))
	else:
		if itemgetter(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)(select_category_list) == (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0):
			statue_label_search.config(text="All Movies : "+str(select_category_list[0])+" (Language)", anchor=W)
			for remove in records:
				record_select = itemgetter(2)(remove)
				user_select = itemgetter(0)(select_category_list)
				if record_select == user_select:
					select_category_list2.append(itemgetter(1,28)(remove))
					display_search_result.insert(END," "+ itemgetter(0)(remove))

	if csr.get()==1:
		if select_category_list[0]=='All':
			if itemgetter(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)(select_category_list) != (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0):
				user_select = itemgetter(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)(select_category_list)
				t2 = []
				for x in range(len(user_select)):
					if user_select[x]==1:
						t2.append(x)
				for remove in records:
					record_select = itemgetter(3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22)(remove)
					rounds = 0
					for y in t2:
						if record_select[y]==1:
							rounds = rounds + 1
							if len(t2) == rounds:
								select_category_list2.append(itemgetter(1,28)(remove))
								display_search_result.insert(END, " "+itemgetter(0)(remove))	
		else:
			if itemgetter(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)(select_category_list) != (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0):
				user_select = itemgetter(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)(select_category_list)
				t2 = []
				for x in range(len(user_select)):
					if user_select[x]==1:
						t2.append(x)
				for remove in records:
					record_select = itemgetter(2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22)(remove)
					rounds = 0
					for y in t2:
						if record_select[y]==1:
							rounds = rounds + 1
							if len(t2) == rounds and user_select[0]==record_select[0]:
								select_category_list2.append(itemgetter(1,28)(remove))
								display_search_result.insert(END, " "+itemgetter(0)(remove))
	else:
		if select_category_list[0]=='All':
			if itemgetter(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)(select_category_list) != (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0):
				for remove in records:
					record_select = itemgetter(3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22)(remove)
					user_select = itemgetter(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)(select_category_list)
					if user_select[0]==1 and record_select[0]==1:
						select_category_list2.append(itemgetter(1,28)(remove))
						display_search_result.insert(END, " "+itemgetter(0)(remove))
					elif user_select[1]==1 and record_select[1]==1:
						select_category_list2.append(itemgetter(1,28)(remove))
						display_search_result.insert(END, " "+itemgetter(0)(remove))
					elif user_select[2]==1 and record_select[2]==1:
						select_category_list2.append(itemgetter(1,28)(remove))
						display_search_result.insert(END, " "+itemgetter(0)(remove))
					elif user_select[3]==1 and record_select[3]==1:
						select_category_list2.append(itemgetter(1,28)(remove))
						display_search_result.insert(END, " "+itemgetter(0)(remove))
					elif user_select[4]==1 and record_select[4]==1:
						select_category_list2.append(itemgetter(1,28)(remove))
						display_search_result.insert(END, " "+itemgetter(0)(remove))
					elif user_select[5]==1 and record_select[5]==1:
						select_category_list2.append(itemgetter(1,28)(remove))
						display_search_result.insert(END, " "+itemgetter(0)(remove))
					elif user_select[6]==1 and record_select[6]==1:
						select_category_list2.append(itemgetter(1,28)(remove))
						display_search_result.insert(END, " "+itemgetter(0)(remove))
					elif user_select[7]==1 and record_select[7]==1:
						select_category_list2.append(itemgetter(1,28)(remove))
						display_search_result.insert(END, " "+itemgetter(0)(remove))
					elif user_select[8]==1 and record_select[8]==1:
						select_category_list2.append(itemgetter(1,28)(remove))
						display_search_result.insert(END, " "+itemgetter(0)(remove))
					elif user_select[9]==1 and record_select[9]==1:
						select_category_list2.append(itemgetter(1,28)(remove))
						display_search_result.insert(END, " "+itemgetter(0)(remove))
					elif user_select[10]==1 and record_select[10]==1:
						select_category_list2.append(itemgetter(1,28)(remove))
						display_search_result.insert(END, " "+itemgetter(0)(remove))
					elif user_select[11]==1 and record_select[11]==1:
						select_category_list2.append(itemgetter(1,28)(remove))
						display_search_result.insert(END, " "+itemgetter(0)(remove))
					elif user_select[12]==1 and record_select[12]==1:
						select_category_list2.append(itemgetter(1,28)(remove))
						display_search_result.insert(END, " "+itemgetter(0)(remove))
					elif user_select[13]==1 and record_select[13]==1:
						select_category_list2.append(itemgetter(1,28)(remove))
						display_search_result.insert(END, " "+itemgetter(0)(remove))
					elif user_select[14]==1 and record_select[14]==1:
						select_category_list2.append(itemgetter(1,28)(remove))
						display_search_result.insert(END, " "+itemgetter(0)(remove))
					elif user_select[15]==1 and record_select[15]==1:
						select_category_list2.append(itemgetter(1,28)(remove))
						display_search_result.insert(END, " "+itemgetter(0)(remove))
					elif user_select[16]==1 and record_select[16]==1:
						select_category_list2.append(itemgetter(1,28)(remove))
						display_search_result.insert(END, " "+itemgetter(0)(remove))
					elif user_select[17]==1 and record_select[17]==1:
						select_category_list2.append(itemgetter(1,28)(remove))
						display_search_result.insert(END, " "+itemgetter(0)(remove))
					elif user_select[18]==1 and record_select[18]==1:
						select_category_list2.append(itemgetter(1,28)(remove))
						display_search_result.insert(END, " "+itemgetter(0)(remove))
					elif user_select[19]==1 and record_select[19]==1:
						select_category_list2.append(itemgetter(1,28)(remove))
						display_search_result.insert(END, " "+itemgetter(0)(remove))

		else:
			if itemgetter(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)(select_category_list) != (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0):
				for remove in records:
					record_select = itemgetter(2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22)(remove)
					user_select = itemgetter(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)(select_category_list)
					if user_select[0] == record_select[0]:
						if user_select[1]==1 and record_select[1]==1:
							select_category_list2.append(itemgetter(1,28)(remove))
							display_search_result.insert(END, " "+itemgetter(0)(remove))
						elif user_select[2]==1 and record_select[2]==1:
							select_category_list2.append(itemgetter(1,28)(remove))
							display_search_result.insert(END, " "+itemgetter(0)(remove))
						elif user_select[3]==1 and record_select[3]==1:
							select_category_list2.append(itemgetter(1,28)(remove))
							display_search_result.insert(END, " "+itemgetter(0)(remove))
						elif user_select[4]==1 and record_select[4]==1:
							select_category_list2.append(itemgetter(1,28)(remove))
							display_search_result.insert(END, " "+itemgetter(0)(remove))
						elif user_select[5]==1 and record_select[5]==1:
							select_category_list2.append(itemgetter(1,28)(remove))
							display_search_result.insert(END, " "+itemgetter(0)(remove))
						elif user_select[6]==1 and record_select[6]==1:
							select_category_list2.append(itemgetter(1,28)(remove))
							display_search_result.insert(END, " "+itemgetter(0)(remove))
						elif user_select[7]==1 and record_select[7]==1:
							select_category_list2.append(itemgetter(1,28)(remove))
							display_search_result.insert(END, " "+itemgetter(0)(remove))
						elif user_select[8]==1 and record_select[8]==1:
							select_category_list2.append(itemgetter(1,28)(remove))
							display_search_result.insert(END, " "+itemgetter(0)(remove))
						elif user_select[9]==1 and record_select[9]==1:
							select_category_list2.append(itemgetter(1,28)(remove))
							display_search_result.insert(END, " "+itemgetter(0)(remove))
						elif user_select[10]==1 and record_select[10]==1:
							select_category_list2.append(itemgetter(1,28)(remove))
							display_search_result.insert(END, " "+itemgetter(0)(remove))
						elif user_select[11]==1 and record_select[11]==1:
							select_category_list2.append(itemgetter(1,28)(remove))
							display_search_result.insert(END, " "+itemgetter(0)(remove))
						elif user_select[12]==1 and record_select[12]==1:
							select_category_list2.append(itemgetter(1,28)(remove))
							display_search_result.insert(END, " "+itemgetter(0)(remove))
						elif user_select[13]==1 and record_select[13]==1:
							select_category_list2.append(itemgetter(1,28)(remove))
							display_search_result.insert(END, " "+itemgetter(0)(remove))
						elif user_select[14]==1 and record_select[14]==1:
							select_category_list2.append(itemgetter(1,28)(remove))
							display_search_result.insert(END, " "+itemgetter(0)(remove))
						elif user_select[15]==1 and record_select[15]==1:
							select_category_list2.append(itemgetter(1,28)(remove))
							display_search_result.insert(END, " "+itemgetter(0)(remove))
						elif user_select[16]==1 and record_select[16]==1:
							select_category_list2.append(itemgetter(1,28)(remove))
							display_search_result.insert(END, " "+itemgetter(0)(remove))
						elif user_select[17]==1 and record_select[17]==1:
							select_category_list2.append(itemgetter(1,28)(remove))
							display_search_result.insert(END, " "+itemgetter(0)(remove))
						elif user_select[18]==1 and record_select[18]==1:
							select_category_list2.append(itemgetter(1,28)(remove))
							display_search_result.insert(END, " "+itemgetter(0)(remove))
						elif user_select[19]==1 and record_select[19]==1:
							select_category_list2.append(itemgetter(1,28)(remove))
							display_search_result.insert(END, " "+itemgetter(0)(remove))
	conn.commit()
	conn.close()
	search_category=1
	searchbox=0
	search_collection=0
	collection_menu.set('Movie Collection')
	if select_category_list2 == []:
		open_film_button["state"]= "disabled"
	else:
		open_film_button["state"]= "normal"
	return select_category_list2

def searchbox_funtion(event=None):
	display_search_result.delete(0,END)
	select_category_list2=[]
	global searchbox
	global search_category
	global search_collection
	searchbox_value = str(searchbox_entry.get())
	conn = sqlite3.connect('data/Database/film_categories.db')
	c = conn.cursor()
	if searchbox_value == "":
		messagebox.showinfo("Search Error","     Searchbox can't be empty ! \n Please ENTER film name to search")
	else:
		c.execute("SELECT *, oid FROM categories WHERE film_name like '%'||?||'%'",(searchbox_value,))
		search_record = c.fetchall()
		for search in search_record:
			display_search_result.insert(END, " "+itemgetter(0)(search))
			select_category_list2.append(itemgetter(1,28)(search))
	conn.commit()
	conn.close()
	searchbox=1
	search_category=0
	search_collection=0
	collection_menu.set('Movie Collection')
	checkbox_reset()
	statue_label_search.config(text="Searched: keyword - '"+ str(searchbox_entry.get())+"'", anchor=W)
	if searchbox_value == "":
		open_film_button["state"]= "disabled"
	else:
		open_film_button["state"]= "normal"
	return select_category_list2

def movie_collection(event):
	global search_category
	global searchbox
	global search_collection
	movies_collection_list.clear()
	display_search_result.delete(0, END)
	if collection_menu.get() != "None":
		conn = sqlite3.connect('data/Database/film_categories.db')
		c = conn.cursor()
		c.execute("SELECT *, oid FROM categories WHERE collection1 like '%'||?||'%'",(collection_menu.get(),))
		search_slot1 = c.fetchall()
		c.execute("SELECT *, oid FROM categories WHERE collection2 like '%'||?||'%'",(collection_menu.get(),))
		search_slot2 = c.fetchall()
		c.execute("SELECT *, oid FROM categories WHERE collection3 like '%'||?||'%'",(collection_menu.get(),))
		search_slot3 = c.fetchall()
		c.execute("SELECT *, oid FROM categories WHERE collection4 like '%'||?||'%'",(collection_menu.get(),))
		search_slot4 = c.fetchall()
		c.execute("SELECT *, oid FROM categories WHERE collection5 like '%'||?||'%'",(collection_menu.get(),))
		search_slot5 = c.fetchall()

		if search_slot1 != []:
			for search in search_slot1:
				movies_collection_list.append(itemgetter(1,28)(search))
				display_search_result.insert(END, " "+itemgetter(0)(search))
				
		if search_slot2 != []:
			for search in search_slot2:
				movies_collection_list.append(itemgetter(1,28)(search))
				display_search_result.insert(END, " "+itemgetter(0)(search))
				
		if search_slot3 != []:
			for search in search_slot3:
				movies_collection_list.append(itemgetter(1,28)(search))
				display_search_result.insert(END, " "+itemgetter(0)(search))
				
		if search_slot4 != []:
			for search in search_slot4:
				movies_collection_list.append(itemgetter(1,28)(search))
				display_search_result.insert(END, " "+itemgetter(0)(search))
				
		if search_slot5 != []:
			for search in search_slot5:
				movies_collection_list.append(itemgetter(1,28)(search))
				display_search_result.insert(END, " "+itemgetter(0)(search))		
		conn.commit()
		conn.close()
	searchbox_entry.delete(0,END)
	checkbox_reset()
	searchbox=0
	search_category=0
	search_collection=1
	if collection_menu.get() == "None":
		statue_label_search.config(text="Collection List Empty. ", anchor=W)
	else:
		statue_label_search.config(text="Selected Collection: "+ str(collection_menu.get()), anchor=W)	
	if movies_collection_list == []:
		open_film_button["state"]= "disabled"
	else:
		open_film_button["state"]= "normal"
	return movies_collection_list

def open_film_funtion():
	try:
		selected_search_film = display_search_result.curselection()[0]
		if searchbox == 1:
			selected_searched_film = searchbox_funtion()
		if search_category == 1:
			selected_searched_film = search_films()
		if search_collection == 1:
			selected_searched_film = movie_collection(1)
		os.startfile(selected_searched_film[selected_search_film][0])
		display_search_result.yview(selected_search_film)
		display_search_result.selection_set(selected_search_film)
	except OSError:
		messagebox.showerror("Movie Loading Error","Movie Path Changed or Removed.")
	except IndexError:
		messagebox.showerror("Movie Loading Error","Didn't SELECT a Movie to Load.")
	
def prep(event):
	messagebox.showinfo("About"," Contact : Hasitha Suneth \n Email : hasisuneth@gmail.com \n Blog : hasisuneth.blogspot.com")

def collection_names():
	collection_names = open("data/TXT/Collections.txt","r")
	collection_list_search.clear()
	for line in collection_names:
		stripped_line = line.strip()
		collection_list_search.append(stripped_line)
	return collection_list_search

def checkbox_reset():
	action_checkbox_search.deselect()
	comedy_checkbox_search.deselect()
	drama_checkbox_search.deselect()
	fantasy_checkbox_search.deselect()
	horror_checkbox_search.deselect()
	mystery_checkbox_search.deselect()
	romance_checkbox_search.deselect()
	thriller_checkbox_search.deselect()
	adventure_checkbox_search.deselect()
	animation_checkbox_search.deselect()
	crime_checkbox_search.deselect()
	documentary_checkbox_search.deselect()
	family_checkbox_search.deselect()
	music_checkbox_search.deselect()
	scifi_checkbox_search.deselect()
	sport_checkbox_search.deselect()
	war_checkbox_search.deselect()
	history_checkbox_search.deselect()
	biography_checkbox_search.deselect()
	combine_checkbox_search.deselect()
	language_search.set('All')

def show_category(event):
	global show_menu_state
	if show_menu_state == 'minimize':
		All_searchbar_frame.grid(row=2, column=0,sticky=W+E+S+N)
		show_menu_state = 'maximize'
	else:
		All_searchbar_frame.grid_forget()
		show_menu_state = 'minimize'

def action_enter(event):
	action_checkbox_search.config(selectcolor=add_checkbox_box_enter_color)
	action_checkbox_search.config(bg=add_checkbox_box_enter_color)
def action_leave(event):
	action_checkbox_search.config(selectcolor=frame_bg_color)
	action_checkbox_search.config(bg=checkbox_bg_color)
def comedy_enter(event):
	comedy_checkbox_search.config(selectcolor=add_checkbox_box_enter_color)
	comedy_checkbox_search.config(bg=add_checkbox_box_enter_color)
def comedy_leave(event):
	comedy_checkbox_search.config(selectcolor=frame_bg_color)
	comedy_checkbox_search.config(bg=checkbox_bg_color)
def drama_enter(event):
	drama_checkbox_search.config(selectcolor=add_checkbox_box_enter_color)
	drama_checkbox_search.config(bg=add_checkbox_box_enter_color)
def drama_leave(event):
	drama_checkbox_search.config(selectcolor=frame_bg_color)
	drama_checkbox_search.config(bg=checkbox_bg_color)
def fantasy_enter(event):
	fantasy_checkbox_search.config(selectcolor=add_checkbox_box_enter_color)
	fantasy_checkbox_search.config(bg=add_checkbox_box_enter_color)
def fantasy_leave(event):
	fantasy_checkbox_search.config(selectcolor=frame_bg_color)
	fantasy_checkbox_search.config(bg=checkbox_bg_color)
def horror_enter(event):
	horror_checkbox_search.config(selectcolor=add_checkbox_box_enter_color)
	horror_checkbox_search.config(bg=add_checkbox_box_enter_color)
def horror_leave(event):
	horror_checkbox_search.config(selectcolor=frame_bg_color)
	horror_checkbox_search.config(bg=checkbox_bg_color)
def mystery_enter(event):
	mystery_checkbox_search.config(selectcolor=add_checkbox_box_enter_color)
	mystery_checkbox_search.config(bg=add_checkbox_box_enter_color)
def mystery_leave(event):
	mystery_checkbox_search.config(selectcolor=frame_bg_color)
	mystery_checkbox_search.config(bg=checkbox_bg_color)
def romance_enter(event):
	romance_checkbox_search.config(selectcolor=add_checkbox_box_enter_color)
	romance_checkbox_search.config(bg=add_checkbox_box_enter_color)
def romance_leave(event):
	romance_checkbox_search.config(selectcolor=frame_bg_color)
	romance_checkbox_search.config(bg=checkbox_bg_color)
def thriller_enter(event):
	thriller_checkbox_search.config(selectcolor=add_checkbox_box_enter_color)
	thriller_checkbox_search.config(bg=add_checkbox_box_enter_color)
def thriller_leave(event):
	thriller_checkbox_search.config(selectcolor=frame_bg_color)
	thriller_checkbox_search.config(bg=checkbox_bg_color)
def western_enter(event):
	western_checkbox_search.config(selectcolor=add_checkbox_box_enter_color)
	western_checkbox_search.config(bg=add_checkbox_box_enter_color)
def western_leave(event):
	western_checkbox_search.config(selectcolor=frame_bg_color)
	western_checkbox_search.config(bg=checkbox_bg_color)
def adventure_enter(event):
	adventure_checkbox_search.config(selectcolor=add_checkbox_box_enter_color)
	adventure_checkbox_search.config(bg=add_checkbox_box_enter_color)
def adventure_leave(event):
	adventure_checkbox_search.config(selectcolor=frame_bg_color)
	adventure_checkbox_search.config(bg=checkbox_bg_color)
def animation_enter(event):
	animation_checkbox_search.config(selectcolor=add_checkbox_box_enter_color)
	animation_checkbox_search.config(bg=add_checkbox_box_enter_color)
def animation_leave(event):
	animation_checkbox_search.config(selectcolor=frame_bg_color)
	animation_checkbox_search.config(bg=checkbox_bg_color)
def crime_enter(event):
	crime_checkbox_search.config(selectcolor=add_checkbox_box_enter_color)
	crime_checkbox_search.config(bg=add_checkbox_box_enter_color)
def crime_leave(event):
	crime_checkbox_search.config(selectcolor=frame_bg_color)
	crime_checkbox_search.config(bg=checkbox_bg_color)
def documentary_enter(event):
	documentary_checkbox_search.config(selectcolor=add_checkbox_box_enter_color)
	documentary_checkbox_search.config(bg=add_checkbox_box_enter_color)
def documentary_leave(event):
	documentary_checkbox_search.config(selectcolor=frame_bg_color)
	documentary_checkbox_search.config(bg=checkbox_bg_color)
def family_enter(event):
	family_checkbox_search.config(selectcolor=add_checkbox_box_enter_color)
	family_checkbox_search.config(bg=add_checkbox_box_enter_color)
def family_leave(event):
	family_checkbox_search.config(selectcolor=frame_bg_color)
	family_checkbox_search.config(bg=checkbox_bg_color)
def music_enter(event):
	music_checkbox_search.config(selectcolor=add_checkbox_box_enter_color)
	music_checkbox_search.config(bg=add_checkbox_box_enter_color)
def music_leave(event):
	music_checkbox_search.config(selectcolor=frame_bg_color)
	music_checkbox_search.config(bg=checkbox_bg_color)
def scifi_enter(event):
	scifi_checkbox_search.config(selectcolor=add_checkbox_box_enter_color)
	scifi_checkbox_search.config(bg=add_checkbox_box_enter_color)
def scifi_leave(event):
	scifi_checkbox_search.config(selectcolor=frame_bg_color)
	scifi_checkbox_search.config(bg=checkbox_bg_color)
def sport_enter(event):
	sport_checkbox_search.config(selectcolor=add_checkbox_box_enter_color)
	sport_checkbox_search.config(bg=add_checkbox_box_enter_color)
def sport_leave(event):
	sport_checkbox_search.config(selectcolor=frame_bg_color)
	sport_checkbox_search.config(bg=checkbox_bg_color)
def war_enter(event):
	war_checkbox_search.config(selectcolor=add_checkbox_box_enter_color)
	war_checkbox_search.config(bg=add_checkbox_box_enter_color)
def war_leave(event):
	war_checkbox_search.config(selectcolor=frame_bg_color)
	war_checkbox_search.config(bg=checkbox_bg_color)
def history_enter(event):
	history_checkbox_search.config(selectcolor=add_checkbox_box_enter_color)
	history_checkbox_search.config(bg=add_checkbox_box_enter_color)
def history_leave(event):
	history_checkbox_search.config(selectcolor=frame_bg_color)
	history_checkbox_search.config(bg=checkbox_bg_color)
def biography_enter(event):
	biography_checkbox_search.config(selectcolor=add_checkbox_box_enter_color)
	biography_checkbox_search.config(bg=add_checkbox_box_enter_color)
def biography_leave(event):
	biography_checkbox_search.config(selectcolor=frame_bg_color)
	biography_checkbox_search.config(bg=checkbox_bg_color)
def category_show_enter(event):
	if show_menu_state == 'minimize':
		category_show_label.config(image=collection_show_img_enter)
	if show_menu_state == 'maximize':
		category_show_label.config(image=collection_show_img_enter)	
def category_show_leave(event):
	if show_menu_state == 'minimize':
		category_show_label.config(image=collection_show_img)
	if show_menu_state == 'maximize':
		category_show_label.config(image=collection_show_img_maxi)
def noncombine_show_enter(event):
	noncombine_label.config(image=noncombined_img_enter)
def noncombine_show_leave(event):
	if csr.get()==1:
		noncombine_label.config(image=noncombined_img_leave)
	else:
		noncombine_label.config(image=noncombined_img)	
def combine_show_enter(event):
	combine_label.config(image=combined_img_enter)
def combine_show_leave(event):
	if csr.get()==1:
		combine_label.config(image=combined_img)
	else:
		combine_label.config(image=combined_img_leave)	
def searchbox_enter(event):
	searchbox_button.config(image=searchbox_img_enter)
def searchbox_leave(event):
	searchbox_button.config(image=searchbox_img)
def movie_collection_enter(event):
	movie_collection_label.config(image=movie_collection_img_enter)
def movie_collection_leave(event):
	movie_collection_label.config(image=movie_collection_img)
def filter_enter(event):
	search_button.config(image=filter_img_enter)
def filter_leave(event):
	search_button.config(image=filter_img)
def load_enter(event):
	open_film_button.config(image=load_img_enter)
def load_leave(event):
	open_film_button.config(image=load_img)
def combined_show(event):
	combine_checkbox_search.select()
	combine_label.config(image=combined_img)
	noncombine_label.config(image=noncombined_img_leave)
def noncombined_show(event):
	combine_checkbox_search.deselect()
	noncombine_label.config(image=noncombined_img)
	combine_label.config(image=combined_img_leave)

collection_show_img = ImageTk.PhotoImage(Image.open("data/image/collection_show_button.jpg"))
collection_show_img_enter = ImageTk.PhotoImage(Image.open("data/image/collection_show_button_enter.jpg"))
collection_show_img_maxi = ImageTk.PhotoImage(Image.open("data/image/collection_show_button_maxi.jpg"))
noncombined_img = ImageTk.PhotoImage(Image.open("data/image/noncombine_button.jpg"))
noncombined_img_leave = ImageTk.PhotoImage(Image.open("data/image/noncombine_button_leave.jpg"))
noncombined_img_enter = ImageTk.PhotoImage(Image.open("data/image/noncombine_button_enter.jpg"))
combined_img = ImageTk.PhotoImage(Image.open("data/image/combine_button.jpg"))
combined_img_leave = ImageTk.PhotoImage(Image.open("data/image/combine_button_leave.jpg"))
combined_img_enter = ImageTk.PhotoImage(Image.open("data/image/combine_button_enter.jpg"))
searchbox_img = ImageTk.PhotoImage(Image.open("data/image/searchbox_button.jpg"))
searchbox_img_enter = ImageTk.PhotoImage(Image.open("data/image/searchbox_button_enter.jpg"))
movie_collection_img = ImageTk.PhotoImage(Image.open("data/image/movie_collection_button.jpg"))
movie_collection_img_enter = ImageTk.PhotoImage(Image.open("data/image/movie_collection_button_enter.jpg"))
filter_img = ImageTk.PhotoImage(Image.open("data/image/filter_button.jpg"))
filter_img_enter = ImageTk.PhotoImage(Image.open("data/image/filter_button_enter.jpg"))
load_img = ImageTk.PhotoImage(Image.open("data/image/load_button.jpg"))
load_img_enter = ImageTk.PhotoImage(Image.open("data/image/load_button_enter.jpg"))

checkbox_font = "Comic Sans MS", "9", "bold"
frame_bg_color = "#2c4c66" 
checkbox_bg_color = "#424242"
checkbox_fg_color = "White" 
checkbox_box_color = "#2c4c66"
add_checkbox_box_enter_color = "#2c4c66"

# Frams
All_searchbar_frame = LabelFrame(root, bg='#424242',bd=0)
searchbar_frame = LabelFrame(All_searchbar_frame, bg='#424242', relief='flat')
category_type_frame = LabelFrame(All_searchbar_frame, bg='#424242',bd=0)
search_result_frame = LabelFrame(root, padx=5, pady=5, bg='#424242', relief='flat')
open_film_frame = LabelFrame(root, padx=5, pady=5, bg='#424242', relief='flat')
searchbox_frame = LabelFrame(root, padx=5, pady=5, bg='#424242', relief='flat')
category_show_frame = LabelFrame(root, padx=3, bg='#424242',bd=0)
statue_label_frame = LabelFrame(root, bg='#424242',bd=0)
#All_searchbar_frame.grid(row=2, column=0,sticky=W+E)
category_type_frame.grid(row=0, column=0,sticky=W+E+S+N)
searchbar_frame.grid(row=1, column=0,sticky=W+E, padx=(4,0),pady=(4,0))
searchbox_frame.grid(row=0, column=0,sticky=W+E)
category_show_frame.grid(row=1, column=0,sticky=W+E+S+N)
search_result_frame.grid(row=3, column=0,sticky=W+E)
open_film_frame.grid(row=4, column=0,sticky=W+E)
statue_label_frame.grid(row=5, column=0,sticky=W+E)

# Buttons
search_button = Button(searchbar_frame, text="Search & Filter",image=filter_img, width=130, height=30, command=search_films, bg="white", activebackground ="#2c4c66", font=("Comic", "10", "bold"), fg="white", relief="flat")
open_film_button = Button(open_film_frame, text="Load Movie",image=load_img,  width=130, height=30, command=open_film_funtion, bg="#8593a4", activebackground ="#2c4c66", font=("Comic", "10", "bold"), fg="#10488d", relief="flat")
searchbox_button = Button(searchbox_frame, text="Search Movie", image=searchbox_img, width=104, height=16, command=searchbox_funtion, bg="#8593a4", activebackground ="#2c4c66", font=("Comic", "10", "bold"), fg="#10488d", relief="flat")
search_button.grid(row=2, column=6,  rowspan=2, sticky=W, padx=(20,0))
searchbox_button.pack(side=RIGHT, padx=(5,0))
open_film_button.pack(side=RIGHT, fill=BOTH, padx=(0,25)) 
open_film_button["state"]= "disabled"
searchbox_button.bind('<Enter>', searchbox_enter)
searchbox_button.bind('<Leave>', searchbox_leave)
search_button.bind('<Enter>', filter_enter)
search_button.bind('<Leave>', filter_leave)
open_film_button.bind('<Enter>', load_enter)
open_film_button.bind('<Leave>', load_leave)

# Scrollbar
scrollbar_search = Scrollbar(search_result_frame, bg="Black")
scrollbar_search.pack(side=RIGHT, fill=Y)

# Listbox
display_search_result = Listbox(search_result_frame,  yscrollcommand=scrollbar_search.set, relief='flat', width=100, height=15, bg="#424949", fg="White", font=("Helvetica", "9"), selectbackground="#408f9b")
display_search_result.pack(side=LEFT, fill=BOTH)
scrollbar_search.config(command=display_search_result.yview)

# Label
language_label_search = Label(searchbar_frame, text="Language", font=("Verdana", "8",), fg="white", bg='#424242')
statue_label_search = Label(statue_label_frame, text="Statue", padx=5, bd=2, anchor=E, bg='#424242', fg="White",width=103)
about_search = Label(root, text="Created by Hasitha Suneth", padx=5, bg='#515A5A', fg="white", relief="flat",font=("Comic Sans MS", "8", "italic"))
category_show_label = Label(category_show_frame, text="Categories", image=collection_show_img, width=360, height=28, bg='#424242', fg="White",bd=0)
combine_label = Label(category_type_frame, text="Combined Result", image=combined_img_leave, width=180, height=26, bg='#515A5A', fg="White",bd=0)
noncombine_label = Label(category_type_frame, text="Non Combined",image=noncombined_img, width=180, height=26, bg='#424242', fg="White",bd=0)
movie_collection_label = Label(category_show_frame, text="Non Combined",image=movie_collection_img, width=360, height=28, bg='#424242', fg="White",bd=0)
language_label_search.grid(row=0, column=6)
statue_label_search.pack( side=RIGHT, fill=BOTH)
about_search.grid(row=6, column=0, columnspan=2, sticky=W+E)
about_search.bind('<Button-1>', prep)
category_show_label.grid(row=0, column=0,padx=(5,0))
combine_label.grid(row=0, column=1)
noncombine_label.grid(row=0, column=0, padx=(8,0))
movie_collection_label.grid(row=0, column=1)
category_show_label.bind('<Button-1>', show_category)
combine_label.bind('<Button-1>', combined_show)
noncombine_label.bind('<Button-1>', noncombined_show)
category_show_label.bind('<Enter>', category_show_enter)
category_show_label.bind('<Leave>', category_show_leave)
noncombine_label.bind('<Enter>', noncombine_show_enter)
noncombine_label.bind('<Leave>', noncombine_show_leave)
combine_label.bind('<Enter>', combine_show_enter)
combine_label.bind('<Leave>', combine_show_leave)

collection_menu = StringVar()
try:
	collection_combobox_search = OptionMenu(category_show_frame, collection_menu, *collection_names(), command=movie_collection)
except:
	collection_combobox_search = OptionMenu(category_show_frame, collection_menu, "None", command=movie_collection)

collection_combobox_search.config(width=50, bg='#424242', font=("times","9","bold"),activebackground="#294b55",activeforeground="white",fg='white',bd=1,highlightthickness=0, relief='flat')
collection_combobox_search["menu"].config(bg="#424242", font=("times","9","bold "), fg="White", activebackground="#2c4c66")
collection_combobox_search.grid(row=0, column=1, padx=(16,0))
collection_menu.set('Movie Collection')
collection_combobox_search.bind('<Enter>',movie_collection_enter)
collection_combobox_search.bind('<Leave>',movie_collection_leave)

# Entry
searchbox_entry = Entry(searchbox_frame, width=30, borderwidth=3, bg="#515A5A", relief="flat", fg="white", font=("Verdana","8","bold"))
searchbox_entry.pack(side=RIGHT)
searchbox_entry.bind('<Return>',searchbox_funtion)

# Tkinter veriable
ac = IntVar() 
co = IntVar()
dr = IntVar()
fa = IntVar()
ho = IntVar()
my = IntVar()
ro = IntVar()
th = IntVar()
we = IntVar()
ad = IntVar()
an = IntVar()
cr = IntVar()
do = IntVar()
fam = IntVar()
mu = IntVar()
sc = IntVar()
sp = IntVar()
wa = IntVar()
hi = IntVar()
bi = IntVar()
csr = IntVar()
language_search = StringVar()
language_option_search = ['All','English','Sinhala','French','Hindi','Tamil','Malayalam','Telugu','Kannada','Korean','Japanese','Spanish','Thai','German','Italian','Chinese','Russian']

# Dropbox
language_box_search = OptionMenu(searchbar_frame, language_search, *language_option_search)
language_box_search.config(width=16, bg="#424242", font=("Times","9","bold"), activebackground="#2c4c66",activeforeground="white",bd=1,highlightthickness=0,fg='white')
language_box_search["menu"].config(bg="#424242", font=("time","9","bold "), fg="White",activebackground="#2c4c66")
language_box_search.grid(row=1, column=6, padx=(20,25))
language_search.set('All')

# Checkbox
action_checkbox_search =  Checkbutton(searchbar_frame, text=" Action",indicatoron=0, variable=ac, width=13, anchor=W, font=checkbox_font, fg=checkbox_fg_color, bg=checkbox_bg_color, selectcolor=checkbox_box_color, activebackground=checkbox_bg_color)
comedy_checkbox_search =  Checkbutton(searchbar_frame, text=" Comedy",indicatoron=0,variable=co, width=13, anchor=W, font=checkbox_font, fg=checkbox_fg_color, bg=checkbox_bg_color, selectcolor=checkbox_box_color, activebackground=checkbox_bg_color)
drama_checkbox_search =  Checkbutton(searchbar_frame, text=" Drama",indicatoron=0, variable=dr, width=13, anchor=W, font=checkbox_font, fg=checkbox_fg_color, bg=checkbox_bg_color, selectcolor=checkbox_box_color, activebackground=checkbox_bg_color)
fantasy_checkbox_search =  Checkbutton(searchbar_frame, text=" Fantasy",indicatoron=0, variable=fa, width=13, anchor=W, font=checkbox_font, fg=checkbox_fg_color, bg=checkbox_bg_color, selectcolor=checkbox_box_color, activebackground=checkbox_bg_color)
horror_checkbox_search =  Checkbutton(searchbar_frame, text=" Horror",indicatoron=0, variable=ho, width=13, anchor=W, font=checkbox_font, fg=checkbox_fg_color, bg=checkbox_bg_color, selectcolor=checkbox_box_color, activebackground=checkbox_bg_color)
mystery_checkbox_search =  Checkbutton(searchbar_frame, text=" Mystery",indicatoron=0, variable=my, width=13, anchor=W, font=checkbox_font, fg=checkbox_fg_color, bg=checkbox_bg_color, selectcolor=checkbox_box_color, activebackground=checkbox_bg_color)
romance_checkbox_search =  Checkbutton(searchbar_frame, text=" Romance",indicatoron=0, variable=ro, width=13, anchor=W, font=checkbox_font, fg=checkbox_fg_color, bg=checkbox_bg_color, selectcolor=checkbox_box_color, activebackground=checkbox_bg_color)
thriller_checkbox_search =  Checkbutton(searchbar_frame, text=" Thriller",indicatoron=0, variable=th, width=13, anchor=W, font=checkbox_font, fg=checkbox_fg_color, bg=checkbox_bg_color, selectcolor=checkbox_box_color, activebackground=checkbox_bg_color)
western_checkbox_search =  Checkbutton(searchbar_frame, text=" Western",indicatoron=0, variable=we, width=13, anchor=W, font=checkbox_font, fg=checkbox_fg_color, bg=checkbox_bg_color, selectcolor=checkbox_box_color, activebackground=checkbox_bg_color)
adventure_checkbox_search =  Checkbutton(searchbar_frame, text=" Adventure",indicatoron=0, variable=ad, width=13, anchor=W, font=checkbox_font, fg=checkbox_fg_color, bg=checkbox_bg_color, selectcolor=checkbox_box_color, activebackground=checkbox_bg_color)
animation_checkbox_search =  Checkbutton(searchbar_frame, text=" Animation",indicatoron=0, variable=an, width=13, anchor=W, font=checkbox_font, fg=checkbox_fg_color, bg=checkbox_bg_color, selectcolor=checkbox_box_color, activebackground=checkbox_bg_color)
crime_checkbox_search =  Checkbutton(searchbar_frame, text=" Crime",indicatoron=0, variable=cr, width=13, anchor=W, font=checkbox_font, fg=checkbox_fg_color, bg=checkbox_bg_color, selectcolor=checkbox_box_color, activebackground=checkbox_bg_color)
documentary_checkbox_search =  Checkbutton(searchbar_frame, text=" Documentary",indicatoron=0, variable=do, width=13, anchor=W, font=checkbox_font, fg=checkbox_fg_color, bg=checkbox_bg_color, selectcolor=checkbox_box_color, activebackground=checkbox_bg_color)
family_checkbox_search =  Checkbutton(searchbar_frame, text=" Family",indicatoron=0, variable=fam, width=13, anchor=W, font=checkbox_font, fg=checkbox_fg_color, bg=checkbox_bg_color, selectcolor=checkbox_box_color, activebackground=checkbox_bg_color)
music_checkbox_search =  Checkbutton(searchbar_frame, text=" Music",indicatoron=0, variable=mu, width=13, anchor=W, font=checkbox_font, fg=checkbox_fg_color, bg=checkbox_bg_color, selectcolor=checkbox_box_color, activebackground=checkbox_bg_color)
scifi_checkbox_search =  Checkbutton(searchbar_frame, text=" Sci-Fi",indicatoron=0, variable=sc, width=13, anchor=W, font=checkbox_font, fg=checkbox_fg_color, bg=checkbox_bg_color, selectcolor=checkbox_box_color, activebackground=checkbox_bg_color)
sport_checkbox_search =  Checkbutton(searchbar_frame, text=" Sport",indicatoron=0, variable=sp, width=13, anchor=W, font=checkbox_font, fg=checkbox_fg_color, bg=checkbox_bg_color, selectcolor=checkbox_box_color, activebackground=checkbox_bg_color)
war_checkbox_search =  Checkbutton(searchbar_frame, text=" War",indicatoron=0, variable=wa, width=13, anchor=W, font=checkbox_font, fg=checkbox_fg_color, bg=checkbox_bg_color, selectcolor=checkbox_box_color, activebackground=checkbox_bg_color)
history_checkbox_search =  Checkbutton(searchbar_frame, text=" History",indicatoron=0, variable=hi, width=13, anchor=W, font=checkbox_font, fg=checkbox_fg_color, bg=checkbox_bg_color, selectcolor=checkbox_box_color, activebackground=checkbox_bg_color)
biography_checkbox_search =  Checkbutton(searchbar_frame, text=" Biography",indicatoron=0, variable=bi, width=13, anchor=W, font=checkbox_font, fg=checkbox_fg_color, bg=checkbox_bg_color, selectcolor=checkbox_box_color, activebackground=checkbox_bg_color)
combine_checkbox_search =  Checkbutton(searchbar_frame, text="Combine Results",indicatoron=0, variable=csr, width=15, anchor=W, font=("Comic", "10", "bold"), fg="#2d3033", bg=checkbox_bg_color, selectcolor="#8593a4", activebackground=checkbox_bg_color)

action_checkbox_search.bind("<Enter>", action_enter)
action_checkbox_search.bind("<Leave>", action_leave)
comedy_checkbox_search.bind("<Enter>", comedy_enter)
comedy_checkbox_search.bind("<Leave>", comedy_leave)
drama_checkbox_search.bind("<Enter>", drama_enter)
drama_checkbox_search.bind("<Leave>", drama_leave)
fantasy_checkbox_search.bind("<Enter>", fantasy_enter)
fantasy_checkbox_search.bind("<Leave>", fantasy_leave)
horror_checkbox_search.bind("<Enter>", horror_enter)
horror_checkbox_search.bind("<Leave>", horror_leave)
mystery_checkbox_search.bind("<Enter>", mystery_enter)
mystery_checkbox_search.bind("<Leave>", mystery_leave)
romance_checkbox_search.bind("<Enter>", romance_enter)
romance_checkbox_search.bind("<Leave>", romance_leave)
thriller_checkbox_search.bind("<Enter>", thriller_enter)
thriller_checkbox_search.bind("<Leave>", thriller_leave)
western_checkbox_search.bind("<Enter>", western_enter)
western_checkbox_search.bind("<Leave>", western_leave)
adventure_checkbox_search.bind("<Enter>", adventure_enter)
adventure_checkbox_search.bind("<Leave>", adventure_leave)
animation_checkbox_search.bind("<Enter>", animation_enter)
animation_checkbox_search.bind("<Leave>", animation_leave)
crime_checkbox_search.bind("<Enter>", crime_enter)
crime_checkbox_search.bind("<Leave>", crime_leave)
documentary_checkbox_search.bind("<Enter>", documentary_enter)
documentary_checkbox_search.bind("<Leave>", documentary_leave)
family_checkbox_search.bind("<Enter>", family_enter)
family_checkbox_search.bind("<Leave>", family_leave)
music_checkbox_search.bind("<Enter>", music_enter)
music_checkbox_search.bind("<Leave>", music_leave)
scifi_checkbox_search.bind("<Enter>", scifi_enter)
scifi_checkbox_search.bind("<Leave>", scifi_leave)
sport_checkbox_search.bind("<Enter>", sport_enter)
sport_checkbox_search.bind("<Leave>", sport_leave)
war_checkbox_search.bind("<Enter>", war_enter)
war_checkbox_search.bind("<Leave>", war_leave)
history_checkbox_search.bind("<Enter>", history_enter)
history_checkbox_search.bind("<Leave>", history_leave)
biography_checkbox_search.bind("<Enter>", biography_enter)
biography_checkbox_search.bind("<Leave>", biography_leave)

action_checkbox_search.grid(row=0, column=0, padx=(15,2), pady=2)
comedy_checkbox_search.grid(row=0, column=4, padx=2,pady=2)
drama_checkbox_search.grid(row=1, column=2, padx=2,pady=2)
fantasy_checkbox_search.grid(row=1, column=4, padx=2, pady=2)
horror_checkbox_search.grid(row=2, column=0, padx=(15,2),pady=2)
mystery_checkbox_search.grid(row=2, column=2, padx=2, pady=2)
romance_checkbox_search.grid(row=2, column=4, padx=2, pady=2)
thriller_checkbox_search.grid(row=3, column=2, padx=2, pady=2)
western_checkbox_search.grid(row=3, column=4, padx=2, pady=2)
adventure_checkbox_search.grid(row=0, column=1, padx=2, pady=2)
animation_checkbox_search.grid(row=0, column=2, padx=2, pady=2)
crime_checkbox_search.grid(row=1, column=0, padx=(15,2), pady=2)
documentary_checkbox_search.grid(row=1, column=1, padx=2, pady=2)
family_checkbox_search.grid(row=1, column=3, padx=2, pady=2)
music_checkbox_search.grid(row=2, column=3, padx=2, pady=2)
scifi_checkbox_search.grid(row=3, column=0, padx=(15,2), pady=2)
sport_checkbox_search.grid(row=3, column=1, padx=2, pady=2)
war_checkbox_search.grid(row=3, column=3, padx=2, pady=2)
history_checkbox_search.grid(row=2, column=1, padx=2, pady=2)
biography_checkbox_search.grid(row=0, column=3, padx=2, pady=2)
#combine_checkbox_search.grid(row=1, column=5, pady=2, columnspan=2, sticky=W)

conn.close()
root.mainloop()