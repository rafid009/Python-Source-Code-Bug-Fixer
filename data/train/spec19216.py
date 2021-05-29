import numpy as np 

def function(x):

	r9 = x
	t4 = x
	paths = []
	try:
		if x >= 8:
			x = t4-r9
			x = x-r9
			t4 = x/4
			paths.append(1)
		else:
			x = r9/r9
			t4 = t4/t4
			t4 = t4+4
			paths.append(2)
		if r9 < 3:
			r9 = 5*r9
			r9 = 8+6
			paths.append(3)
		else:
			r9 = r9/x
			paths.append(4)
		paths.append(5)
		assert t4 >= 0
		x = t4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))