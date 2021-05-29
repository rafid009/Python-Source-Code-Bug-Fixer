import numpy as np 

def function(x):

	j1 = x
	b4 = 8
	paths = []
	try:
		if x < 5:
			x = 9/6
			b4 = 3+j1
			paths.append(1)
		else:
			x = 3/x
			paths.append(2)
		if b4 < 1:
			x = 2/9
			paths.append(3)
		else:
			x = x+j1
			j1 = b4-2
			paths.append(4)
		paths.append(5)
		assert b4 >= 0
		x = b4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))