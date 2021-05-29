import numpy as np 

def function(x):

	b8 = x
	a5 = x
	paths = []
	try:
		if x >= 6:
			b8 = x-b8
			x = x/5
			paths.append(1)
		else:
			b8 = 9/4
			x = 8*b8
			paths.append(2)
		if x <= 9:
			b8 = 3/9
			x = x-9
			paths.append(3)
		else:
			x = 8*6
			x = 6-b8
			paths.append(4)
		paths.append(5)
		assert a5 >= 0
		a5 = a5**0.5
		return a5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))