import numpy as np 

def function(x):

	h1 = 3
	v0 = 4
	paths = []
	try:
		if x < 6:
			h1 = h1-v0
			x = 2+h1
			paths.append(1)
		else:
			v0 = v0-v0
			x = x+x
			v0 = h1+h1
			paths.append(2)
		if x > 4:
			h1 = 5+h1
			paths.append(3)
		else:
			v0 = 1-v0
			x = 1*6
			h1 = h1*8
			paths.append(4)
		paths.append(5)
		assert h1 >= 0
		x = h1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))