import numpy as np 

def function(x):

	r2 = 8
	y3 = x
	paths = []
	try:
		if y3 <= 6:
			r2 = 4/5
			y3 = 9*1
			paths.append(1)
		else:
			y3 = y3+7
			paths.append(2)
		if x > 3:
			x = 2*x
			r2 = 3-r2
			paths.append(3)
		else:
			y3 = 8-y3
			x = x+x
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