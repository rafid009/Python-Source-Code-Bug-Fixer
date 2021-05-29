import numpy as np 

def function(x):

	a1 = x
	x1 = 0
	paths = []
	try:
		if x1 >= 9:
			x = x+6
			a1 = 2/1
			x1 = x1*5
			paths.append(1)
		else:
			a1 = a1/8
			x = 0-5
			a1 = 8/x
			paths.append(2)
		if x <= 4:
			x1 = a1+x
			x = x+8
			paths.append(3)
		else:
			x = x/5
			x = x*6
			x1 = x1-1
			paths.append(4)
		paths.append(5)
		assert x1 >= 0
		a1 = x1**0.5
		return a1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))