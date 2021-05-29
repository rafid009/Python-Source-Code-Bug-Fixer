import numpy as np 

def function(x):

	h8 = x
	k1 = 2
	paths = []
	try:
		if h8 > 7:
			x = x/x
			paths.append(1)
		else:
			k1 = k1/h8
			x = 7-9
			paths.append(2)
		if k1 <= 1:
			x = h8-k1
			x = x/1
			paths.append(3)
		else:
			k1 = 1-k1
			paths.append(4)
		paths.append(5)
		assert h8 >= 0
		x = h8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))