import argparse
import re
from termcolor import colored
import pytest
from longest_frame import *


example1 = "this is not a DNA or RNA sequence"
example2 = "atcgtacgtgactgactgtacgtgGGGATCGATGCCCCTTAAAGAGTTTACATATTGCTGGAGGCGTTAACCCCGGAactgacttactgcggtcag" # ex1: http://bioweb.uwlax.edu/GenWeb/Molecular/Theory/Translation/Translation_Problems/translation_problems.htm
example3 = "acttagccgggactaTCAATGTAACGCGCTACCCGGAGCTCTGGGCCCAAATTTCATCCACTctcggggaagtccgaggagtccgt" # ex2: http://bioweb.uwlax.edu/GenWeb/Molecular/Theory/Translation/Translation_Problems/translation_problems.htm
example4 = "ccgtcttacttaagccccaagagaagCGCTACGTCTTACGCTGGAGCTCTCATGGATCGGTTCGGTAGGGCTCGATCACATCGCTAGCCATagaaagcacgtgggctgg" #ex from https://vlab.amrita.edu/index.php?sub=3&brch=273&sim=1432&cnt=1

def test_dna_reverse_complement():
    example1 = "this is not a DNA or RNA sequence"
    example2 = "atcgtacgtgactgactgtacgtgGGGATCGATGCCCCTTAAAGAGTTTACATATTGCTGGAGGCGTTAACCCCGGAactgacttactgcggtcag" 
    example3 = "acttagccgggactaTCAATGTAACGCGCTACCCGGAGCTCTGGGCCCAAATTTCATCCACTctcggggaagtccgaggagtccgt" 
    example4 = "ccgtcttacttaagccccaagagaagCGCTACGTCTTACGCTGGAGCTCTCATGGATCGGTTCGGTAGGGCTCGATCACATCGCTAGCCATagaaagcacgtgggctgg" 
    with pytest.raises(ValueError):
        dna_reverse_complement(example1)
    expected2 = 'ctgaccgcagtaagtcagtTCCGGGGTTAACGCCTCCAGCAATATGTAAACTCTTTAAGGGGCATCGATCCCcacgtacagtcagtcacgtacgat'
    expected3 = 'acggactcctcggacttccccgagAGTGGATGAAATTTGGGCCCAGAGCTCCGGGTAGCGCGTTACATTGAtagtcccggctaagt'
    expected4 = 'ccagcccacgtgctttctATGGCTAGCGATGTGATCGAGCCCTACCGAACCGATCCATGAGAGCTCCAGCGTAAGACGTAGCGcttctcttggggcttaagtaagacgg'
    assert dna_reverse_complement(example2) == expected2
    assert dna_reverse_complement(example3) == expected3
    assert dna_reverse_complement(example4) == expected4
    assert dna_reverse_complement(expected2) == example2
    

def test_find_matches():
    example1 = "AUGCCCUCCGCAUGAAUUGAAGCGUAGAUGCCCUAAGGUUUUCAUCAUUUGAGGACGAUGAA"
    example2 = "aucguacgugacugacuguacgugGGGAUCGAUGCCCCUUAAAGAGUUUACAUAUUGCUGGAGGCGUUAACCCCGGAacugacuuacugcggucag" 
    example3 = "acttagccgggactaTCAATGTAACGCGCTACCCGGAGCTCTGGGCCCAAATTTCATCCACTctcggggaagtccgaggagtccgt" 
    example4 = "ccgtcttacttaagccccaagagaagCGCTACGTCTTACGCTGGAGCTCTCATGGATCGGTTCGGTAGGGCTCGATCACATCGCTAGCCATagaaagcacgtgggctgg"
    expected1 = ['CCCUCCGCA', 'CCC', 'AAU']
    expected2 = ['CCCCUUAAAGAGUUUACAUAUUGCUGGAGGCGU']
    expected3 = []
    expected4 = ['GATCGGTTCGGTAGGGCTCGATCACATCGC']
    assert sorted(find_matches(example1)) == sorted(expected1)
    assert sorted(find_matches(example2)) == sorted(expected2)
    assert sorted(find_matches(example3)) == sorted(expected3)
    assert sorted(find_matches(example4)) == sorted(expected4)
    
def test_find_longest_match():
    example1 = ['CCCUCCGCA', 'CCC', 'AAU']
    expected1 = 'CCCUCCGCA'
    example2 = []
    expected2 = None
    expected3 = None
    assert find_longest_match(example1, 0) == expected1
    assert find_longest_match(example2, 0) == expected2
    assert find_longest_match(example1, 10) == expected3
    
def test_main():
    example1 = "atcgtacgtgactgactgtacgtgGGGATCGATGCCCCTTAAAGAGTTTACATATTGCTGGAGGCGTTAACCCCGGAactgacttactgcggtcag"
    expected1 = "CCCCTTAAAGAGTTTACATATTGCTGGAGGCGT"
    example2 = "acttagccgggactaTCAATGTAACGCGCTACCCGGAGCTCTGGGCCCAAATTTCATCCACTctcggggaagtccgaggagtccgt"
    expected2 = "ATGTAACGCGCTACCCGGAGCTCTGGGCCCAAATTT"
    example3 = "ccgtcttacttaagccccaagagaagCGCTACGTCTTACGCTGGAGCTCTCATGGATCGGTTCGGTAGGGCTCGATCACATCGCTAGCCATagaaagcacgtgggctgg"
    expected3 = "TGGATCGGTTCGGTAGGGCTCGATCACATCGCTAGC"
    assert main(example1, 0, 'on_yellow') == expected1
    assert main(example2, 0, 'on_yellow') == expected2
    assert main(example3, 0, 'on_yellow') == expected3