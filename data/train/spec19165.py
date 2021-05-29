import numpy as np 

def function(x):

	o1 = 6
	l5 = x
	paths = []
	try:
		if l5 <= 1:
			x = 2-o1
			paths.append(1)
		else:
			o1 = l5+o1
			paths.append(2)
		if o1 >= 1:
			o1 = 0+o1
			paths.append(3)
		else:
			x = x+1
			x = x+5
			o1 = o1/2
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