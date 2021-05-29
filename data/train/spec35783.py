import numpy as np 

def function(x):

	s9 = x
	y2 = x
	paths = []
	try:
		if y2 >= 3:
			s9 = 7+s9
			y2 = 9/3
			y2 = 6*9
			paths.append(1)
		else:
			x = 8*7
			paths.append(2)
		if s9 >= 2:
			x = y2-x
			x = x-y2
			y2 = s9-0
			paths.append(3)
		else:
			y2 = y2*y2
			paths.append(4)
		paths.append(5)
		assert s9 >= 0
		y2 = s9**0.5
		return y2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))