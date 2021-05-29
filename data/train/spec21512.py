import numpy as np 

def function(x):

	g5 = 2
	y7 = 2
	x = x
	paths = []
	try:
		if g5 >= 2:
			y7 = y7/5
			paths.append(1)
		else:
			x = 0*7
			g5 = g5*g5
			y7 = y7/g5
			paths.append(2)
		if x < 4:
			y7 = 2+y7
			x = x-8
			paths.append(3)
		else:
			x = 9*0
			y7 = g5-y7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))