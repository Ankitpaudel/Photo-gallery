from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox, filedialog
import shutil
import os

# Global variables section - add variables that are required

path = 'images/' # folder that has all the images

# functions and sub-functions to manage the various buttons and user inter-action
  
# see the coursework sepcification

imageBtnList=[]
def showFriendFriends(head, count): 
    '''this function show friend friends image and their name if exist '''
    print(f"show friend friends in column {count}")
    friendFolderPath = path + head # Full path of friend friends
    print(friendFolderPath)
    friend = head +"'s" #Friend name to add in remove button
    row = 2
    
    # if friend friends are already displayed
    if bodyFrame.grid_slaves(row=row, column=count): # check whether if any widgets are already displayed in the specific row and column if it is not empty message will pop up
        messagebox.showinfo("Information",f"{friend} friends are already displayed!")
        return
    
    if os.path.isdir(friendFolderPath): # check whether image are their in friends friend file
        if os.listdir(friendFolderPath): # check file exist or not
            for file in os.listdir(friendFolderPath): #Loop through each friend friends eg.'myAppStarter/images/adom/......
                print(file,"line 34")
                (head,tail)= os.path.splitext(file)
                print(f"head is {head}, tail is {tail} line 39")
                if tail.lower() not in [".png",".jpg"]:
                    continue
                fullPath =friendFolderPath+"/"+file
                print(fullPath)
                print(row)
                friendPhoto = PhotoImage(file=fullPath)
                friendPhoto = friendPhoto.subsample(3,3)
                FriendsLabel = ttk.Label(bodyFrame, image=friendPhoto)
                FriendsLabel.image = friendPhoto
                FriendsLabel.grid(row=row, column=count)
                friendFreindsNameBtn =ttk.Label(bodyFrame, text=head, style='friendFreindsName.TLabel', anchor='center')
                friendFreindsNameBtn.grid(row=row+1, column=count)
                row =row+2
            clearFriendFriendsBtn = ttk.Button(bodyFrame, text=f"Remove\n{friend}\nfriends",style='clearFriendFriendsBtn.TButton', command= lambda:clearFriendFriends(count))
            clearFriendFriendsBtn.grid(row=row, column=count)
        else:
            messagebox.showinfo("No Images Found",f"Friends folder does exist for {friend} but no image in the folder")
    else:
        messagebox.showinfo("No Folder",f"Friends folder does not exist for {friend}")

   #function to show the friend image
def showFriends():
    #This line simply prints a message to the console indicating that the show friends action has been clicked.
    print("show friends clicked")
    showFrame()
    btnShowFriends.configure(state=DISABLED)
    btnClearAll.configure(state=NORMAL)
    "This line calls a function named"
    processPath()
     
    
    #function to process the path of image 
def processPath():
    global path  # Declare path as a global variable to access it inside the function
    if os.path.exists(path):  # Check if the specified path exists
        print("path exist")  # Print a message indicating that the path exists
        if os.path.isdir(path):  # Check if the path is a directory
            print("its a directory")  # Print a message indicating that it's a directory
            count = 0  # Initialize a counter to keep track of the number of image files processed
            for file in os.listdir(path):  # Iterate over the files in the directory
                print(file)  # Print the name of the file
                (head, tail) = os.path.splitext(file)  # Split the file name into its name and extension
                print(f"head is {head}, tail is {tail}")  # Print the name and extension of the file
                
                if tail.lower() not in [".png", ".jpg"]:  # Check if the file extension is not .png or .jpg
                    continue  # Skip processing this file if its extension is not an image
                print(file)  # Print the name of the image file
                count += 1  # Increment the counter for each image file processed
                print(f"number of images is {count}")  # Print the count of image files processed
                displayImage(file, count)  # Call a function to display the image
        else:
            print("path exist but no folders")  # Print a message indicating that the path exists but has no folders
            messagebox.showinfo("Folder Information", "Path exists but has no folder")  # Show a messagebox with information about the path
    else:
        print("not path")  # Print a message indicating that the path does not exist
        messagebox.showinfo("Path Information", "Path does not exist")  # Show a messagebox indicating that the path does not exist

        
def displayImage(item, count):
    # Calculating the column number based on the count to determine the position of the image
    column = count * 2
    print(f"Column number calculated: {column}")
    
    # Extracting the filename (head) and extension (tail) from the item
    (head, tail) = os.path.splitext(item)
    print(f"Filename: {head}")
    print(f"Extension: {tail}")
    
    # Constructing the full path of the item by combining the path and the item name
    itemLoc = path + item  # Full path required for accessing the image
    print(f"Complete item location: {itemLoc}")
    
    # Loading the image using PhotoImage and subsampling to reduce its size
    photo = PhotoImage(file=itemLoc)
    photo = photo.subsample(2, 2)  # Reducing the size of the image for display
    print(f"Image loaded and resized: {photo}")
    
    # Creating a button with the image and binding a function to it
    buttonName = head + "'s friends"
    imageButtons = ttk.Button(bodyFrame, image=photo, command=lambda: showFriendFriends(head, column - 2))
    imageButtons.image = photo  # Keeping a reference to the image to prevent it from being garbage collected
    imageButtons.grid(row=0, column=column - 2)  # Placing the button in the GUI grid
    imageBtnList.append((buttonName, item))  # Adding the button name and item to a list for reference
    
    # Creating a button with the friend's name and binding a function to it
    friendsName = ttk.Button(bodyFrame, text=buttonName.capitalize(), style='friendName.TButton',
                              command=lambda: friendButton(head, column - 2))
    
    friendsName.grid(row=1, column=column - 2, ipadx=5)  # Placing the button in the GUI grid with additional padding
         


def friendButton(head, column):
    # Storing the head and column parameters in local variables for clarity
    head1 = head
    column1 = column
    
    # Invoking the function to display the friends of the specified head at the given column position
    showFriendFriends(head1, column1)



def clearAll():
    # Prompt the user for confirmation to clear all images
    answer = messagebox.askquestion('Confirmation', 'Are you sure you want to clear all images?')
    
    # If user confirms the action
    if answer == 'yes':
        # Remove all widgets (images) within the bodyFrame
        for widget in bodyFrame.winfo_children():
            widget.destroy()
        
        # Hide the bodyFrame from the GUI
        bodyFrame.grid_remove()
    
    # Enable the "Show Friends" button after clearing
    btnShowFriends.configure(state=NORMAL)
    # Disable the "Clear All" button as it's already cleared
    btnClearAll.config(state=DISABLED)

        
def delFriend():
    # Request user input to select a file for deletion
    delFile = filedialog.askopenfilename(initialdir=path, title="Select file to delete", filetypes=(("Image files", "*.png;*.jpg;*.jpeg;*.gif"), ('All files', '*.*')))
    
    # Proceed if a file is selected
    if delFile:
        # Ask for confirmation before deleting the selected file
        check = messagebox.askyesno(title="Confirm Deletion", message="Are you sure you want to delete this file?")
        
        # If user confirms deletion
        if check:
            # Extract filename from the full path
            filename = os.path.basename(delFile)
            # Delete the selected file
            os.remove(delFile)
            
            # Clear the display area by removing all widgets inside bodyFrame
            for widget in bodyFrame.winfo_children():
                widget.destroy()
            # Hide the bodyFrame from the GUI layout
            bodyFrame.grid_remove()
            # Update the display to reflect the deleted file
            showFriends()
            # Provide feedback to the user about the successful deletion
            messagebox.showinfo("File Deleted", f"The file {filename} has been successfully deleted.")
        
        # If user cancels deletion
        else:
            # Notify the user about the cancelled deletion action
            messagebox.showinfo("Deletion Cancelled", "File deletion has been cancelled. No files were deleted.")

             
def addFriend():
    # Define acceptable file types for the file dialog
    filetypes = (("Image files", "*.png;*.jpg;*.jpeg;*.gif"), ("All files", "*.*"))
    
    # Prompt the user to select a file for adding as a new friend
    selectFile = filedialog.askopenfilename(initialdir="./", title="Select File", filetypes=filetypes)
    
    # If a file is selected
    if selectFile:
        # Display the selected file path for verification
        print(selectFile)
        
        # Confirm the user's intention to add the selected file as a new friend
        check = messagebox.askquestion("Confirm Addition", "Are you sure you want to add this file as a new friend?")
        
        # If the user confirms the addition
        if check == "yes":
            # Check if the selected file is an image
            (head, tail) = os.path.splitext(selectFile)
            
            # If the file has a valid image extension
            if tail.lower() in [".png", ".jpeg"]:
                # Copy the selected file to the designated path
                shutil.copy(selectFile, path)
                
                # Extract the filename from the full path
                filename = os.path.basename(selectFile)
                
                # Display the newly added friend's image
                displayImage(filename, len(imageBtnList) + 1) 
                
                # Provide feedback about the successful addition
                messagebox.showinfo("New Friend Added", f"The file {filename} has been added as a new friend.")
                
            else:
                # Warn the user if the selected file is not an image
                messagebox.showwarning("Invalid File Type", "The selected file is not an image file and cannot be added.")
        else:
            # Inform the user that the addition process has been cancelled
            messagebox.showinfo("Addition Cancelled", "The addition of the new friend has been cancelled.")


def quitApp():
    # Prompt the user for confirmation before quitting
    see_more = messagebox.askyesno(message='Are you sure you want to quit?', detail='Click yes to quit')
    
    # If the user chooses to quit
    if see_more:
        # Exit the application
        exit()


# There will be some other functions to handle the user interactions like clearing friend'sfriends, create frames, etc
def clearFriendFriends(column):
    print(f"column to be clear is {column}")
    widgets = bodyFrame.grid_slaves(column=column)
    num_widgets = len(widgets)
    print(num_widgets)
    for widget in widgets[:num_widgets-2]: # iterate over widgets starting from indes 4 onwards
        print(widget)
        widget.grid_remove()
 
#create Bidy Frame again after clearing all       
def showFrame():
    bodyFrame.grid(row=2,column=0,padx=10,pady=10, sticky=NW)
    btnShowFriends.configure(state=DISABLED)
    btnClearAll.configure(state=NORMAL)        
        
# Basic Window for your app
myApp = Tk()
myApp.title("Image display app by: Ankit paudel")
myApp.geometry("1200x800")
myApp.maxsize(1200,800)
myApp.configure(background='Teal')

# Code to configure styles for your ttk widgets
# write code below to create styles for you buttons, labels, frames, etc

style = ttk.Style()
style.theme_use("alt")
style.configure('Menu.TLabelframe', background="#153448")
style.configure('body.TLabelframe', background="#3C5B6F",fg="black")
#style for Button 
style.configure('TButton',
                background="#DFD0B8", #b2dfed
                foreground= '#060c8c',
                width=20,
                font=('arial, 14'),
                relief='raised')

style.map('TButton', background=[('active','red')]) #Background color change when any button in the window is hover

# style for friend name below their name
style.configure('friendName.TButton',
                backgroung="white",
                width=14,
                borderwidth=8,
                bordercolor = 'white',
                background="white", 
                font="arial 10", 
                foreground="black",
                relief = 'groove',
                anchoe='center')
style.configure('clearFriendFriendsBtn.TButton',
                background="red", 
                width=8,
                font=('arial 8'))

style.configure('friendFreindsName.TLabel',
                width=8,
                background="black",
                borderwidth=6,
                foreground="white",
                font=('arial',9),
                relief='sunken',
                anchor='center')
style.map('TButton', foreground=[('active','#060c8c'),('disabled','gray')])


# Create a frame(mainMenu) that will hold buttons to manage the app.
mainMenu =ttk.LabelFrame(myApp,  text="App Menu:", width=1200, style='Menu.TLabelframe' ) 
mainMenu.grid(row=0,column=0, ipady=6, sticky=NW)

bodyFrame = ttk.LabelFrame(myApp, text="My Friends - click a friend to see their friends", style='body.TLabelframe' ) #b2dfee
bodyFrame.grid(row=2,column=0,padx=10,pady=10, sticky=NW)


# create buttons that have been described in the coursework specification and add to the frame above
btnShowFriends = ttk.Button(mainMenu, text="Show Friends", command=showFriends )
btnShowFriends.grid(row=0, column=0, ipadx=4, ipady=10, sticky=W)
btnClearAll = ttk.Button(mainMenu, text="Clear All", command=clearAll )
btnClearAll.grid(row=0, column=1, ipadx=4, ipady=10, sticky=W)
btnClearAll.config(state=DISABLED)

btnDeleteFriebds = ttk.Button(mainMenu, text="Delete Friends", command=delFriend )
btnDeleteFriebds.grid(row=0, column=2, ipadx=4, ipady=10, sticky=W)
btnAddFriends = ttk.Button(mainMenu,  text="Add Friends", command=addFriend)
btnAddFriends.grid(row=0, column=3,ipadx=4, ipady=10, sticky=NW)
btnQuit = ttk.Button(mainMenu, text="Quit", command=quitApp )
btnQuit.grid(row=0, column=4,ipadx=4, ipady=10, sticky=NW)

myApp.mainloop()
