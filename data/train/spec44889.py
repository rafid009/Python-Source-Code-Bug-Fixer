import numpy as np 

def function(x):

	r7 = 4
	o1 = 5
	paths = []
	try:
		if x >= 7:
			r7 = o1-9
			paths.append(1)
		else:
			r7 = o1-r7
			o1 = 2*o1
			paths.append(2)
		if o1 > 5:
			r7 = r7*9
			paths.append(3)
		else:
			o1 = r7/o1
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