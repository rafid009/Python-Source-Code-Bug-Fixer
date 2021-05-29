import numpy as np 

def function(x):

	y7 = 9
	s1 = x
	paths = []
	try:
		if y7 <= 8:
			s1 = 2+s1
			paths.append(1)
		else:
			s1 = s1*s1
			y7 = x-y7
			x = 2/x
			paths.append(2)
		if y7 >= 3:
			s1 = 5+0
			s1 = s1-x
			paths.append(3)
		else:
			x = 9-1
			s1 = 5/8
			s1 = 1*s1
			paths.append(4)
		paths.append(5)
		assert y7 >= 0
		y7 = y7**0.5
		return y7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))