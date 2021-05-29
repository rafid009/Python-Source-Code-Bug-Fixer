import numpy as np 

def function(x):

	a4 = x
	y1 = 0
	paths = []
	try:
		if x <= 3:
			x = x*7
			paths.append(1)
		else:
			x = x*0
			paths.append(2)
		if x < 6:
			a4 = a4/5
			paths.append(3)
		else:
			a4 = 6*x
			x = x*y1
			x = x-7
			paths.append(4)
		paths.append(5)
		assert a4 >= 0
		y1 = a4**0.5
		return y1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))