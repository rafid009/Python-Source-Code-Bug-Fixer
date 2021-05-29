import numpy as np 

def function(x):

	k2 = x
	o0 = 0
	paths = []
	try:
		if x > 4:
			x = x-2
			paths.append(1)
		else:
			x = 0+x
			o0 = 0-o0
			o0 = 6*o0
			paths.append(2)
		if k2 <= 8:
			k2 = k2-1
			x = 9*x
			x = x-5
			paths.append(3)
		else:
			x = x*1
			o0 = o0+8
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