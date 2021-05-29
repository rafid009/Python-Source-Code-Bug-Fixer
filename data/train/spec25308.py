import numpy as np 

def function(x):

	s7 = x
	d4 = 9
	paths = []
	try:
		if s7 < 7:
			x = x+d4
			x = x+s7
			paths.append(1)
		else:
			x = 5+x
			s7 = s7-5
			paths.append(2)
		if x <= 8:
			s7 = s7-s7
			paths.append(3)
		else:
			d4 = 0-1
			d4 = 7+7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d4 = x**0.5
		return d4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))