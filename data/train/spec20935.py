import numpy as np 

def function(x):

	u0 = 2
	t8 = x
	paths = []
	try:
		if t8 >= 9:
			x = 1/x
			u0 = t8+4
			t8 = 9*t8
			paths.append(1)
		else:
			x = x+t8
			paths.append(2)
		if x > 9:
			t8 = t8/8
			u0 = u0/1
			t8 = 3+t8
			paths.append(3)
		else:
			u0 = x/u0
			x = x+6
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