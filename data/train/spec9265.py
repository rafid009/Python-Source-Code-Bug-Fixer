import numpy as np 

def function(x):

	b6 = 9
	j1 = x
	x = 1
	paths = []
	try:
		if j1 > 5:
			b6 = 8-j1
			b6 = b6/b6
			paths.append(1)
		else:
			x = x+0
			b6 = 2-j1
			j1 = b6*9
			paths.append(2)
		if j1 >= 2:
			x = 5+j1
			b6 = 1/b6
			j1 = 6-j1
			paths.append(3)
		else:
			x = x-j1
			paths.append(4)
		paths.append(5)
		assert j1 >= 0
		x = j1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))