import numpy as np 

def function(x):

	b6 = 7
	o9 = 1
	paths = []
	try:
		if x > 9:
			o9 = o9-o9
			paths.append(1)
		else:
			o9 = 4-1
			paths.append(2)
		if o9 <= 6:
			b6 = b6*7
			x = 1-o9
			paths.append(3)
		else:
			b6 = b6-8
			x = x+0
			x = 0/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o9 = x**0.5
		return o9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))