import numpy as np 

def function(x):

	u2 = x
	y3 = 1
	paths = []
	try:
		if u2 >= 6:
			x = u2-9
			y3 = x*y3
			paths.append(1)
		else:
			y3 = 7+y3
			u2 = 3+2
			x = 9-x
			paths.append(2)
		if u2 < 7:
			y3 = 0+3
			x = 7+x
			u2 = 2/1
			paths.append(3)
		else:
			u2 = u2*2
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