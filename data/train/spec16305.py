import numpy as np 

def function(x):

	t3 = x
	y5 = 3
	paths = []
	try:
		if x < 6:
			y5 = 4-7
			paths.append(1)
		else:
			t3 = 0+t3
			t3 = t3/8
			y5 = 5+y5
			paths.append(2)
		if y5 >= 5:
			x = 9+4
			t3 = 5/t3
			paths.append(3)
		else:
			x = x+8
			y5 = 7-y5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y5 = x**0.5
		return y5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))