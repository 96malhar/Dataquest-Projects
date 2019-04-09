import read
import collections

if __name__ == "__main__":
	df=read.load_data()
	headlines=df['headline'].tolist()
	
	str_headline = ""
	for line in headlines:
		str_headline = str_headline + str(line) + " "
	str_headline = str_headline.lower()
	str_headline = str_headline.strip()
		
	words = str_headline.split(" ")
	c = collections.Counter(words)
	print(c.most_common(100))


