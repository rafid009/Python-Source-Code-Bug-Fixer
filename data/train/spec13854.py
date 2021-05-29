import numpy as np 

def function(x):

	s9 = 7
	f9 = x
	x = x
	paths = []
	try:
		if s9 < 4:
			x = x-3
			x = 7/x
			x = x/7
			paths.append(1)
		else:
			s9 = s9/5
			s9 = 0/s9
			s9 = s9*s9
			paths.append(2)
		if f9 > 3:
			x = x-0
			s9 = s9-0
			paths.append(3)
		else:
			f9 = 0+f9
			s9 = 1-x
			x = 3+x
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