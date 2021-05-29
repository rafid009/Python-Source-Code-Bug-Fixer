import numpy as np 

def function(x):

	l0 = 8
	o4 = x
	paths = []
	try:
		if x < 8:
			x = x+9
			o4 = o4+2
			paths.append(1)
		else:
			x = o4-x
			l0 = l0-0
			paths.append(2)
		if x > 5:
			o4 = l0*o4
			l0 = 0*l0
			o4 = o4-1
			paths.append(3)
		else:
			l0 = l0+x
			o4 = 9-2
			o4 = o4*8
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