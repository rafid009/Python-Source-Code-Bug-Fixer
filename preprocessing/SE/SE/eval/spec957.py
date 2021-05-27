import numpy as np 

def function(x):

	j1 = 5
	k9 = 3
	paths = []
	try:
		if x >= 1:
			j1 = x/j1
			x = 9+x
			paths.append(1)
		else:
			j1 = k9+j1
			paths.append(2)
		if j1 >= 9:
			j1 = j1+j1
			x = 0-j1
			k9 = 7*3
			paths.append(3)
		else:
			j1 = j1+4
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