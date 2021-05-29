import numpy as np 

def function(x):

	s1 = 6
	d2 = 0
	paths = []
	try:
		if x >= 2:
			d2 = d2*0
			paths.append(1)
		else:
			x = 1*x
			paths.append(2)
		if s1 > 2:
			s1 = s1*s1
			paths.append(3)
		else:
			d2 = d2+6
			x = s1/6
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