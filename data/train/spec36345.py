import numpy as np 

def function(x):

	c4 = 8
	s1 = 1
	paths = []
	try:
		if s1 < 8:
			x = x-3
			paths.append(1)
		else:
			s1 = s1+s1
			paths.append(2)
		if x > 3:
			s1 = s1/3
			s1 = 3*7
			c4 = 2+c4
			paths.append(3)
		else:
			s1 = x+s1
			s1 = s1*1
			paths.append(4)
		paths.append(5)
		assert s1 >= 0
		x = s1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))