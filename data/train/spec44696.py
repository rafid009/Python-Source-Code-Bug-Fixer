import numpy as np 

def function(x):

	y6 = 4
	s1 = x
	paths = []
	try:
		if x > 7:
			y6 = x/y6
			y6 = 9-1
			paths.append(1)
		else:
			y6 = y6+x
			x = 2-x
			paths.append(2)
		if y6 >= 2:
			x = 6+0
			y6 = y6+8
			s1 = 3-2
			paths.append(3)
		else:
			s1 = s1+y6
			x = x+x
			y6 = s1+y6
			paths.append(4)
		paths.append(5)
		assert y6 >= 0
		s1 = y6**0.5
		return s1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))