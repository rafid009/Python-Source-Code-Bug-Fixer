import numpy as np 

def function(x):

	s7 = x
	f8 = x
	paths = []
	try:
		if x > 5:
			x = x+9
			x = x*3
			paths.append(1)
		else:
			f8 = 5-f8
			f8 = s7/f8
			f8 = f8/f8
			paths.append(2)
		if x >= 9:
			x = x-1
			paths.append(3)
		else:
			s7 = s7*s7
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