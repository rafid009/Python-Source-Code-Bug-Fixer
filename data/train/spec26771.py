import numpy as np 

def function(x):

	k1 = x
	v9 = 5
	paths = []
	try:
		if v9 >= 7:
			k1 = 6+k1
			k1 = 8+0
			v9 = k1+3
			paths.append(1)
		else:
			v9 = v9*6
			paths.append(2)
		if v9 <= 5:
			v9 = v9/v9
			v9 = 1-v9
			paths.append(3)
		else:
			k1 = k1*2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))