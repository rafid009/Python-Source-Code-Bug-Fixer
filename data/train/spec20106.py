import numpy as np 

def function(x):

	o6 = x
	r1 = 3
	paths = []
	try:
		if o6 <= 0:
			x = x/7
			paths.append(1)
		else:
			x = o6/2
			paths.append(2)
		if x < 0:
			x = x-9
			paths.append(3)
		else:
			r1 = r1+6
			r1 = r1*9
			x = 0+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r1 = x**0.5
		return r1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))