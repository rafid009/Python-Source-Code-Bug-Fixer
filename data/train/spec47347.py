import numpy as np 

def function(x):

	y9 = 0
	t5 = 4
	paths = []
	try:
		if x > 7:
			y9 = y9-1
			paths.append(1)
		else:
			t5 = y9/4
			paths.append(2)
		if t5 > 0:
			t5 = t5/2
			paths.append(3)
		else:
			y9 = y9*2
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