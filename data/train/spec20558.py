import numpy as np 

def function(x):

	s2 = x
	o9 = x
	paths = []
	try:
		if x <= 8:
			o9 = 2-o9
			x = x*4
			x = x+1
			paths.append(1)
		else:
			x = 2/7
			o9 = o9+0
			paths.append(2)
		if s2 < 0:
			s2 = 6/s2
			x = o9*x
			paths.append(3)
		else:
			o9 = 4/o9
			o9 = 0/o9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o9 = x**0.5
		return o9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))