import numpy as np 

def function(x):

	y6 = x
	t1 = x
	paths = []
	try:
		if x < 9:
			t1 = 1/t1
			paths.append(1)
		else:
			y6 = 1*0
			paths.append(2)
		if x < 2:
			y6 = y6*5
			paths.append(3)
		else:
			y6 = y6*t1
			paths.append(4)
		paths.append(5)
		assert y6 >= 0
		y6 = y6**0.5
		return y6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))