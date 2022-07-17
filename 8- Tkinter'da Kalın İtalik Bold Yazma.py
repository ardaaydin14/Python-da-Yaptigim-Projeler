from tkinter import *
   
class RadioFont( Frame ):

     
	def __init__( self ):
		
        
		Frame.__init__( self )
		self.pack( expand = YES, fill = BOTH )
		self.master.title( "https://github.com/ardaaydin14" ) 

		self.frame1 = Frame( self )
		self.frame1.pack()
 
		self.text = Entry( self.frame1, width = 40,font = "Corbel 34" )

		self.text.insert( INSERT, "https://github.com/ardaaydin14" )
		self.text.pack( padx = 5, pady = 5 )
 
		self.frame2 = Frame( self )
		self.frame2.pack()
   
		fontSelections = [ "Plain", "Bold", "Italic", "Bold/Italic" ]

		self.chosenFont = StringVar()
  
		
		self.chosenFont.set( fontSelections[ 0 ] ) 
  
	
		for style in fontSelections:
			aButton = Radiobutton( self.frame2, text = style,
			variable = self.chosenFont, value = style,
			command = self.changeFont )
			aButton.pack( side = LEFT, padx = 5, pady = 5 )
 
	def changeFont( self ):
		
      
		desiredFont = "Corbel 34"

		if self.chosenFont.get() == "Bold":
			desiredFont += " bold"
		elif self.chosenFont.get() == "Italic":
			desiredFont += " italic"
		elif self.chosenFont.get() == "Bold/Italic":
			desiredFont += " bold italic"

		self.text.config( font = desiredFont )

def main():
	RadioFont().mainloop()
 
if __name__ == "__main__":
	main()