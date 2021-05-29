import numpy as np 

def function(x):

	y1 = 7
	t6 = 8
	paths = []
	try:
		if x < 1:
			y1 = y1/t6
			t6 = x/7
			x = 0-y1
			paths.append(1)
		else:
			y1 = y1-5
			paths.append(2)
		if x >= 3:
			y1 = 1*y1
			paths.append(3)
		else:
			t6 = 1/t6
			y1 = x*8
			x = x*2
			paths.append(4)
		paths.append(5)
		assert t6 >= 0
		y1 = t6**0.5
		return y1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))