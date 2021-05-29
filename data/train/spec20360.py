import numpy as np 

def function(x):

	o4 = 3
	l5 = x
	x = 2
	paths = []
	try:
		if l5 < 2:
			l5 = l5+4
			x = 2*x
			x = x+x
			paths.append(1)
		else:
			o4 = o4+9
			paths.append(2)
		if l5 >= 7:
			x = x-o4
			o4 = 2/9
			o4 = 2/o4
			paths.append(3)
		else:
			o4 = 9*x
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