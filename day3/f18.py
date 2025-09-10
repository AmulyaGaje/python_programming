#A 3-day tech workshop collected attendee registrations separately for each day. 
# You are given three lists (day1, day2, day3) of email addresses — lists may contain duplicates 
# (people registering multiple times) and email case may vary (Upper/Lower).
# Write a Python program that:
# Cleans each day's list (normalizes case, removes duplicates).
# Prints the total number of unique attendees across all days.
# Prints the list of attendees who attended all three days.
# Prints the list of attendees who attended exactly one day.
# Prints pairwise overlap counts (day1 & day2, day2 & day3, day1 & day3).
# Produces a final report with counts and sorted lists for each of the above outputs.
 
d1=[]
d2=[]
d3=[]
d1=list(input("Enter email registered on day 1").split())
d2=list(input("ENter email regesterd on day2").split())
d3=list(input("Enter email registered on day 3").split())
def clean(d1):
    cleaned=[]
    for i in d1:
        x=i.lower()
        if(x not in cleaned):
            cleaned.append(x)
    return cleaned
x1=clean(d1)
x2=clean(d2)
x3=clean(d3)
print(f"{x1}{x2}{x3}")
for i in x1:
    if i in x2 and i in x3:
        print(i,"registered in al three days")
