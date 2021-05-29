import numpy as np 

def function(x):

	y8 = 3
	t1 = 8
	paths = []
	try:
		if y8 >= 5:
			t1 = x/2
			t1 = 2+0
			paths.append(1)
		else:
			x = x-3
			y8 = 4+y8
			paths.append(2)
		if x > 2:
			x = t1/8
			t1 = x*t1
			x = 1*3
			paths.append(3)
		else:
			t1 = 1/x
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