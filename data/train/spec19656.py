import numpy as np 

def function(x):

	y2 = x
	t7 = x
	paths = []
	try:
		if y2 <= 4:
			y2 = y2+t7
			paths.append(1)
		else:
			x = 3-7
			paths.append(2)
		if x >= 5:
			x = 0-y2
			t7 = x*x
			paths.append(3)
		else:
			t7 = t7+8
			paths.append(4)
		paths.append(5)
		assert t7 >= 0
		x = t7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))