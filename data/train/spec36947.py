import numpy as np 

def function(x):

	y4 = 3
	t2 = x
	paths = []
	try:
		if y4 <= 5:
			y4 = 8*y4
			x = 8-x
			paths.append(1)
		else:
			x = x*y4
			x = 5/8
			paths.append(2)
		if t2 > 1:
			y4 = x*x
			x = 4-x
			x = x*8
			paths.append(3)
		else:
			x = x-y4
			paths.append(4)
		paths.append(5)
		assert t2 >= 0
		x = t2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))