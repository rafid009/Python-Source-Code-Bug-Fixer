import numpy as np 

def function(x):

	v9 = 7
	t4 = x
	paths = []
	try:
		if t4 <= 0:
			x = x-5
			v9 = v9+v9
			t4 = t4-x
			paths.append(1)
		else:
			v9 = 3+9
			x = t4/x
			x = x*4
			paths.append(2)
		if t4 >= 6:
			x = 8*v9
			paths.append(3)
		else:
			t4 = t4*x
			t4 = t4-4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v9 = x**0.5
		return v9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))