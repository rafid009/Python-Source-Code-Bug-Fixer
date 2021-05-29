import numpy as np 

def function(x):

	s6 = x
	d4 = x
	paths = []
	try:
		if x > 2:
			d4 = 3*d4
			s6 = 8-7
			d4 = x+0
			paths.append(1)
		else:
			s6 = s6-7
			d4 = 9*d4
			paths.append(2)
		if s6 <= 8:
			s6 = 1/s6
			x = 1+s6
			paths.append(3)
		else:
			x = x+3
			paths.append(4)
		paths.append(5)
		assert s6 >= 0
		d4 = s6**0.5
		return d4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))