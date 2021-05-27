import numpy as np 

def function(x):

	s1 = x
	u9 = x
	paths = []
	try:
		if x > 1:
			s1 = 5+s1
			u9 = u9/x
			u9 = x-9
			paths.append(1)
		else:
			s1 = 9*u9
			x = 2+x
			s1 = x-s1
			paths.append(2)
		if u9 > 3:
			s1 = 9-s1
			paths.append(3)
		else:
			s1 = s1-u9
			u9 = 5/x
			s1 = 5*s1
			paths.append(4)
		paths.append(5)
		assert u9 >= 0
		u9 = u9**0.5
		return u9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))