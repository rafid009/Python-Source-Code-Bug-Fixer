import numpy as np 

def function(x):

	r8 = x
	y9 = 7
	paths = []
	try:
		if x > 0:
			y9 = y9+r8
			paths.append(1)
		else:
			x = 0+x
			y9 = r8*y9
			paths.append(2)
		if r8 <= 8:
			y9 = y9/3
			y9 = 0*x
			paths.append(3)
		else:
			r8 = r8-2
			r8 = 7/x
			paths.append(4)
		paths.append(5)
		assert r8 >= 0
		x = r8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))