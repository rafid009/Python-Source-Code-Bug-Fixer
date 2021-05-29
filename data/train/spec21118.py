import numpy as np 

def function(x):

	i4 = x
	y3 = x
	paths = []
	try:
		if y3 >= 4:
			y3 = 1-y3
			paths.append(1)
		else:
			x = x/1
			paths.append(2)
		if y3 <= 3:
			y3 = 2*y3
			paths.append(3)
		else:
			x = x+8
			i4 = i4*8
			x = 9+x
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