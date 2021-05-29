import numpy as np 

def function(x):

	d0 = 8
	s1 = x
	paths = []
	try:
		if d0 < 4:
			x = 1-x
			x = 9+x
			paths.append(1)
		else:
			s1 = 2+x
			s1 = s1*1
			paths.append(2)
		if s1 > 7:
			d0 = d0*d0
			s1 = s1-s1
			paths.append(3)
		else:
			s1 = s1-1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d0 = x**0.5
		return d0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))