import tkinter as tk

class MazeGUI:
    
    def __init__(self, maze):
        self.maze = maze
        self.maze.title("Maze")

        self.canvas = tk.Canvas(self.maze, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)
        
        # Bind the resize event to the resize handler
        self.canvas.bind("<Configure>", self.on_resize)

        # Draw the initial square
        self.draw_maze()

        #Define game

        #Define Training Agent 
    
    def on_resize(self, event):
        # Redraw the square when the window is resized
        self.draw_maze()

    def draw_maze(self):        
#--------------------------------------------Drawing Boarders of Maze-------------------------------------------  
        # Clear the canvas
        self.canvas.delete("all")

        # Get the size of the canvas
        width = self.canvas.winfo_width()
        height = self.canvas.winfo_height()

        # Define the margin for the square
        margin = 20

        # Calculate the size of the square based on the canvas size
        size = min(width, height) - 2 * margin
        sizeMaze = size /2

        # Calculate the top-left corner of the square (b = boarders)
        b_x1 = (width - size) // 2
        b_y1 = (height - size) // 2
        b_x2 = b_x1 + size
        b_y2 = b_y1 + size

        # Draw the square using lines
        self.canvas.create_line(b_x1, b_y1, b_x2, b_y1, fill="black", width=2)  # Top edge
        self.canvas.create_line(b_x2, b_y1, b_x2, b_y2, fill="black", width=2)  # Right edge
        self.canvas.create_line(b_x2, b_y2, b_x1, b_y2, fill="black", width=2)  # Bottom edge
        self.canvas.create_line(b_x1, b_y2, b_x1, b_y1, fill="black", width=2)  # Left edge
#---------------------------------------------------------------------------------------------------------------
#--------------------------------------------Drawing Maze-------------------------------------------------------  
        # Calculate the simple maze corner (m = maze)
        m_x1 = (width - sizeMaze) // 2
        m_y1 = (height - sizeMaze) // 2
        m_x2 = m_x1 + sizeMaze
        m_y2 = m_y1 + sizeMaze

        #Draw Simple Maze 
        self.canvas.create_line(m_x1, m_y1, b_x2, m_y1, fill="black", width=2)  # Top edge
        self.canvas.create_line(b_x2, b_y2 / 2, m_x2 / 1.25, b_y2 / 2, fill="black", width=2)  # Middle edge
        self.canvas.create_line(m_x2 / 1.25, b_y2 / 2, m_x2 / 1.25, b_y2, fill="black", width=2)  # Right edge
        self.canvas.create_line(m_x1, m_y1, m_x1, b_y2, fill="black", width=2)  # Right edge
#---------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":

    game = tk.Tk()
    board = MazeGUI(game)
    game.mainloop()


