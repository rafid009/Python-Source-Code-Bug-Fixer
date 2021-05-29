import numpy as np 

def function(x):

	s9 = 0
	y7 = 8
	paths = []
	try:
		if x <= 6:
			s9 = 7/x
			paths.append(1)
		else:
			x = x-4
			paths.append(2)
		if y7 <= 1:
			x = 7+5
			x = y7/x
			s9 = s9*x
			paths.append(3)
		else:
			y7 = 6+y7
			y7 = y7*2
			y7 = y7/x
			paths.append(4)
		paths.append(5)
		assert y7 >= 0
		x = y7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))