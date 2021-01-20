#!/usr/bin/env python3

import gender_guesser.detector as gender

def rounded_percent(nom, den):
    return round(float(nom)/float(den),2)

d = {}
detect = gender.Detector()
with open("linux_kernel_v2.6.11-HEAD_20-1-2020_sorted-contributors.txt") as f:
    for line in f:
        split_line = line.split()
        if len(split_line) > 1:
            n_commit = int(split_line[0])
            full_name=" ".join(split_line[1:-1])
            name=split_line[1]
            d[full_name] = [n_commit, detect.get_gender(name)]

n_male, n_female, n_unknown = 0, 0, 0
tot_male_commits, tot_female_commits, tot_unknow_commits = 0, 0, 0

for p, val in d.items():
    if val[1] == 'female':
        n_female += 1
        tot_female_commits += val[0]
    elif val[1] == 'male':
        n_male += 1
        tot_male_commits += val[0]
    else:
        n_unknown += 1
        tot_unknow_commits += val[0]

tot_people = n_female+n_male+n_unknown
tot_commits = tot_female_commits+tot_male_commits+tot_unknow_commits
tot_gendered_people = n_female+n_male
tot_genedered_commits = tot_female_commits+tot_male_commits
print ("Authors: female, male, unkown gender")
print (n_female, n_male, n_unknown)
print( "Percentages on total gendered authors and of unknown genders on total people")
print (rounded_percent(n_female,tot_gendered_people), rounded_percent(n_male,tot_gendered_people), rounded_percent(n_unknown,tot_people))
print ("Commits: female, male, unkown gender")
print (tot_female_commits, tot_male_commits, tot_unknow_commits)
print( "Percentages on total gendered commits and of unknown genders on total commits")
print (rounded_percent(tot_female_commits,tot_genedered_commits), rounded_percent(tot_male_commits,tot_genedered_commits), rounded_percent(tot_unknow_commits ,tot_commits))
    


