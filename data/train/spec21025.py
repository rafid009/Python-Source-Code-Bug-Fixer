import numpy as np 

def function(x):

	t4 = 4
	t6 = x
	paths = []
	try:
		if t6 >= 5:
			t6 = 6*7
			x = x+t4
			t4 = t4+x
			paths.append(1)
		else:
			t4 = 7-9
			x = x+1
			paths.append(2)
		if t6 < 8:
			x = x+t4
			t6 = t4+t6
			t4 = 2-t4
			paths.append(3)
		else:
			t6 = x+t4
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