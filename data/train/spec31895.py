import numpy as np 

def function(x):

	j1 = x
	n6 = x
	paths = []
	try:
		if n6 > 8:
			n6 = 1/4
			paths.append(1)
		else:
			x = x+9
			j1 = j1/x
			paths.append(2)
		if x > 8:
			j1 = j1-3
			j1 = 1/3
			paths.append(3)
		else:
			j1 = j1-8
			x = 1/3
			n6 = n6+x
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