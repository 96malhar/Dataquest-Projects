import read
import collections
def remove_subdomain(url):
	word_list = str(url).split(".")
	l = len(word_list)
	domain_name = word_list[l-2] + "." + word_list[l-1]
	return domain_name


if __name__ == "__main__":
	df=read.load_data()
	
	df['url'].dropna(inplace=True)
	
	domains = df['url'].apply(remove_subdomain)
	#print(domains.value_counts()) does not work coz only some values shown

	#for name, count in domains.value_counts().items(): For Lazy Iteration
		#print(name,count)
	
	domains = domains.tolist() 
	c=collections.Counter(domains)
	print(c.most_common(100)) #to display 100 most common

	

