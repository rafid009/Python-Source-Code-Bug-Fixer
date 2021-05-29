import numpy as np 

def function(x):

	y6 = 2
	l6 = 4
	paths = []
	try:
		if l6 > 4:
			y6 = l6*1
			l6 = l6-1
			paths.append(1)
		else:
			l6 = x/l6
			paths.append(2)
		if x >= 7:
			l6 = 3+l6
			paths.append(3)
		else:
			y6 = y6-6
			l6 = l6*8
			paths.append(4)
		paths.append(5)
		assert y6 >= 0
		x = y6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))