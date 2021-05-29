import numpy as np 

def function(x):

	j1 = 0
	paths = []
	try:
		if j1 <= 9:
			j1 = j1+j1
			j1 = j1+0
			paths.append(1)
		else:
			x = 1/j1
			paths.append(2)
		if x > 0:
			x = 0/5
			x = x+1
			j1 = 7*j1
			paths.append(3)
		else:
			j1 = 7-x
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