import numpy as np 

def function(x):

	t9 = x
	x4 = x
	paths = []
	try:
		if x <= 9:
			t9 = t9/7
			x = t9/t9
			x4 = 9*6
			paths.append(1)
		else:
			t9 = x/2
			x4 = 9*5
			x4 = 7-x4
			paths.append(2)
		if x4 > 1:
			t9 = 4/t9
			paths.append(3)
		else:
			x4 = 3*x4
			paths.append(4)
		paths.append(5)
		assert t9 >= 0
		x4 = t9**0.5
		return x4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))