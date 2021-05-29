import numpy as np 

def function(x):

	s6 = 9
	n5 = 9
	paths = []
	try:
		if n5 < 3:
			s6 = 0/s6
			paths.append(1)
		else:
			s6 = x/n5
			paths.append(2)
		if n5 >= 4:
			n5 = x+0
			s6 = 2+9
			n5 = n5*s6
			paths.append(3)
		else:
			x = s6-2
			paths.append(4)
		paths.append(5)
		assert n5 >= 0
		s6 = n5**0.5
		return s6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))