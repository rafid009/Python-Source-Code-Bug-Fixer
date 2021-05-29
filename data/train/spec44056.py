import numpy as np 

def function(x):

	t2 = 3
	x1 = 9
	paths = []
	try:
		if x1 <= 5:
			t2 = 7*t2
			x1 = x1*1
			paths.append(1)
		else:
			t2 = t2/3
			x = x-8
			t2 = x1-1
			paths.append(2)
		if x1 > 5:
			x1 = t2*7
			x1 = x1+6
			paths.append(3)
		else:
			t2 = 7-t2
			x = x/8
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