import numpy as np 

def function(x):

	j1 = x
	x1 = 4
	paths = []
	try:
		if j1 <= 8:
			j1 = 1+j1
			paths.append(1)
		else:
			j1 = j1/2
			j1 = 9-j1
			j1 = 9-x1
			paths.append(2)
		if j1 > 7:
			j1 = j1-6
			j1 = x1*4
			paths.append(3)
		else:
			x = 3+x
			x1 = j1-3
			j1 = x1+j1
			paths.append(4)
		paths.append(5)
		assert x1 >= 0
		x1 = x1**0.5
		return x1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))