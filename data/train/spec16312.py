import numpy as np 

def function(x):

	o0 = x
	b7 = x
	paths = []
	try:
		if o0 < 8:
			o0 = o0+8
			b7 = b7-7
			paths.append(1)
		else:
			o0 = o0/o0
			b7 = b7+1
			paths.append(2)
		if x >= 9:
			b7 = o0+6
			paths.append(3)
		else:
			b7 = 3/9
			x = x/6
			x = b7/x
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