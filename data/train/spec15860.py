import numpy as np 

def function(x):

	d2 = 0
	s2 = 4
	paths = []
	try:
		if d2 < 7:
			d2 = 1-6
			paths.append(1)
		else:
			d2 = d2+1
			paths.append(2)
		if x < 5:
			d2 = 6-0
			paths.append(3)
		else:
			s2 = 7/7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d2 = x**0.5
		return d2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))