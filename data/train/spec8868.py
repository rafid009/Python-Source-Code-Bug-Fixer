import numpy as np 

def function(x):

	s2 = 4
	y4 = 5
	paths = []
	try:
		if y4 <= 6:
			s2 = s2/y4
			paths.append(1)
		else:
			y4 = x-7
			x = x*2
			y4 = 7/3
			paths.append(2)
		if x >= 5:
			y4 = y4-9
			paths.append(3)
		else:
			y4 = y4-0
			s2 = s2-8
			s2 = 2/8
			paths.append(4)
		paths.append(5)
		assert y4 >= 0
		x = y4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))