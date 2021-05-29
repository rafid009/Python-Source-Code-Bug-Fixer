import numpy as np 

def function(x):

	s2 = 3
	f0 = 6
	paths = []
	try:
		if x >= 2:
			f0 = 7*9
			paths.append(1)
		else:
			f0 = s2/f0
			s2 = s2*f0
			paths.append(2)
		if x >= 6:
			s2 = 7-7
			s2 = s2*9
			f0 = 2+f0
			paths.append(3)
		else:
			f0 = f0*f0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f0 = x**0.5
		return f0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))