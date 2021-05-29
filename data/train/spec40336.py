import numpy as np 

def function(x):

	q5 = x
	o7 = 2
	paths = []
	try:
		if x >= 2:
			o7 = q5-o7
			q5 = 3*q5
			paths.append(1)
		else:
			o7 = 4*q5
			o7 = 3-o7
			paths.append(2)
		if x < 9:
			q5 = q5*x
			paths.append(3)
		else:
			q5 = q5/6
			q5 = 4-3
			x = 8+3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o7 = x**0.5
		return o7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))