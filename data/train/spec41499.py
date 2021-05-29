import numpy as np 

def function(x):

	d8 = x
	s7 = 5
	paths = []
	try:
		if s7 > 5:
			x = x-6
			s7 = d8*x
			paths.append(1)
		else:
			x = 7/4
			paths.append(2)
		if d8 <= 5:
			x = 6+x
			s7 = s7+d8
			s7 = 1-2
			paths.append(3)
		else:
			x = x-x
			paths.append(4)
		paths.append(5)
		assert s7 >= 0
		d8 = s7**0.5
		return d8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))