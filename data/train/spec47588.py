import numpy as np 

def function(x):

	j1 = x
	b4 = x
	paths = []
	try:
		if j1 >= 7:
			b4 = 9*9
			paths.append(1)
		else:
			b4 = b4-b4
			x = x-b4
			paths.append(2)
		if j1 <= 9:
			j1 = 8/6
			x = 1-j1
			b4 = 3-b4
			paths.append(3)
		else:
			b4 = b4/x
			x = j1-x
			b4 = b4/2
			paths.append(4)
		paths.append(5)
		assert b4 >= 0
		b4 = b4**0.5
		return b4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))