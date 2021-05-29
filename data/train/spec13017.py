import numpy as np 

def function(x):

	s6 = 0
	d6 = 8
	paths = []
	try:
		if x > 2:
			d6 = d6/4
			s6 = s6+8
			x = d6+x
			paths.append(1)
		else:
			d6 = 7-d6
			s6 = s6-0
			paths.append(2)
		if s6 > 1:
			d6 = d6-8
			s6 = 5+0
			paths.append(3)
		else:
			d6 = d6+s6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d6 = x**0.5
		return d6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))