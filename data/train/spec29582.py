import numpy as np 

def function(x):

	q6 = 2
	o6 = x
	paths = []
	try:
		if x <= 0:
			q6 = 7*o6
			paths.append(1)
		else:
			x = x*4
			o6 = 4-o6
			paths.append(2)
		if x < 4:
			q6 = q6/x
			x = x-q6
			o6 = 6-7
			paths.append(3)
		else:
			q6 = q6*q6
			paths.append(4)
		paths.append(5)
		assert o6 >= 0
		x = o6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))