import numpy as np 

def function(x):

	x5 = 9
	x1 = 5
	paths = []
	try:
		if x < 1:
			x = 9/5
			x = 6+x
			paths.append(1)
		else:
			x1 = x1-x1
			paths.append(2)
		if x >= 5:
			x1 = x1*x
			x5 = 2-x
			paths.append(3)
		else:
			x1 = x1+4
			x = x*0
			paths.append(4)
		paths.append(5)
		assert x5 >= 0
		x1 = x5**0.5
		return x1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))