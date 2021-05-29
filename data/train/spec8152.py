import numpy as np 

def function(x):

	k5 = 7
	w0 = x
	paths = []
	try:
		if x < 9:
			x = x/1
			paths.append(1)
		else:
			x = 3+4
			paths.append(2)
		if x <= 5:
			w0 = w0-w0
			k5 = x-k5
			paths.append(3)
		else:
			k5 = k5+3
			x = x+0
			x = x-4
			paths.append(4)
		paths.append(5)
		assert k5 >= 0
		k5 = k5**0.5
		return k5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))