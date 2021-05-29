import numpy as np 

def function(x):

	x0 = x
	t4 = x
	paths = []
	try:
		if x >= 9:
			x = x/2
			t4 = t4-t4
			paths.append(1)
		else:
			t4 = t4*x0
			x = 8*t4
			x = x*3
			paths.append(2)
		if x0 < 5:
			t4 = 8/2
			x0 = 4-4
			x = x-5
			paths.append(3)
		else:
			t4 = 8-t4
			x0 = x0/t4
			paths.append(4)
		paths.append(5)
		assert t4 >= 0
		x0 = t4**0.5
		return x0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))