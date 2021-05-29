import numpy as np 

def function(x):

	o8 = x
	q5 = 3
	paths = []
	try:
		if q5 < 8:
			o8 = o8*8
			paths.append(1)
		else:
			x = x*6
			x = 0-x
			paths.append(2)
		if o8 > 4:
			o8 = x/8
			paths.append(3)
		else:
			q5 = q5-0
			o8 = o8*7
			q5 = 6*q5
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