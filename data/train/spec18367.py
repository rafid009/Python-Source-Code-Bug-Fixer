import numpy as np 

def function(x):

	s4 = 9
	d9 = x
	paths = []
	try:
		if x < 9:
			x = 0+x
			d9 = d9+s4
			paths.append(1)
		else:
			d9 = 3-5
			x = x-1
			s4 = 9+s4
			paths.append(2)
		if d9 >= 4:
			d9 = d9-0
			paths.append(3)
		else:
			d9 = 4/d9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d9 = x**0.5
		return d9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))