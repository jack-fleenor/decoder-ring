from math import inf
from tkinter import END, LEFT, RIGHT, Button, Frame, Label, Entry

class TopRow:
  def __init__(self, root):
    self.root = root
    self.row = Frame(root)
    self.text_field_label = Label(self.row, text="Message: ")
    self.text_field_label.grid(row=0, column=0)
    self.secrect_text_field_label = Label(self.row, text="Secret Message: ")
    self.secrect_text_field_label.grid(row=0, column=2)
    self.text_field_input = Entry(self.row, bd=1)
    self.text_field_input.grid(row=0, column=1)
    self.secrect_text_field_input = Entry(self.row, bd=1)
    self.secrect_text_field_input.grid(row=0, column=3)
    self.decode_button = Button(self.row, text="Decode", command=self.handle_decode)
    self.encode_button = Button(self.row, text="Encode", command=self.print_input)
    self.decode_button.grid(row=1, column=0)
    self.encode_button.grid(row=1, column=1)
    self.row.pack()
  
  def handle_decode(self):
    input_value = self.text_field_input.get()
    left, right = 0, len(input_value)
    message = ''
    while left < right:
      if input_value[left] != ' ':
        left += 1
      elif input_value[left] == ' ':
        if input_value[left + 1] == ' ':
          message += "1"
          left += 2
        else:
          message += "0"
          left += 1
    self.secrect_text_field_input.insert(END, message)

class Window:
  def __init__(self,root):
    self.root = root
    self.root.title = "Window"
    self.top_row = TopRow(root)
    self.root.mainloop()