import numpy as np 

def function(x):

	r4 = x
	o1 = x
	paths = []
	try:
		if x >= 4:
			o1 = 6*r4
			paths.append(1)
		else:
			r4 = r4-2
			paths.append(2)
		if o1 >= 2:
			x = x+x
			paths.append(3)
		else:
			o1 = 9+r4
			paths.append(4)
		paths.append(5)
		assert o1 >= 0
		x = o1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))