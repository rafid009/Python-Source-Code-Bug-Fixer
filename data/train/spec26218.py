import numpy as np 

def function(x):

	y9 = 3
	v9 = 2
	paths = []
	try:
		if x > 4:
			x = x*2
			x = 5-y9
			v9 = v9*9
			paths.append(1)
		else:
			x = x+8
			v9 = 2/v9
			x = x+x
			paths.append(2)
		if x >= 5:
			y9 = y9/1
			y9 = 5-y9
			x = x/x
			paths.append(3)
		else:
			v9 = x-4
			paths.append(4)
		paths.append(5)
		assert v9 >= 0
		y9 = v9**0.5
		return y9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))