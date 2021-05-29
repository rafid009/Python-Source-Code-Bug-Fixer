import numpy as np 

def function(x):

	f9 = 9
	s7 = x
	paths = []
	try:
		if x > 6:
			x = x*0
			s7 = 1-6
			x = 6*f9
			paths.append(1)
		else:
			f9 = 7+x
			x = s7/9
			paths.append(2)
		if x > 6:
			f9 = 9+f9
			paths.append(3)
		else:
			s7 = f9-s7
			f9 = f9-3
			f9 = 1-s7
			paths.append(4)
		paths.append(5)
		assert s7 >= 0
		x = s7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))