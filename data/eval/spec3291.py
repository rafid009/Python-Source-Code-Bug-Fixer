import numpy as np 

def function(x):

	o1 = 1
	o7 = x
	paths = []
	try:
		if x <= 6:
			o1 = o1+o1
			paths.append(1)
		else:
			o1 = 6-o7
			o1 = 1/o1
			paths.append(2)
		if x > 5:
			o1 = o7-o1
			paths.append(3)
		else:
			o1 = o7+o1
			o1 = o1*5
			x = x+x
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