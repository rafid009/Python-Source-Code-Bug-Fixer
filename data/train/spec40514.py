import numpy as np 

def function(x):

	t8 = 0
	v7 = x
	paths = []
	try:
		if t8 < 6:
			v7 = 7*9
			x = 5-x
			paths.append(1)
		else:
			v7 = 1+v7
			t8 = 4*v7
			paths.append(2)
		if x > 4:
			x = 8-5
			v7 = 4-0
			paths.append(3)
		else:
			t8 = t8*9
			v7 = v7/3
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