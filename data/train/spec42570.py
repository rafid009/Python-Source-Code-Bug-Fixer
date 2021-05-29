import numpy as np 

def function(x):

	y2 = x
	t7 = 3
	paths = []
	try:
		if x > 7:
			t7 = t7+8
			t7 = 7+y2
			x = t7-x
			paths.append(1)
		else:
			y2 = y2+0
			paths.append(2)
		if y2 >= 7:
			t7 = x/t7
			x = t7/6
			x = x*y2
			paths.append(3)
		else:
			t7 = x+t7
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