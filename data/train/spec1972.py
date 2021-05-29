import numpy as np 

def function(x):

	y6 = x
	t9 = 3
	paths = []
	try:
		if x < 8:
			x = y6*x
			paths.append(1)
		else:
			t9 = 3+y6
			t9 = t9/3
			y6 = 4/1
			paths.append(2)
		if y6 <= 0:
			t9 = t9*x
			t9 = 7-0
			t9 = x-3
			paths.append(3)
		else:
			t9 = t9/7
			paths.append(4)
		paths.append(5)
		assert t9 >= 0
		y6 = t9**0.5
		return y6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))