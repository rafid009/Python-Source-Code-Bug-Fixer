import numpy as np 

def function(x):

	o7 = 8
	l4 = 7
	paths = []
	try:
		if x > 0:
			x = x*6
			paths.append(1)
		else:
			o7 = 6-o7
			paths.append(2)
		if x > 3:
			l4 = l4-0
			o7 = o7*o7
			paths.append(3)
		else:
			o7 = o7+x
			l4 = 4-5
			x = l4/1
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