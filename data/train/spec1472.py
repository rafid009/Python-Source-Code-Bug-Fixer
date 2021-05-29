import numpy as np 

def function(x):

	k7 = x
	o1 = 7
	paths = []
	try:
		if x > 0:
			x = k7/x
			o1 = 9*o1
			paths.append(1)
		else:
			x = x*3
			o1 = o1*4
			paths.append(2)
		if o1 <= 1:
			k7 = o1+6
			k7 = x-8
			x = k7+x
			paths.append(3)
		else:
			k7 = x+3
			k7 = 1/x
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