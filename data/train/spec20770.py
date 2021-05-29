import numpy as np 

def function(x):

	t4 = x
	y9 = 1
	x = 9
	paths = []
	try:
		if x <= 9:
			y9 = t4/y9
			paths.append(1)
		else:
			y9 = y9-3
			t4 = t4-4
			y9 = x+9
			paths.append(2)
		if y9 < 7:
			x = x*y9
			paths.append(3)
		else:
			y9 = y9*7
			x = 5-7
			paths.append(4)
		paths.append(5)
		assert y9 >= 0
		t4 = y9**0.5
		return t4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))