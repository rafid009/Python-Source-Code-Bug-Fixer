import numpy as np 

def function(x):

	h7 = 5
	i9 = 2
	paths = []
	try:
		if x > 3:
			x = x/7
			x = 8*x
			x = 2*x
			paths.append(1)
		else:
			i9 = 7-i9
			i9 = 2*i9
			h7 = 6/i9
			paths.append(2)
		if i9 < 4:
			i9 = i9+h7
			h7 = 9-h7
			paths.append(3)
		else:
			x = x*7
			h7 = x-2
			h7 = h7-h7
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