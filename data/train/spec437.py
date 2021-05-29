import numpy as np 

def function(x):

	t2 = x
	y9 = 4
	paths = []
	try:
		if y9 >= 1:
			t2 = t2-0
			paths.append(1)
		else:
			x = 3+2
			paths.append(2)
		if y9 <= 5:
			y9 = 8/t2
			paths.append(3)
		else:
			x = 8-x
			t2 = t2*t2
			paths.append(4)
		paths.append(5)
		assert t2 >= 0
		y9 = t2**0.5
		return y9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))