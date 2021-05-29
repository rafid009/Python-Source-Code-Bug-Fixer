import numpy as np 

def function(x):

	q7 = 3
	t4 = x
	paths = []
	try:
		if t4 > 9:
			x = 0+x
			paths.append(1)
		else:
			x = x*3
			t4 = 7+t4
			t4 = t4-4
			paths.append(2)
		if t4 < 8:
			q7 = q7-0
			q7 = 6*6
			paths.append(3)
		else:
			t4 = 8-1
			x = t4*6
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