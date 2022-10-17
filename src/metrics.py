from sklearn.metrics import precision_score, recall_score
import csv
import argparse

def get_metrics(y_true, y_pred):
    """Returns precision, recall, F1 score and support for each class"""
    precision = precision_score(y_true, y_pred, pos_label='0')
    recall = recall_score(y_true, y_pred, pos_label='0')
    return precision, recall

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('data', help='Path to data file')
    parser.add_argument('--csv-delimiter', default='\t', help='CSV delimiter')
    args = parser.parse_args()
    with open(args.data, 'r') as f:
        reader = csv.DictReader(f, delimiter=args.csv_delimiter)
        y_true = []
        y_pred = []
        for row in reader:
            y_true.append(row['ground_truth'])
            y_pred.append(row['prediction'])
        precision, recall = get_metrics(y_true, y_pred)
        print('Precision: {}'.format(precision))
        print('Recall: {}'.format(recall))

if __name__ == '__main__':
    main()
    