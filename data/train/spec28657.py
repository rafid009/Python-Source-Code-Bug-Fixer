import numpy as np 

def function(x):

	i2 = 2
	h1 = x
	x = 7
	paths = []
	try:
		if i2 >= 6:
			x = h1*x
			i2 = i2+3
			x = x-h1
			paths.append(1)
		else:
			x = x+x
			paths.append(2)
		if i2 <= 1:
			h1 = 7/h1
			paths.append(3)
		else:
			i2 = i2+i2
			h1 = i2*h1
			paths.append(4)
		paths.append(5)
		assert h1 >= 0
		i2 = h1**0.5
		return i2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))