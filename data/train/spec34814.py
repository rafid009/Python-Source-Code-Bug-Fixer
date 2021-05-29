import numpy as np 

def function(x):

	t1 = 4
	y7 = 3
	paths = []
	try:
		if t1 <= 0:
			t1 = x+t1
			y7 = 6-0
			t1 = 7+8
			paths.append(1)
		else:
			y7 = x*y7
			paths.append(2)
		if t1 > 6:
			y7 = y7*9
			paths.append(3)
		else:
			y7 = y7+0
			y7 = 3/2
			t1 = t1-5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y7 = x**0.5
		return y7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))