import numpy as np 

def function(x):

	s0 = x
	v5 = x
	paths = []
	try:
		if v5 >= 8:
			x = x*2
			s0 = 1*s0
			paths.append(1)
		else:
			v5 = v5/s0
			v5 = 1/v5
			paths.append(2)
		if x <= 1:
			s0 = s0*x
			x = x+6
			paths.append(3)
		else:
			x = v5+v5
			v5 = 6-3
			s0 = s0/4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v5 = x**0.5
		return v5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))