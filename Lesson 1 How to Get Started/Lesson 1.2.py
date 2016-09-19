# Lesson 1: Problem Set

#number of hours in 7 week

days = 7 * 7 * 24
print (days)


a = 1
x = 5

a,x = x,a
a,x = x,a

print (a)
print (x)


speed_of_light = 299800000. # meters per second
nano_per_sec = 1000000000. # 1 billion

nanodistance = speed_of_light / nano_per_sec

print (nanodistance)


s = ''
print (s[1:])


# text = "all zip files are zipped"
text = 'all zip files are compressed'
print (text.find('zip', text.find('zip') + 1))


x = 3.14159


int_x = int(x) # integral part of x
string_x = str(x)
dot_position = string_x.find('.')
check_fractional = str(int(string_x[dot_position + 1:dot_position + 2]) - 5)

new_x = int_x - check_fractional.find('-')

print (new_x)