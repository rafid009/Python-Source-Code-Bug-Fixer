import numpy as np 

def function(x):

	l7 = x
	o1 = 5
	paths = []
	try:
		if l7 >= 8:
			o1 = o1*o1
			l7 = l7/7
			paths.append(1)
		else:
			x = x-o1
			paths.append(2)
		if l7 > 0:
			l7 = l7+l7
			l7 = 5/l7
			x = 9*x
			paths.append(3)
		else:
			l7 = l7-2
			o1 = 8-l7
			x = 0*l7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o1 = x**0.5
		return o1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))