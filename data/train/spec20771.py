import numpy as np 

def function(x):

	s6 = x
	d9 = x
	x = x
	paths = []
	try:
		if x < 4:
			s6 = s6*2
			paths.append(1)
		else:
			x = x+1
			x = 3-3
			d9 = 5-d9
			paths.append(2)
		if d9 < 0:
			d9 = d9*1
			d9 = d9+d9
			paths.append(3)
		else:
			d9 = x-4
			x = x+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		s6 = x**0.5
		return s6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))