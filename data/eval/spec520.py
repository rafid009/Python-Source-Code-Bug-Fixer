import numpy as np 

def function(x):

	r6 = 8
	f9 = 8
	paths = []
	try:
		if f9 <= 8:
			f9 = f9+2
			x = r6*f9
			paths.append(1)
		else:
			f9 = r6+f9
			x = x*5
			paths.append(2)
		if f9 < 5:
			x = 0*x
			paths.append(3)
		else:
			x = r6-x
			f9 = 5-f9
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