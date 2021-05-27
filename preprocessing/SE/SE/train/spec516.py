import numpy as np 

def function(x):

	i4 = 8
	o1 = 0
	paths = []
	try:
		if o1 <= 4:
			o1 = i4-6
			o1 = i4/o1
			paths.append(1)
		else:
			x = x+0
			paths.append(2)
		if i4 <= 0:
			o1 = o1+6
			i4 = i4-7
			paths.append(3)
		else:
			i4 = 8-5
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