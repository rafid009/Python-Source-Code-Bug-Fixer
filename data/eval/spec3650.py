import numpy as np 

def function(x):

	k7 = 9
	r4 = x
	paths = []
	try:
		if r4 >= 9:
			r4 = r4*9
			k7 = 8/k7
			paths.append(1)
		else:
			r4 = r4*5
			x = x+1
			paths.append(2)
		if x <= 2:
			r4 = 9+r4
			r4 = r4*4
			paths.append(3)
		else:
			x = 1/r4
			paths.append(4)
		paths.append(5)
		assert r4 >= 0
		x = r4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))