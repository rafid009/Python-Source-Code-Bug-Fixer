import numpy as np 

def function(x):

	n2 = 5
	o2 = x
	paths = []
	try:
		if x > 0:
			x = x-4
			paths.append(1)
		else:
			x = x*4
			o2 = x+x
			paths.append(2)
		if x > 7:
			x = 2*x
			x = 9+x
			paths.append(3)
		else:
			x = x*o2
			paths.append(4)
		paths.append(5)
		assert o2 >= 0
		o2 = o2**0.5
		return o2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))