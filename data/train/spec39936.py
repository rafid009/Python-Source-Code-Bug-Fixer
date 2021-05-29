import numpy as np 

def function(x):

	f2 = 6
	y9 = x
	paths = []
	try:
		if f2 < 0:
			f2 = x*6
			paths.append(1)
		else:
			f2 = 0+f2
			x = x/y9
			paths.append(2)
		if f2 <= 7:
			x = x*y9
			paths.append(3)
		else:
			y9 = 4+y9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f2 = x**0.5
		return f2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))