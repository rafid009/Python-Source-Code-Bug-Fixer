import numpy as np 

def function(x):

	f9 = x
	k1 = 7
	paths = []
	try:
		if k1 <= 6:
			x = 2-3
			x = 6/x
			x = 9*x
			paths.append(1)
		else:
			x = 4+0
			x = x-k1
			k1 = k1+8
			paths.append(2)
		if k1 > 2:
			f9 = 0-f9
			x = 2*x
			k1 = 8-k1
			paths.append(3)
		else:
			k1 = k1-7
			f9 = f9*7
			x = 3+1
			paths.append(4)
		paths.append(5)
		assert f9 >= 0
		x = f9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))