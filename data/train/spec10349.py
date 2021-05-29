import numpy as np 

def function(x):

	t4 = x
	y6 = 1
	paths = []
	try:
		if y6 > 3:
			y6 = y6+3
			t4 = t4/y6
			paths.append(1)
		else:
			x = y6+x
			y6 = 6+y6
			paths.append(2)
		if y6 > 9:
			y6 = y6*5
			t4 = t4+t4
			x = 5/x
			paths.append(3)
		else:
			y6 = 3+9
			x = 8+x
			paths.append(4)
		paths.append(5)
		assert t4 >= 0
		x = t4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))