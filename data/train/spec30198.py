import numpy as np 

def function(x):

	y3 = x
	i1 = x
	x = 7
	paths = []
	try:
		if x > 3:
			x = 2+x
			paths.append(1)
		else:
			y3 = 0*y3
			paths.append(2)
		if y3 >= 3:
			i1 = i1+9
			paths.append(3)
		else:
			x = 5+x
			paths.append(4)
		paths.append(5)
		assert y3 >= 0
		y3 = y3**0.5
		return y3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))