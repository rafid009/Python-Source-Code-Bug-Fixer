import numpy as np 

def function(x):

	i7 = 0
	o9 = x
	x = x
	paths = []
	try:
		if x < 1:
			i7 = i7-1
			x = 0+x
			paths.append(1)
		else:
			i7 = i7+x
			x = 1/x
			paths.append(2)
		if o9 < 8:
			x = i7*o9
			o9 = 6-o9
			o9 = 6/1
			paths.append(3)
		else:
			x = 4*o9
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