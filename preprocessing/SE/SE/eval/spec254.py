import numpy as np 

def function(x):

	j6 = 7
	s4 = 4
	x = x
	paths = []
	try:
		if x < 8:
			j6 = x+4
			paths.append(1)
		else:
			x = x+s4
			paths.append(2)
		if s4 <= 8:
			j6 = 1/7
			paths.append(3)
		else:
			j6 = 9-j6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j6 = x**0.5
		return j6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))