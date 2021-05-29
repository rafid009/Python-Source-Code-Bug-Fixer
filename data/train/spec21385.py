import numpy as np 

def function(x):

	y9 = 2
	t1 = 5
	paths = []
	try:
		if x < 7:
			y9 = 8/y9
			x = x*4
			x = 1+x
			paths.append(1)
		else:
			y9 = y9-y9
			t1 = 1-t1
			paths.append(2)
		if y9 > 7:
			y9 = x+4
			x = 5-x
			paths.append(3)
		else:
			t1 = 2-t1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t1 = x**0.5
		return t1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))