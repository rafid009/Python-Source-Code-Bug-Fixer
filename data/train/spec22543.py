import numpy as np 

def function(x):

	a0 = 4
	x7 = x
	paths = []
	try:
		if x >= 7:
			x = 5*0
			x7 = x7+1
			x = x7+x
			paths.append(1)
		else:
			x7 = x7+x
			paths.append(2)
		if x > 2:
			x = 4/6
			x7 = x7-9
			paths.append(3)
		else:
			x = x7+x
			x = 8-2
			paths.append(4)
		paths.append(5)
		assert x7 >= 0
		a0 = x7**0.5
		return a0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))