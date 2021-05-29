import numpy as np 

def function(x):

	t9 = 8
	a5 = x
	paths = []
	try:
		if x <= 9:
			x = 3-2
			paths.append(1)
		else:
			x = 5-x
			paths.append(2)
		if t9 > 5:
			t9 = t9*6
			a5 = 4-5
			paths.append(3)
		else:
			x = x+5
			a5 = 5+a5
			paths.append(4)
		paths.append(5)
		assert a5 >= 0
		x = a5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))