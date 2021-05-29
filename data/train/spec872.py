import numpy as np 

def function(x):

	s0 = x
	d0 = 5
	paths = []
	try:
		if s0 >= 8:
			d0 = s0/d0
			paths.append(1)
		else:
			d0 = x-d0
			s0 = d0/s0
			paths.append(2)
		if x <= 3:
			x = x/1
			s0 = 2/s0
			d0 = 1*5
			paths.append(3)
		else:
			x = 6+x
			s0 = s0*s0
			paths.append(4)
		paths.append(5)
		assert s0 >= 0
		d0 = s0**0.5
		return d0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))