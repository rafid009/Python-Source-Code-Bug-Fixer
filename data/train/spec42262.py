import numpy as np 

def function(x):

	t4 = x
	y9 = 0
	paths = []
	try:
		if t4 >= 9:
			t4 = t4/x
			paths.append(1)
		else:
			t4 = 9+t4
			paths.append(2)
		if t4 >= 4:
			y9 = y9*3
			x = 8/4
			y9 = x+0
			paths.append(3)
		else:
			t4 = 9/t4
			paths.append(4)
		paths.append(5)
		assert t4 >= 0
		y9 = t4**0.5
		return y9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))