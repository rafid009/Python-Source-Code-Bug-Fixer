import numpy as np 

def function(x):

	n6 = x
	o1 = x
	paths = []
	try:
		if x > 1:
			x = x/o1
			n6 = 8-n6
			n6 = n6+8
			paths.append(1)
		else:
			x = x/o1
			x = o1+x
			paths.append(2)
		if x < 2:
			x = x-2
			paths.append(3)
		else:
			o1 = 1*0
			x = 3-x
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