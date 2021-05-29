import numpy as np 

def function(x):

	y3 = 2
	f4 = 1
	paths = []
	try:
		if f4 < 4:
			y3 = x*5
			paths.append(1)
		else:
			y3 = 6/3
			x = 6*x
			y3 = 5*y3
			paths.append(2)
		if y3 > 8:
			f4 = f4+1
			x = 9+7
			f4 = f4+6
			paths.append(3)
		else:
			f4 = x/f4
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