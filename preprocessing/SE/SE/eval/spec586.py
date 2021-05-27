import numpy as np 

def function(x):

	j1 = 4
	i8 = 6
	paths = []
	try:
		if x < 9:
			j1 = 1-j1
			i8 = i8-j1
			paths.append(1)
		else:
			x = 9-x
			i8 = j1/3
			x = 2*x
			paths.append(2)
		if i8 > 2:
			x = x*3
			paths.append(3)
		else:
			i8 = i8/7
			x = 6*7
			j1 = j1+4
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