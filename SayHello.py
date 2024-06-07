"""
File: SayHello.py
"""
# import the EasyFrame class
# it implements a frame window on which you can place GUI controls
from breezypythongui import EasyFrame

class SayHello(EasyFrame):
    """
    our SayHello class is a subclass of the EasyFrame class
    it inherits 
    class to displays a hello message
    """
    
    def __init__(self):
        """
        sets up the GUI window
        """

        # debug output to Python shell window
        print("__init__ method called")
        
        # start by calling the __init__() method of our parent class
        # this starts us off with a basic frame window on which we can add GUI components
        # we add GUI components on a grid
        # row 0, column 0 is the upper left corner of the grid
        EasyFrame.__init__(self)
        
        # labels for first and last names
        # you don't usually need to save the names of label objects
        # place the "First Name" label in row 0, column 0
        self.addLabel(text = "First Name", row = 0, column = 0)
        
        # place the "Last Name" label in row 1, column 0
        self.addLabel(text = "Last Name", row = 1, column = 0)

        # add text fields for user to enter first and last names
        # you need to save the names of text field objects
        # you will use the getText() method to read the text that the user has entered
        # you will use the setText() method to clear the text when the user hits the "Clear" button
        # place the firstName text field in row 0, column 1, initialize the text to an empty string
        self.firstName = self.addTextField( text = "", row = 0, column = 1)
        
        # place the lastName text field in row 1, column 1, initialize the text to an empty string
        self.lastName = self.addTextField( text = "", row =1, column =1)

        # add command buttons
        # add the "Clear" button in row 3, column 0
        # specify the method to be called when the user clicks the button
        # use clear for the method name
        self.clearBtn = self.addButton( text = "Clear", row = 3, column = 0, command = self.clear)
        
        # add the "Say Hello" button in row 3, column 1
        # specify the method to be called when the user clicks the button
        # use hello for the method name
        self.helloBtn = self.addButton(text = "Say Hello", row = 3, column = 1, command = self.hello)

    def clear(self):
        """
        event procedure called when the user clicks the "Clear" button
        blank out the text fields used to enter first and last names
        """

        # debug output to Python shell window
        print("user clicked Clear button")

        # blank out the firstName text field
        self.firstName.setText( "" )
        
        # blank out the lastName text field
        self.lastName.setText( "" )

    def hello(self):
        """
        event procedure called when the user clicks the "Say Hello" button
        """

        # debug output to Python shell window
        print("user clicked Say Hello button")
        
        # determine what message to display
        # store it in a variable named msg

        if self.firstName.getText() == "":
            msg = "Please enter first name."
        
        elif self.lastName.getText() == "":
            msg = "Please enter last name."

        else:
            msg = "Hello " + self.firstName.getText() + " " + self.lastName.getText()

        # debug output to Python shell window
        print(msg)
        
        # display the message in a message box
        self.messageBox( title = "", message = msg)
        
def main():
    """
    instantiates and pops up the window.
    """
    
    # debug output to Python shell window
    print("calling main loop")

    # this creates an object instance of our SayHello class
    # it uses that instance to call the mainloop method defined in the parent EasyFrame class
    # mainloop() will call the SayHello __init__() method and then loop waiting for events like button clicks
    SayHello().mainloop()
    
    # debug output to Python shell window
    print("returned from main loop")

    # hold window open to allow user to view output
    print("")
    input("Press ENTER to continue ")
        
# call our main function
if __name__ == "__main__":
    main()
