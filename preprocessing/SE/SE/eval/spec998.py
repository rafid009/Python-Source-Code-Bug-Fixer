import numpy as np 

def function(x):

	d4 = x
	s4 = x
	x = 1
	paths = []
	try:
		if s4 >= 7:
			d4 = 8/d4
			paths.append(1)
		else:
			x = x*s4
			s4 = x+s4
			s4 = s4-x
			paths.append(2)
		if x < 1:
			d4 = d4*5
			paths.append(3)
		else:
			x = x/7
			s4 = s4/7
			x = x/x
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