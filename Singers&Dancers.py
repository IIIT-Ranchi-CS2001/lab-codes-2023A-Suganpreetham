singers={'sugan','preetham','raj','ram','aditya','rahul','rohit'}
dancers={'preetham','varun','aditya','virat','gautham','chota bheem','doraemon'}
artists=singers.union(dancers)
allrounders=singers.intersection(dancers)
danbutnotsin=dancers-allrounders
sinbutnotdan=singers-allrounders
unique=danbutnotsin.union(sinbutnotdan)
print(artists)
print(allrounders)
print(danbutnotsin)
print(sinbutnotdan)
print(unique)