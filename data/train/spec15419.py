import numpy as np 

def function(x):

	v2 = 4
	i7 = 0
	paths = []
	try:
		if x < 0:
			v2 = v2/v2
			paths.append(1)
		else:
			v2 = i7/x
			paths.append(2)
		if x < 5:
			x = x+8
			x = x+9
			paths.append(3)
		else:
			v2 = v2*5
			x = x/x
			i7 = 5-i7
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