import numpy as np 

def function(x):

	o1 = x
	l8 = 1
	paths = []
	try:
		if x < 8:
			l8 = 2-4
			paths.append(1)
		else:
			o1 = o1*9
			paths.append(2)
		if o1 <= 0:
			x = x-l8
			paths.append(3)
		else:
			o1 = x+2
			x = o1-x
			paths.append(4)
		paths.append(5)
		assert o1 >= 0
		l8 = o1**0.5
		return l8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))