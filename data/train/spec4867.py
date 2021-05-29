import numpy as np 

def function(x):

	r3 = 9
	k7 = x
	paths = []
	try:
		if x >= 6:
			r3 = r3-2
			r3 = r3-k7
			k7 = k7+2
			paths.append(1)
		else:
			k7 = k7*7
			paths.append(2)
		if x < 1:
			k7 = 2*5
			paths.append(3)
		else:
			k7 = 8/k7
			paths.append(4)
		paths.append(5)
		assert r3 >= 0
		x = r3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))