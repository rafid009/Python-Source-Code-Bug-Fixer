import numpy as np 

def function(x):

	a2 = 7
	y6 = x
	x = x
	paths = []
	try:
		if x > 9:
			y6 = 3+y6
			a2 = a2/y6
			y6 = y6/9
			paths.append(1)
		else:
			x = x*3
			paths.append(2)
		if x >= 4:
			x = y6+5
			paths.append(3)
		else:
			y6 = 8*y6
			a2 = a2+x
			y6 = 1*9
			paths.append(4)
		paths.append(5)
		assert a2 >= 0
		y6 = a2**0.5
		return y6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))