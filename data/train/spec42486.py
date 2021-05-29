import numpy as np 

def function(x):

	s4 = x
	d2 = x
	paths = []
	try:
		if x > 0:
			d2 = 8-5
			x = 8-d2
			s4 = 1-s4
			paths.append(1)
		else:
			x = 5-2
			d2 = 8+d2
			paths.append(2)
		if d2 < 5:
			x = 0-x
			s4 = 8-s4
			paths.append(3)
		else:
			x = x*1
			d2 = x+d2
			paths.append(4)
		paths.append(5)
		assert d2 >= 0
		x = d2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))