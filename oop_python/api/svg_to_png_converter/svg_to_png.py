import cairosvg
from xml.etree import ElementTree

class ImageConverter:
    """
    Classic SVG to PNG image converter based on CairoSVG
    Documentation: https://cairosvg.org/documentation/
    To Run in Terminal:
        py -i filepath/svg_to_png.py
        SVG: filepath/image.svg
        PNG: filepath/newPNG_name.png
        Would you like to quit? (y/n) 
        y <enter>
        >>> quit()

    Functions:
        init -- Initialization to run menu function
        convert -- Converts using cairosvg library with parameters url (svg)
            and write_to (png)
        quit -- SystemExit of program in interpreter mode
        error_menu -- References quit function to exit when facing a filepath or system error,
            also used to direct commands from menu to exit program
        menu -- main menu for converting svgs to a png
    """
    def __init__(self):
        print("Hi, welcome to an SVG to PNG converter!")
        self.menu()

    def convert(self, svg, png):
        cairosvg.svg2png(url=svg, write_to=png)
        print("SVG successfully converted")

    def quit(self):
        raise SystemExit()

    def error_menu(self, command):
        if command == "y":
            self.quit()
        elif command == "n":
            self.menu()
        else:
            print("Invalid Input")

    def menu(self):
        try:
            svg = ""
            png = ""
            while True:
                print("Please enter the filepath for svg or type 'quit' to exit:")
                svg = input("SVG: ")
                if svg == 'quit':
                    self.error_menu('y')
                print("Please enter the output filepath and name for png or type 'quit' to exit:")
                png = input("PNG: ")
                if png == 'quit':
                    self.error_menu('y')
                try:
                    self.convert(svg, png)
                except ElementTree.ParseError:
                    command = input("Invalid SVG Format\nQuit? (y,n)").lower()
                    self.error_menu(command)
                except OSError:
                    command = input("Invalid SVG Filepath or Name\nQuit? (y, n)").lower()
                    self.error_menu(command)
                else:
                    command = input("Would you like to quit? (y/n)").lower()
                    self.error_menu(command)
        finally:
            print("\nThank you for using svg to png converter")

ImageConverter()
