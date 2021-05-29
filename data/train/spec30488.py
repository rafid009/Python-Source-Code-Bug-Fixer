import numpy as np 

def function(x):

	o9 = 3
	m2 = 4
	paths = []
	try:
		if m2 <= 1:
			m2 = o9*3
			x = x*4
			paths.append(1)
		else:
			o9 = 9+o9
			o9 = 4/o9
			o9 = 6/o9
			paths.append(2)
		if x >= 3:
			o9 = 8/7
			paths.append(3)
		else:
			o9 = 9+7
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