import numpy as np 

def function(x):

	v4 = 6
	t7 = 9
	paths = []
	try:
		if v4 >= 8:
			x = 2+x
			paths.append(1)
		else:
			t7 = 1-t7
			x = x-5
			paths.append(2)
		if x <= 7:
			x = 3*6
			x = x*9
			t7 = 4/t7
			paths.append(3)
		else:
			x = 3+8
			paths.append(4)
		paths.append(5)
		assert t7 >= 0
		x = t7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))