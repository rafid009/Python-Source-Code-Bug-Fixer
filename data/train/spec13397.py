import numpy as np 

def function(x):

	v1 = x
	b9 = 6
	paths = []
	try:
		if v1 <= 5:
			x = 7/x
			b9 = b9*7
			v1 = v1-b9
			paths.append(1)
		else:
			b9 = 4+b9
			paths.append(2)
		if v1 < 5:
			v1 = 0-x
			paths.append(3)
		else:
			b9 = 7/b9
			v1 = v1-1
			paths.append(4)
		paths.append(5)
		assert v1 >= 0
		x = v1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))