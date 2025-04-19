import customtkinter as ctk

C_GRAY = '#333'
C_HOVER = '#444'
C_GREEN = '#7FFF00'
PLAYER = "O"
CNT = 0
ROWS = 5
COLUMNS = 5
LINE = 4
GRID = [[None] * ROWS] * COLUMNS

def message(head, message):
   message_w = ctk.CTkToplevel()
   message_w.resizable(False, False)
   message_w.title(head)
   ctk.CTkLabel(message_w, text=message, wraplength=200).pack(padx=30, pady=10)
   ctk.CTkButton(message_w, text='OK', fg_color=C_GRAY, hover_color=C_HOVER, border_color=C_GREEN, border_width=3,
               command=message_w.destroy).pack(padx=30, pady=20)
   message_w.grab_set()
   message_w.wait_window()
    
def reset():
   global CNT, GRID
   for i in range(ROWS):
      for j in range(COLUMNS):
         GRID[i][j].configure(text=' ', state='normal')
   CNT = 0   

def is_winner(GRID):
   for i in range(ROWS):
      for j in range(COLUMNS):
         # check for columns
         if j + LINE - 1 < COLUMNS:
            if all(GRID[i][j + k].cget("text") == PLAYER for k in range(LINE)):
               return True;
         
         # check for rows
         if i + LINE - 1 < ROWS:
            if all(GRID[i + k][j].cget("text") == PLAYER for k in range(LINE)):
               return True;
            
         # check for main diagonal lines
         if i + LINE - 1 < ROWS and j + LINE - 1 < COLUMNS:
            if all(GRID[i + k][j + k].cget('text') == PLAYER for k in range(LINE)):
               return True
         
         # check for secondary lines
         if i + LINE - 1 < ROWS and j - LINE + 1 >= 0:
            if all(GRID[i + k][j - k].cget('text') == PLAYER for k in range(LINE)):
               return True
   return False
          
def check(i, j):
   global PLAYER, CNT, GRID
   CNT += 1
   btn = GRID[i][j]
   btn.configure(state='disabled', text=PLAYER)
   if is_winner(GRID):
      message('WAOS!', f'- Game winner: {PLAYER} -')
      reset()
   elif CNT == ROWS * COLUMNS:
      message('UPS!', '- Finished in a draw -')
      reset()
   else:
      PLAYER = 'X' if PLAYER == 'O' else 'O'

def main():
   global GRID
   app = ctk.CTk()
   app.title('TIC-TAC-TOE')
   app.resizable(False, False)
   app.geometry('400x400')

   frame = ctk.CTkFrame(app, corner_radius=10)
   frame.grid(row=0, column=0, sticky='nsew', padx=5, pady=5)

   # Grid-Buttons
   GRID = [[ctk.CTkButton(frame, text=' ', font=('Helvetica', 25, 'bold'), state='normal', fg_color=C_GRAY, 
                     hover_color=C_HOVER, text_color_disabled=C_GREEN, 
                     command=lambda r = i, c = j: check(r, c)) for j in range(COLUMNS)] for i in range(ROWS)]

   for i in range(ROWS):
      for j in range(COLUMNS):
         GRID[i][j].grid(row=i, column=j, sticky='nsew', padx=5, pady=5)

   frame.rowconfigure(list(range(ROWS)), weight=1)
   frame.columnconfigure(list(range(COLUMNS)), weight=1)

   app.rowconfigure(0, weight=1)
   app.columnconfigure(0, weight=1)

   app.mainloop()

if __name__ == '__main__':
    main()