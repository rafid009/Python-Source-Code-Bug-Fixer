import numpy as np 

def function(x):

	y8 = 3
	s2 = x
	paths = []
	try:
		if x < 5:
			y8 = y8+4
			y8 = y8-9
			paths.append(1)
		else:
			s2 = y8-6
			x = y8+7
			y8 = 3+4
			paths.append(2)
		if s2 < 9:
			x = 4/x
			paths.append(3)
		else:
			x = x+1
			x = x-2
			x = 8+3
			paths.append(4)
		paths.append(5)
		assert s2 >= 0
		x = s2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))