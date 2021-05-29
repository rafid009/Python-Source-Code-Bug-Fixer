import numpy as np 

def function(x):

	s2 = 0
	y4 = x
	paths = []
	try:
		if s2 >= 4:
			x = x+y4
			paths.append(1)
		else:
			s2 = s2/y4
			s2 = s2-8
			s2 = x*5
			paths.append(2)
		if y4 > 7:
			x = x*6
			s2 = s2-s2
			paths.append(3)
		else:
			y4 = x-s2
			x = 1/x
			paths.append(4)
		paths.append(5)
		assert s2 >= 0
		y4 = s2**0.5
		return y4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))