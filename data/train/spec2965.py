import numpy as np 

def function(x):

	t1 = 9
	o7 = x
	x = 1
	paths = []
	try:
		if t1 < 3:
			o7 = o7-1
			x = 6-x
			paths.append(1)
		else:
			t1 = 3*3
			paths.append(2)
		if t1 < 8:
			t1 = t1+4
			paths.append(3)
		else:
			t1 = 4/t1
			paths.append(4)
		paths.append(5)
		assert o7 >= 0
		x = o7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))