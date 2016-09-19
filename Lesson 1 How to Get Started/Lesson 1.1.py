## String operations

name = 'Yurii Ratushnyi'
print (name[-4])
print (name[3:])
print (name[:2])
print (name[:])

s = 'audacity'
print ('U' + s[2:])
print (s + s[0:0])
print (s[:3] + s[3:])
print (s[:-1])


sentence = 'We are constantly trying to improve our Services, so these Terms may need to change along with the Services'
print (sentence)
print (sentence.find('to'))
print (sentence[sentence.find('to'):])
print (sentence.find('algebra'))

s = 'string'
print (s.find('')) ## search for empty string returns 0
print (s.find('s'))


print ('/ ' * 15)

# Return first link from the page

page = '<li><a href="http://blag.xkcd.com">Blag</a></li>'

start_link = page.find('<a href=')
start_url = page.find('"', start_link)
end_url = page.find('"', start_url + 1)
url = page[start_url + 1:end_url]

print (url)