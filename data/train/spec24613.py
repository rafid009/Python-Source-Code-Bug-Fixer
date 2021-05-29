import numpy as np 

def function(x):

	o8 = x
	s9 = x
	paths = []
	try:
		if s9 >= 5:
			x = s9-4
			o8 = s9+o8
			paths.append(1)
		else:
			o8 = 1+o8
			paths.append(2)
		if o8 <= 8:
			s9 = 6*1
			paths.append(3)
		else:
			x = x/2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))