import numpy as np 

def function(x):

	i7 = 2
	w7 = 4
	paths = []
	try:
		if i7 >= 2:
			i7 = 1+i7
			paths.append(1)
		else:
			x = x/i7
			x = 9+x
			i7 = 8*i7
			paths.append(2)
		if w7 < 1:
			w7 = 3+8
			i7 = 0/2
			paths.append(3)
		else:
			w7 = i7-9
			paths.append(4)
		paths.append(5)
		assert w7 >= 0
		x = w7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))