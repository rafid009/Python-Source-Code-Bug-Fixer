import numpy as np 

def function(x):

	i2 = x
	o1 = 7
	paths = []
	try:
		if o1 >= 1:
			x = x/o1
			o1 = 9-o1
			paths.append(1)
		else:
			o1 = o1-5
			x = x+5
			paths.append(2)
		if x >= 4:
			i2 = i2+5
			x = x-4
			x = i2/x
			paths.append(3)
		else:
			i2 = 9-i2
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