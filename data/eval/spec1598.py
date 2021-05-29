import numpy as np 

def function(x):

	y6 = x
	l5 = 6
	paths = []
	try:
		if x >= 5:
			l5 = 2+l5
			y6 = 2+y6
			paths.append(1)
		else:
			l5 = 5+y6
			y6 = 3*9
			paths.append(2)
		if y6 <= 7:
			x = 0*x
			y6 = y6/1
			y6 = 5-2
			paths.append(3)
		else:
			y6 = 9-1
			y6 = 6*3
			y6 = y6*0
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