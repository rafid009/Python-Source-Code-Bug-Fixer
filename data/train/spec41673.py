import numpy as np 

def function(x):

	v1 = x
	t8 = x
	paths = []
	try:
		if v1 < 3:
			x = x*t8
			x = 9+x
			x = 8-t8
			paths.append(1)
		else:
			x = 4/v1
			t8 = 0/t8
			paths.append(2)
		if x >= 8:
			t8 = 7-t8
			paths.append(3)
		else:
			t8 = v1-9
			t8 = t8/x
			paths.append(4)
		paths.append(5)
		assert t8 >= 0
		x = t8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))