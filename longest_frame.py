import argparse
import re
import sys
from termcolor import colored

def dna_reverse_complement(sequence):
    dna_dict = {'A':'T', 'T':'A', 'G':'C', 'C':'G', 'a':'t', 't':'a', 'c':'g', 'g':'c'}
    try:
        complement = ''.join(map(lambda x: dna_dict[x], sequence[::-1]))
    except:
        raise ValueError("Sequence contains 't' or 'T', indicating DNA, but contains characters other than ACTG (case-insensitive).")
    return complement

def find_matches(sequence):
    matches = re.findall('(?=A[TU]G((?:.{3})+?)[TU](?:AG|AA|GA))', sequence)
    return matches

def find_longest_match(matches, min_length):
    longest_match, length = None, min_length
    for match in matches:
        if len(match) >= length:
            length = len(match)
            longest_match = match
    return longest_match

def print_highlighted_frame(sequence, longest_match, on_color='on_red'):
    text = sequence.split(longest_match)[0] + colored(longest_match, on_color=on_color) + sequence.split(longest_match)[1]
    print(text)

def parse_args(args):   
    parser = argparse.ArgumentParser(description="Longest reading frame highlighter")
    parser.add_argument('--min-length', '-ml', default=1, type=int, help='Minimum reading frame length recognized by the program.')
    parser.add_argument('--color', '-c', default='on_yellow', type=str, help="""Color used to highlight the reading frame within the original sequence. Must be one of: on_grey, on_red, on_green, on_yellow (default), on_blue, on_magenta, on_cyan, on_white.""")
    parser.add_argument('--camel', '-ca', default='atcgtacgtgactgactgtacgtgATGCCCAAGCTGAATAGCGTAGAGGGGTTTTCATCATTTGAGGACGATGTATAAactgacttactgcggtcag', type=str, help="Sequence to be analyed with the 5'UTR in lowercase, the reading frame in uppercase, and the 3'UTR in lowercase. Default example: atcgtacgtgactgactgtacgtgATGCCCAAGCTGAATAGCGTAGAGGGGTTTTCATCATTTGAGGACGATGTATAAactgacttactgcggtcag")
    return parser.parse_args()

def main(sequence, min_length, on_color):
        
    # Find open reading frames - if DNA also check complement
    if 'T' in sequence.upper():
        forward_matches = find_matches(sequence)
        comp_matches = find_matches(dna_reverse_complement(sequence))
        matches = forward_matches + comp_matches
    else:
        matches = find_matches(sequence)
        
    # Determine which open reading frame is longest
    longest_match = find_longest_match(matches, min_length)
    
    # Print results to output
    if longest_match is None:
        print("No frame at or above specified minimum length. Original sequence: " + sequence)
    else:
        if longest_match in comp_matches:
            longest_match = dna_reverse_complement(longest_match)
        print_highlighted_frame(sequence, longest_match, on_color=on_color)
        
    return longest_match
    
def main_parse_wrapper():
    # parse arguments, check for input sequence
    args = parse_args(sys.argv[1:])
    sequence = args.camel
    min_length = args.min_length
    on_color = args.color
    if sequence == 'atcgtacgtgactgactgtacgtgATGCCCAAGCTGAATAGCGTAGAGGGGTTTTCATCATTTGAGGACGATGTATAAactgacttactgcggtcag':
        print("WARNING: No camel provided. Proceeding with default sequence as a demonstration. Provide your own sequence using --camel or -ca.")
    
    main(sequence, min_length, on_color)
    
if __name__ == '__main__':
    main_parse_wrapper()