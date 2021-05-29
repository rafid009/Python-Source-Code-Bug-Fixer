import numpy as np 

def function(x):

	t8 = x
	v7 = x
	paths = []
	try:
		if v7 >= 1:
			v7 = v7-x
			x = 1-x
			paths.append(1)
		else:
			x = 8+3
			paths.append(2)
		if v7 >= 5:
			x = t8-3
			paths.append(3)
		else:
			v7 = v7-t8
			t8 = v7+0
			x = x+6
			paths.append(4)
		paths.append(5)
		assert v7 >= 0
		x = v7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))