import numpy as np 

def function(x):

	y3 = 8
	t4 = 2
	paths = []
	try:
		if y3 > 0:
			t4 = 6-t4
			paths.append(1)
		else:
			t4 = x/t4
			x = 7/x
			paths.append(2)
		if x > 3:
			t4 = t4-1
			y3 = x*y3
			paths.append(3)
		else:
			y3 = t4/y3
			y3 = 2*7
			y3 = y3-y3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t4 = x**0.5
		return t4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))