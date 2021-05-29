import numpy as np 

def function(x):

	j1 = 2
	e9 = x
	paths = []
	try:
		if e9 < 6:
			x = x+8
			e9 = e9*j1
			paths.append(1)
		else:
			j1 = x-6
			e9 = 0*j1
			paths.append(2)
		if x < 1:
			j1 = 5/j1
			e9 = e9/e9
			paths.append(3)
		else:
			x = 5-x
			j1 = 7*5
			paths.append(4)
		paths.append(5)
		assert e9 >= 0
		j1 = e9**0.5
		return j1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))