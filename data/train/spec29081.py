import numpy as np 

def function(x):

	y5 = x
	t2 = x
	paths = []
	try:
		if x > 9:
			t2 = 4/y5
			paths.append(1)
		else:
			y5 = y5/3
			t2 = 0/8
			t2 = t2-4
			paths.append(2)
		if y5 < 7:
			t2 = t2/2
			y5 = y5/9
			paths.append(3)
		else:
			y5 = t2-7
			paths.append(4)
		paths.append(5)
		assert y5 >= 0
		x = y5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))