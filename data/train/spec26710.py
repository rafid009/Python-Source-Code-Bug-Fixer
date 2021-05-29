import numpy as np 

def function(x):

	k2 = 6
	w9 = x
	paths = []
	try:
		if k2 >= 9:
			w9 = w9*8
			paths.append(1)
		else:
			x = k2+x
			paths.append(2)
		if w9 < 7:
			x = x*w9
			x = 1+x
			paths.append(3)
		else:
			k2 = w9+0
			paths.append(4)
		paths.append(5)
		assert w9 >= 0
		x = w9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))