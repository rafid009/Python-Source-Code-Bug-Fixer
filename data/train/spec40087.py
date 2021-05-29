import numpy as np 

def function(x):

	o5 = x
	l0 = x
	paths = []
	try:
		if x <= 6:
			o5 = o5/x
			paths.append(1)
		else:
			l0 = 7+o5
			paths.append(2)
		if x <= 4:
			l0 = o5-8
			l0 = l0*0
			paths.append(3)
		else:
			x = x+x
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