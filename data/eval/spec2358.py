import numpy as np 

def function(x):

	n2 = 6
	j1 = x
	x = x
	paths = []
	try:
		if n2 <= 0:
			n2 = n2*3
			paths.append(1)
		else:
			n2 = n2-x
			paths.append(2)
		if j1 >= 3:
			j1 = 6/4
			x = x/8
			j1 = j1-6
			paths.append(3)
		else:
			n2 = 4/j1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n2 = x**0.5
		return n2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))