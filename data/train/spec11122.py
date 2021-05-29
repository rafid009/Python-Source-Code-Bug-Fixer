import numpy as np 

def function(x):

	t6 = x
	y3 = 5
	paths = []
	try:
		if t6 >= 7:
			t6 = t6/3
			y3 = y3+y3
			paths.append(1)
		else:
			t6 = 4+7
			paths.append(2)
		if y3 > 4:
			x = x+7
			paths.append(3)
		else:
			t6 = t6-t6
			t6 = t6/7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y3 = x**0.5
		return y3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))