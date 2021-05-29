import numpy as np 

def function(x):

	h1 = x
	i2 = x
	paths = []
	try:
		if x <= 3:
			x = i2+x
			x = 5-5
			paths.append(1)
		else:
			x = 8*5
			i2 = i2/x
			x = 7+h1
			paths.append(2)
		if i2 >= 7:
			h1 = 7/h1
			i2 = 8/i2
			paths.append(3)
		else:
			h1 = h1/7
			x = h1-x
			paths.append(4)
		paths.append(5)
		assert i2 >= 0
		h1 = i2**0.5
		return h1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))