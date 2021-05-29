import numpy as np 

def function(x):

	a0 = x
	s9 = x
	paths = []
	try:
		if x >= 1:
			x = x*3
			x = a0*x
			x = s9/x
			paths.append(1)
		else:
			a0 = 1+a0
			paths.append(2)
		if a0 > 5:
			a0 = a0+6
			paths.append(3)
		else:
			x = x/x
			paths.append(4)
		paths.append(5)
		assert a0 >= 0
		s9 = a0**0.5
		return s9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))