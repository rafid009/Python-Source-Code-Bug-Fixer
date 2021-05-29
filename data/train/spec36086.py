import numpy as np 

def function(x):

	y6 = x
	b3 = x
	paths = []
	try:
		if x < 2:
			b3 = 5*3
			paths.append(1)
		else:
			y6 = y6-3
			y6 = y6*x
			paths.append(2)
		if x <= 9:
			y6 = y6*0
			y6 = y6*3
			paths.append(3)
		else:
			b3 = 4-y6
			x = 8/x
			paths.append(4)
		paths.append(5)
		assert b3 >= 0
		b3 = b3**0.5
		return b3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))