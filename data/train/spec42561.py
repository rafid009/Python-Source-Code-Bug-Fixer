import numpy as np 

def function(x):

	y3 = x
	y4 = 4
	paths = []
	try:
		if y4 <= 5:
			x = x/y3
			x = x-1
			paths.append(1)
		else:
			x = x+x
			paths.append(2)
		if y3 > 7:
			y4 = 0*y4
			y3 = 4+y3
			paths.append(3)
		else:
			x = x*3
			paths.append(4)
		paths.append(5)
		assert y3 >= 0
		x = y3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))