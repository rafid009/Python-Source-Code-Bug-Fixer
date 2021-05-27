import numpy as np 

def function(x):

	i9 = 1
	w3 = 5
	paths = []
	try:
		if i9 >= 9:
			i9 = 1-i9
			w3 = x/w3
			paths.append(1)
		else:
			i9 = w3-6
			paths.append(2)
		if w3 >= 2:
			x = x*7
			x = x/i9
			paths.append(3)
		else:
			x = w3+w3
			x = x/i9
			i9 = i9*i9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i9 = x**0.5
		return i9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))