import numpy as np 

def function(x):

	x1 = x
	p8 = x
	paths = []
	try:
		if p8 <= 7:
			x1 = 8*2
			x1 = x+0
			paths.append(1)
		else:
			x = 8*x
			paths.append(2)
		if x >= 3:
			x1 = x1+p8
			paths.append(3)
		else:
			x1 = x-x1
			x1 = x1/p8
			paths.append(4)
		paths.append(5)
		assert p8 >= 0
		x = p8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))