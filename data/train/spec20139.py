import numpy as np 

def function(x):

	y8 = 8
	t7 = x
	paths = []
	try:
		if t7 <= 8:
			t7 = y8-2
			paths.append(1)
		else:
			y8 = 8*8
			paths.append(2)
		if y8 <= 7:
			x = 8+1
			paths.append(3)
		else:
			x = 0-7
			t7 = t7*1
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