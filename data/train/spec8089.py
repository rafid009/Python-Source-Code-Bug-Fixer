import numpy as np 

def function(x):

	e4 = 0
	y3 = 2
	paths = []
	try:
		if e4 >= 0:
			y3 = x+5
			e4 = y3*2
			paths.append(1)
		else:
			y3 = y3+3
			paths.append(2)
		if x < 0:
			x = e4*0
			paths.append(3)
		else:
			e4 = e4+7
			paths.append(4)
		paths.append(5)
		assert e4 >= 0
		x = e4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))