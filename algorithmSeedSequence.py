data = """KMWIAIASMVFMFISVGFIYLSRYKVKMKWLRFLLALVAYILLIFAGIIIIFVVFSGP
KMWIAITSMVFMFISVFSIYISRYKAKNKIIRFILAFIAYVLMILAGIIIIFVVFSGP
KMWISLGSIVFMFISVFSIYFSRYKITNRIGKIVLAFIAYSLMIVAGLIMVIVVFSGP
KMWISLTGIGLMFVAVFSIYFSRYKVKNKIIKIILATIAYISMIIAGLIIVFVVFSGP
KMWVSFVSMGLMFLSVVLTIFAKEKLSG.LLRYSVLSVTFVMIMVSGVIIFLVVATGP
NMWISFFAMGLMFISVIVTIITKEKAKG.ILRYILLTFSFICLVVAGIIVFFTVFAGP
NMWISFFALALMFISAGAAIFSREKLRG.VIQKIVLAFSFICLLVSGLIVFLIVIGGP
NMYISFGGLLLMFISAGTALLARTKLSG.FFSKVVLTFSFCCLLVSGIIVAYIVLGGP
NMWISFIGLFLMFVSVVTAIVSREKLSG.FLQKVVLVFSFLCLVVSGLIVFYIVIGGP
KMNISLIAIGLMFVCNLLMIFAR.KITNGFLRFLVKTIAFLLLLVVLVMILIVIF...
.MWISFYSIGLLLVSILIITAVRKWVHNMVLSFLMKLVAYVMFFIGTLLMVLVVLTWP
KMWISFAGIGAFAIAALMVALSHTKLSG.WFATLVRLIAFIIFLFGTVIMIFVVVSGP
KMWVSLASMGFMFISILMIYLSRYKLNNKPLKFISALVAYLLMIVSGLIILFVVLSGP
KMWFALGAIGFMFFAVSFILLSRYKIKNKFLKGITALVAYTLMIVSGIVIFLVVFSGP
KMWFALGSMGLMFLAVIAIYISRYKFKNRFLKIITSFVAYTCMLISGVIVFFVVFSGP
KMWFALGSMGLMFLAVASIYLSRFKCQNRFLKIAISSFAYMCMLISGIIVFVVVFSGP
KMWFALGSMGLMFLAVVTIYFSRFKLKSRFLKITASTVAYSLMLMSGIIVFLVVFSGP
KMWISLAGMGFMFLSLIFIYFSRFKLKG.IFRIFTAIIAYALMIMAGLLILFVVLSGP
NMYISFAGILFLFLAIGLIFLSRYKLKG.VISGIVAFLAYMFMILGGLIIFYIVFSGP
NMWISLFGMGLLCLAMVLIVASRYRLKQKLFKWAAAVIAYACLALGGLIMAYIVLSGP""".split('\n')

def create_sequence_based_on_common(sequences):
    # Assumption! All sequences are the same length
    length = len(sequences[0])

    # Find the most common letter at each position
    # If there is a tie, choose the first one    
    consensus = ""
    for i in range(length):
        # Get the ith letter from each sequence
        letters = [seq[i] for seq in sequences]
        # Find the most common letter
        most_common = max(set(letters), key=letters.count)
        consensus += most_common

    return consensus

def rank_sequences_based_on_common(sequences):
    # Assumption! All sequences are the same length
    length = len(sequences[0])

    # Find the most common letter at each position
    # If there is a tie, choose the first one    
    consensus = ""
    for i in range(length):
        # Get the ith letter from each sequence
        letters = [seq[i] for seq in sequences]
        # Find the most common letter
        most_common = max(set(letters), key=letters.count)
        consensus += most_common

    # Rank the sequences based on how many letters they have in common with the consensus
    ranked_sequences = []
    for seq in sequences:
        score = 0
        for i in range(length):
            if seq[i] == consensus[i]:
                score += 1
        ranked_sequences.append((score, seq))

    # Sort the sequences by their score
    ranked_sequences.sort(reverse=True)

    return ranked_sequences

new_seq_based_on_common = create_sequence_based_on_common(data)
print("new_seq_based_on_common:", new_seq_based_on_common)

ranked_sequences = rank_sequences_based_on_common(data)
print("ranked_sequences:", ranked_sequences)
