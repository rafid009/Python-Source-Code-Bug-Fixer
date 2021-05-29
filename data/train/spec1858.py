import numpy as np 

def function(x):

	v7 = 9
	l1 = 9
	paths = []
	try:
		if v7 <= 8:
			v7 = v7-0
			v7 = 8+v7
			paths.append(1)
		else:
			v7 = v7+v7
			v7 = 5+7
			paths.append(2)
		if l1 <= 7:
			l1 = v7/l1
			paths.append(3)
		else:
			x = x+7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v7 = x**0.5
		return v7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))