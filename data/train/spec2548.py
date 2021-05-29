import numpy as np 

def function(x):

	a1 = x
	j7 = 8
	paths = []
	try:
		if a1 >= 1:
			a1 = a1*2
			x = 3+2
			paths.append(1)
		else:
			x = j7*x
			paths.append(2)
		if j7 >= 2:
			j7 = j7/6
			paths.append(3)
		else:
			j7 = 3-j7
			a1 = a1*1
			x = j7-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))