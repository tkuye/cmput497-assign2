from nltk import ChartParser, data
import argparse
import csv
from tqdm import tqdm

def read_grammar(filename):
    return data.load(filename)


def read_sentences(filename, csv_delimiter='\t'):
    with open(filename, 'r') as f:
        reader = csv.reader(f, delimiter=csv_delimiter)
        next(reader)
        return [{
            'id': row[0],
            'label': row[1],
            'sentence': row[2],
            'pos': row[3],
        } for row in reader]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('sentences', help='Path to sentences file')
    parser.add_argument('grammar', help='Path to grammar file')
    parser.add_argument('--csv-delimiter', default='\t', help='CSV delimiter')
    parser.add_argument('output', help='Path to output file')
    args = parser.parse_args()
    grammar = read_grammar(args.grammar)
    sentences = read_sentences(args.sentences)
    parser = ChartParser(grammar)
    
    data_sentences = []
    for sentence in tqdm(sentences):
        pos_sent = sentence['pos'].split()
        parses = list(parser.parse(pos_sent))
        data_sentences.append({
            'id': sentence['id'],
            'ground_truth': sentence['label'],
            'prediction': len(parses) > 0 and '0' or '1',
        })
    
    with open(args.output, 'w') as f:
        writer = csv.DictWriter(f, fieldnames=['id', 'ground_truth', 'prediction'], delimiter=args.csv_delimiter)
        writer.writeheader()
        writer.writerows(data_sentences)
    

if __name__ == '__main__':
    main()
    