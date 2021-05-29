import numpy as np 

def function(x):

	t7 = 8
	t2 = 5
	x = x
	paths = []
	try:
		if t2 > 3:
			t2 = 5/t2
			t2 = 9*t2
			x = x*t2
			paths.append(1)
		else:
			x = 6*5
			x = t2-x
			t2 = t2/8
			paths.append(2)
		if x < 1:
			t2 = 8-t2
			paths.append(3)
		else:
			t7 = 6/x
			paths.append(4)
		paths.append(5)
		assert t2 >= 0
		x = t2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))