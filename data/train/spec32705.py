import numpy as np 

def function(x):

	r6 = x
	y3 = 2
	paths = []
	try:
		if r6 < 9:
			x = x/2
			paths.append(1)
		else:
			r6 = 9-r6
			paths.append(2)
		if y3 <= 3:
			y3 = y3+r6
			r6 = 5+r6
			paths.append(3)
		else:
			y3 = y3-7
			y3 = r6/y3
			x = 8/7
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