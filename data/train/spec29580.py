import numpy as np 

def function(x):

	s4 = 5
	r5 = 0
	paths = []
	try:
		if r5 > 0:
			x = x/s4
			s4 = 4/s4
			paths.append(1)
		else:
			r5 = s4*s4
			paths.append(2)
		if x > 2:
			s4 = 1/s4
			r5 = r5*5
			paths.append(3)
		else:
			r5 = r5-9
			x = x+5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r5 = x**0.5
		return r5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))