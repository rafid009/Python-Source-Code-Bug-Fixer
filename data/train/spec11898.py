import numpy as np 

def function(x):

	f9 = x
	o0 = x
	paths = []
	try:
		if f9 <= 5:
			f9 = f9*x
			paths.append(1)
		else:
			x = x-1
			x = 4/2
			f9 = f9/7
			paths.append(2)
		if f9 <= 9:
			o0 = x+0
			x = 3-5
			paths.append(3)
		else:
			o0 = o0*1
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