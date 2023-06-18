from gen_fp_seq_seed import *
from Bio.SeqRecord import SeqRecord
from Bio.SeqIO import FastaIO
from tkinter import *
from tkinter import filedialog

class App(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.input_label = Label(self, text="Enter a string:")
        self.input_label.pack()
        self.input_entry = Entry(self)
        self.input_entry.pack()
        self.submit_button = Button(self, text="Generate Sequence List", command=self.generate_sequence_list)
        self.submit_button.pack()
        self.output_label = Label(self, text="Output:")
        self.output_label.pack()
        self.output_text = Text(self)
        self.output_text.pack()
        self.save_button = Button(self, text="Save to File", command=self.save_to_file)
        self.save_button.pack()

    def generate_sequence_list(self):
        input_str = self.input_entry.get()
        result = fp_generate(ai_generate_sequence_list(input_str))

        fasta_name = input_str.replace(',', '_').replace(' ', '')
        result_record = SeqRecord(result, id=fasta_name, description="Generated by PeptGPT")

        self.output_text.delete("1.0", END)
        self.output_text.insert(END, FastaIO.as_fasta(result_record))
    
    def save_to_file(self):
    # Open file dialog to choose a file to save the output to
        filename = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if not filename:
        # User cancelled save operation
            return
        with open(filename, "w") as f:
        # Write the contents of the output text widget to the file
            f.write(self.output_text.get("1.0", END))

def run_gui():
    root = Tk()
    app = App(root)
    root.mainloop()

run_gui()