import numpy as np 

def function(x):

	m2 = x
	o8 = 4
	paths = []
	try:
		if x <= 8:
			x = x/8
			o8 = m2+o8
			o8 = o8/o8
			paths.append(1)
		else:
			x = x+7
			o8 = o8/9
			paths.append(2)
		if x > 9:
			x = x+4
			o8 = 2-o8
			paths.append(3)
		else:
			x = 2*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))