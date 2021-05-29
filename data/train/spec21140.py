import numpy as np 

def function(x):

	n3 = 1
	x6 = 3
	paths = []
	try:
		if n3 <= 2:
			x6 = 3+x6
			x6 = x+x6
			x6 = x6+x
			paths.append(1)
		else:
			x = 2+7
			x = n3-x
			paths.append(2)
		if x < 1:
			x6 = x6+1
			x = x-n3
			paths.append(3)
		else:
			x = x/x
			n3 = n3+1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x6 = x**0.5
		return x6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))