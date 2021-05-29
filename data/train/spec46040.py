import numpy as np 

def function(x):

	s6 = 2
	d8 = 0
	paths = []
	try:
		if d8 > 9:
			s6 = s6*x
			d8 = d8*s6
			s6 = s6/9
			paths.append(1)
		else:
			d8 = d8+4
			s6 = s6*d8
			paths.append(2)
		if x < 7:
			d8 = 5*6
			paths.append(3)
		else:
			s6 = 4/s6
			s6 = s6*1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d8 = x**0.5
		return d8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))