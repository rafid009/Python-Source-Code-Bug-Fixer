import numpy as np 

def function(x):

	o0 = 3
	x8 = x
	paths = []
	try:
		if x8 > 8:
			o0 = o0*4
			paths.append(1)
		else:
			x = x-4
			x8 = x8-6
			x = 5-1
			paths.append(2)
		if o0 < 5:
			o0 = o0-o0
			o0 = o0/8
			x = 4+x
			paths.append(3)
		else:
			o0 = 2+1
			x = 5-x
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