marker = "EY"
replacement = "Eyjafjallajokull"
line = "The eruption of the volcano EY in 2010 disrupted air travel in Europe for 6 days."
i=line.find(marker)
j=len(marker)
replaced =line[0:i]+replacement+line[i+2:]

print (replaced)