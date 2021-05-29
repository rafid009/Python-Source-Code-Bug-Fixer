import numpy as np 

def function(x):

	t6 = 9
	o3 = x
	paths = []
	try:
		if t6 > 2:
			t6 = t6/4
			t6 = t6-t6
			o3 = 9/7
			paths.append(1)
		else:
			t6 = 0+t6
			t6 = 8-t6
			t6 = 9/t6
			paths.append(2)
		if x <= 1:
			x = 6+1
			paths.append(3)
		else:
			x = x-6
			o3 = 3*o3
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