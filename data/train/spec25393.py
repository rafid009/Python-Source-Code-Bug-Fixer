import numpy as np 

def function(x):

	i3 = x
	w3 = 5
	paths = []
	try:
		if x > 5:
			i3 = 3-i3
			paths.append(1)
		else:
			w3 = i3*x
			x = x-i3
			paths.append(2)
		if i3 < 5:
			i3 = 1+w3
			x = 7-i3
			x = x-3
			paths.append(3)
		else:
			i3 = x/1
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