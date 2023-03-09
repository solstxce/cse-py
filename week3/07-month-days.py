#Month to days
year=[31,28,31,30,31,30,31,31,30,31,30,31]
year2=["jan","feb","mar","apr","may","jun","jul","aug","sep","oct","nov","dec"]
month=input("Enter a month: ").lower()
for i in range(0,len(year2)):
    if month.startswith(year2[i]):
        days=year[i]
print(f"{month.title()} has {days} days.")
