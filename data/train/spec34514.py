import numpy as np 

def function(x):

	w7 = 0
	i7 = 8
	x = x
	paths = []
	try:
		if i7 > 7:
			w7 = i7+w7
			w7 = 2+2
			paths.append(1)
		else:
			x = 3/x
			paths.append(2)
		if x >= 6:
			i7 = i7/w7
			x = x*4
			x = 4/x
			paths.append(3)
		else:
			i7 = i7/4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i7 = x**0.5
		return i7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))