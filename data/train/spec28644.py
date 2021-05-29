import numpy as np 

def function(x):

	s4 = x
	d2 = 2
	paths = []
	try:
		if x >= 1:
			x = 9+x
			paths.append(1)
		else:
			d2 = 9*d2
			s4 = s4-3
			x = s4/2
			paths.append(2)
		if d2 < 7:
			s4 = 8+s4
			x = s4+x
			d2 = d2/9
			paths.append(3)
		else:
			x = d2*s4
			s4 = 2/s4
			d2 = 4+s4
			paths.append(4)
		paths.append(5)
		assert s4 >= 0
		x = s4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))