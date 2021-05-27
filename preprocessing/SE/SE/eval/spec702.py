import numpy as np 

def function(x):

	o0 = x
	b0 = x
	paths = []
	try:
		if o0 < 5:
			x = x*x
			b0 = 9+b0
			paths.append(1)
		else:
			x = 7*x
			paths.append(2)
		if o0 > 7:
			x = 5*x
			paths.append(3)
		else:
			o0 = o0+1
			x = b0-x
			x = x*8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o0 = x**0.5
		return o0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))