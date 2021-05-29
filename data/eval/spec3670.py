import numpy as np 

def function(x):

	s9 = x
	u5 = x
	paths = []
	try:
		if u5 <= 9:
			x = 8*x
			x = 7+2
			paths.append(1)
		else:
			u5 = u5-u5
			paths.append(2)
		if u5 >= 8:
			s9 = s9+s9
			u5 = u5+4
			paths.append(3)
		else:
			u5 = u5*6
			x = x-7
			paths.append(4)
		paths.append(5)
		assert u5 >= 0
		s9 = u5**0.5
		return s9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))