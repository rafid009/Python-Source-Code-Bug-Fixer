import numpy as np 

def function(x):

	s7 = 5
	d7 = x
	paths = []
	try:
		if x < 2:
			s7 = s7+5
			x = d7-0
			s7 = d7*s7
			paths.append(1)
		else:
			d7 = 5/d7
			paths.append(2)
		if s7 < 4:
			s7 = 0*1
			d7 = d7-8
			paths.append(3)
		else:
			s7 = 1*x
			d7 = d7/5
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