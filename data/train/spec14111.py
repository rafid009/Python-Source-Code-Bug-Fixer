import numpy as np 

def function(x):

	t2 = 0
	y1 = 6
	paths = []
	try:
		if y1 >= 7:
			t2 = 7*t2
			t2 = t2/2
			paths.append(1)
		else:
			y1 = x*y1
			t2 = y1+0
			paths.append(2)
		if y1 <= 6:
			x = x-y1
			paths.append(3)
		else:
			x = 3-t2
			y1 = x-8
			paths.append(4)
		paths.append(5)
		assert t2 >= 0
		y1 = t2**0.5
		return y1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))