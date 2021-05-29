import numpy as np 

def function(x):

	t1 = 9
	y7 = x
	paths = []
	try:
		if t1 < 4:
			x = 0*3
			y7 = y7-5
			x = x*y7
			paths.append(1)
		else:
			y7 = y7-x
			y7 = y7-9
			x = x*5
			paths.append(2)
		if t1 > 3:
			y7 = x*8
			paths.append(3)
		else:
			x = x+8
			x = 0*2
			paths.append(4)
		paths.append(5)
		assert y7 >= 0
		x = y7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))