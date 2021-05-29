import numpy as np 

def function(x):

	n8 = x
	j1 = 6
	paths = []
	try:
		if x <= 3:
			j1 = 9-7
			x = x+2
			paths.append(1)
		else:
			x = 1*n8
			paths.append(2)
		if j1 >= 2:
			x = j1-n8
			n8 = 8*1
			paths.append(3)
		else:
			j1 = j1-j1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j1 = x**0.5
		return j1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))