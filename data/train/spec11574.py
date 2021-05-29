import numpy as np 

def function(x):

	y9 = 0
	t3 = 7
	paths = []
	try:
		if x > 4:
			x = x/2
			paths.append(1)
		else:
			y9 = t3-5
			x = x-t3
			y9 = x/y9
			paths.append(2)
		if t3 < 5:
			y9 = y9-x
			paths.append(3)
		else:
			x = x+5
			x = x*9
			t3 = 6+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y9 = x**0.5
		return y9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))