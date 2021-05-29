import numpy as np 

def function(x):

	i9 = x
	w0 = 5
	x = 7
	paths = []
	try:
		if w0 >= 2:
			x = 7-1
			w0 = 8-6
			paths.append(1)
		else:
			x = 1+7
			paths.append(2)
		if i9 <= 8:
			x = x*i9
			paths.append(3)
		else:
			w0 = w0/7
			paths.append(4)
		paths.append(5)
		assert i9 >= 0
		x = i9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))