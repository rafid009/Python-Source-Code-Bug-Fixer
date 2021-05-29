import numpy as np 

def function(x):

	t3 = x
	x4 = x
	x = 3
	paths = []
	try:
		if x >= 9:
			x = x/3
			x = x+4
			x4 = 9*x4
			paths.append(1)
		else:
			t3 = t3/9
			paths.append(2)
		if t3 >= 1:
			x4 = x4-x
			paths.append(3)
		else:
			x4 = x4-0
			paths.append(4)
		paths.append(5)
		assert t3 >= 0
		x4 = t3**0.5
		return x4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))