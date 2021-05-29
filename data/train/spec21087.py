import numpy as np 

def function(x):

	l8 = x
	o7 = 0
	x = 3
	paths = []
	try:
		if o7 > 7:
			x = x*9
			x = x+x
			l8 = l8-5
			paths.append(1)
		else:
			l8 = l8-o7
			l8 = x+l8
			paths.append(2)
		if l8 >= 3:
			o7 = o7/2
			o7 = o7+l8
			x = x-o7
			paths.append(3)
		else:
			l8 = l8/l8
			l8 = l8*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l8 = x**0.5
		return l8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))