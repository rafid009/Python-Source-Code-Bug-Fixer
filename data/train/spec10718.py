import numpy as np 

def function(x):

	t2 = x
	y2 = 0
	paths = []
	try:
		if x >= 8:
			y2 = 8-y2
			paths.append(1)
		else:
			t2 = t2+5
			y2 = y2+9
			t2 = t2+1
			paths.append(2)
		if x <= 9:
			t2 = 8/5
			y2 = 2+x
			paths.append(3)
		else:
			x = 2-8
			t2 = t2/6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y2 = x**0.5
		return y2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))