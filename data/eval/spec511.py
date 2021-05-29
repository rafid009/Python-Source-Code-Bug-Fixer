import numpy as np 

def function(x):

	y9 = x
	f2 = 2
	paths = []
	try:
		if x < 1:
			x = x+8
			paths.append(1)
		else:
			f2 = 0/9
			x = 2-x
			f2 = y9+f2
			paths.append(2)
		if x > 1:
			y9 = y9-4
			y9 = y9+f2
			paths.append(3)
		else:
			f2 = x+5
			paths.append(4)
		paths.append(5)
		assert f2 >= 0
		f2 = f2**0.5
		return f2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))