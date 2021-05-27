import numpy as np 

def function(x):

	i9 = x
	h0 = 9
	paths = []
	try:
		if h0 > 6:
			x = 5+7
			i9 = 1+i9
			x = x*i9
			paths.append(1)
		else:
			x = x-8
			x = h0/i9
			paths.append(2)
		if x < 8:
			x = x+h0
			i9 = i9+6
			h0 = h0*0
			paths.append(3)
		else:
			i9 = 3-4
			i9 = x+i9
			x = 6/h0
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