import numpy as np 

def function(x):

	f3 = x
	t4 = 4
	paths = []
	try:
		if x > 8:
			t4 = t4*f3
			f3 = 1-f3
			paths.append(1)
		else:
			x = x+9
			paths.append(2)
		if x >= 0:
			t4 = x-t4
			paths.append(3)
		else:
			f3 = 3*f3
			paths.append(4)
		paths.append(5)
		assert t4 >= 0
		t4 = t4**0.5
		return t4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))