import numpy as np 

def function(x):

	o9 = 4
	i7 = x
	paths = []
	try:
		if x >= 1:
			o9 = 8-o9
			paths.append(1)
		else:
			o9 = o9+5
			x = x/5
			paths.append(2)
		if i7 <= 0:
			x = 7+0
			x = 3*x
			o9 = x/o9
			paths.append(3)
		else:
			i7 = o9-i7
			paths.append(4)
		paths.append(5)
		assert i7 >= 0
		x = i7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))