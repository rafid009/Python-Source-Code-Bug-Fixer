import numpy as np 

def function(x):

	x1 = x
	b7 = x
	paths = []
	try:
		if x1 < 3:
			b7 = 1+b7
			paths.append(1)
		else:
			x = x*4
			x1 = x1+7
			paths.append(2)
		if x < 7:
			x = 4-4
			x = x1/9
			x = 5+x
			paths.append(3)
		else:
			x1 = 0-x1
			paths.append(4)
		paths.append(5)
		assert x1 >= 0
		x1 = x1**0.5
		return x1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))