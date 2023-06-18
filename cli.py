from gen_fp_seq_seed import *
from Bio import SeqIO
from Bio.SeqIO import FastaIO
from Bio.SeqRecord import SeqRecord

def run_cli():
    prompt = input('Provide comma-seprated list of keywords\n')
    result = fp_generate(ai_generate_sequence_list(prompt))
    fasta_name = prompt.replace(',', '_').replace(' ', '')
    result_record = SeqRecord(result, id=fasta_name, description="Generated by PeptGPT")

    print("\n")
    print(FastaIO.as_fasta(result_record))
    SeqIO.write(result_record, 'out.fasta', format="fasta")

run_cli()