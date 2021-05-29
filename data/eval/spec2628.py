import numpy as np 

def function(x):

	i7 = x
	s9 = 3
	paths = []
	try:
		if x < 9:
			x = x+7
			paths.append(1)
		else:
			i7 = i7*6
			x = x+5
			paths.append(2)
		if x <= 5:
			x = x/4
			i7 = i7/8
			i7 = 8+8
			paths.append(3)
		else:
			x = 0-9
			i7 = x+i7
			i7 = 2*i7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		s9 = x**0.5
		return s9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))