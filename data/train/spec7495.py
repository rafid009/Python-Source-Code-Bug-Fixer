import numpy as np 

def function(x):

	j5 = x
	e9 = 4
	paths = []
	try:
		if x >= 0:
			j5 = 5+4
			e9 = 1-7
			paths.append(1)
		else:
			j5 = 9/j5
			j5 = j5*7
			x = 6*1
			paths.append(2)
		if e9 >= 5:
			x = 8-2
			x = e9+j5
			j5 = 0/j5
			paths.append(3)
		else:
			x = x/7
			e9 = 7*e9
			paths.append(4)
		paths.append(5)
		assert j5 >= 0
		x = j5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))