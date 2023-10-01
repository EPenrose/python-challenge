import csv
import os


CSV_PATH = os.path.join("Resources", "election_data.csv")

csvfile = "election_data.csv"

os.chdir(os.path.dirname(os.path.realpath(__file__)))
with open(CSV_PATH, 'r') as csvfile:
    reader = csv.reader(csvfile)
    csv_header =next(csvfile)
    
    total_votes = 0
    candidates = []
    votes_per_candidate = {}
    
    for row in reader:
        if row[2] == 'Country':
            continue
        
        total_votes += 1
        
        candidate = row[2]
        if candidate not in candidates:
            candidates.append(candidate)
            votes_per_candidate[candidate] = 0
        
        votes_per_candidate[candidate] += 1
    
    percentages = {}
    for candidate in votes_per_candidate:
        percentage = votes_per_candidate[candidate] / total_votes * 100
        percentages[candidate] = percentage
    
    winner = max(votes_per_candidate, key=votes_per_candidate.get)
    
    print('Election Results')
    print('-------------------------')
    print(f'Total Votes: {total_votes}')
    print('-------------------------')
    for candidate in candidates:
        print(f'{candidate}: {percentages[candidate]:.3f}% ({votes_per_candidate[candidate]})')
    print('-------------------------')
    print(f'Winner: {winner}')
    print('-------------------------')
    
    
    with open(r'analysis\result.txt', 'w') as outfile:
        outfile.write('Election Results\n')
        outfile.write('-------------------------\n')
        outfile.write(f'Total Votes: {total_votes}\n')
        outfile.write('-------------------------\n')
        for candidate in candidates:
            outfile.write(f'{candidate}: {percentages[candidate]:.3f}% ({votes_per_candidate[candidate]})\n')
        outfile.write('-------------------------\n')
        outfile.write(f'Winner: {winner}\n')
        outfile.write('-------------------------\n')
