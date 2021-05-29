import numpy as np 

def function(x):

	t1 = x
	y9 = x
	paths = []
	try:
		if y9 > 9:
			t1 = x+0
			x = x-1
			paths.append(1)
		else:
			x = x/7
			x = x+2
			paths.append(2)
		if x > 2:
			t1 = t1*3
			paths.append(3)
		else:
			y9 = 0-9
			x = 5/3
			y9 = y9-4
			paths.append(4)
		paths.append(5)
		assert y9 >= 0
		x = y9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))