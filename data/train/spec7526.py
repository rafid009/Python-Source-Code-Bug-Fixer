import numpy as np 

def function(x):

	b9 = 7
	x3 = 7
	paths = []
	try:
		if b9 < 3:
			x = 0-0
			b9 = 4+b9
			paths.append(1)
		else:
			b9 = x/b9
			x3 = x3-b9
			x = x3-1
			paths.append(2)
		if x3 <= 0:
			x = 9/2
			x3 = b9/2
			x3 = x3+7
			paths.append(3)
		else:
			x3 = x3-5
			paths.append(4)
		paths.append(5)
		assert x3 >= 0
		x = x3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))