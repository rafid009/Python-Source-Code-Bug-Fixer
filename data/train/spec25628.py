import numpy as np 

def function(x):

	i2 = x
	t1 = 9
	paths = []
	try:
		if x >= 5:
			t1 = 4+8
			i2 = 1+6
			paths.append(1)
		else:
			x = 6/x
			paths.append(2)
		if i2 < 0:
			t1 = t1-5
			i2 = i2-7
			i2 = 1-3
			paths.append(3)
		else:
			x = x-9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t1 = x**0.5
		return t1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))