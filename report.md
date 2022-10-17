# Report 
Report information for assignment 2.

## Scores
- Precision: 0.78
- Recall: 0.978444

Additionally, you may run `python3 src/metrics.py ./output/train.tsv` to get the results of the precision and recall scores. 

Reasons for false positive scores
- The context free grammar had too many rules in place it was over parsing the sentences. 
- The rules may be contradicting one another which is why they may be over parsing bad sentences.

Reasons for false negative scores
- Some of the rules in place could not cover all the possible cases available to ensure the sentences were completely parsable. 


## With our current design, is it possible to build a perfect grammar checker? 
No it is not. By creating arbitrary rules to cover each of the possible cases, we obviously using a rule based methodology alone cannot effectively parse every possible sentence as new sentences can quite easily be constructed that may be valid but not within our current rule set.

