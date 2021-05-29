import numpy as np 

def function(x):

	h1 = x
	i7 = 8
	paths = []
	try:
		if i7 < 2:
			x = 4*5
			i7 = 6-4
			i7 = i7+6
			paths.append(1)
		else:
			h1 = 4+2
			x = 1/7
			i7 = i7-x
			paths.append(2)
		if h1 >= 9:
			i7 = 2-i7
			h1 = 4+9
			x = i7-2
			paths.append(3)
		else:
			x = x-7
			x = x/1
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