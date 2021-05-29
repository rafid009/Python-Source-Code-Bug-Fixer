import numpy as np 

def function(x):

	s4 = 8
	y4 = x
	paths = []
	try:
		if s4 < 4:
			x = 7+y4
			s4 = 3-s4
			paths.append(1)
		else:
			y4 = s4+x
			paths.append(2)
		if y4 >= 5:
			y4 = y4-2
			paths.append(3)
		else:
			x = x+s4
			x = 2*x
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