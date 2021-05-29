import numpy as np 

def function(x):

	x2 = x
	e7 = x
	x = 7
	paths = []
	try:
		if x2 > 3:
			e7 = e7/3
			e7 = 5+e7
			paths.append(1)
		else:
			x2 = x2/x
			e7 = e7/7
			x = x+1
			paths.append(2)
		if x2 >= 0:
			x = x+x
			e7 = 8/1
			x2 = x2-0
			paths.append(3)
		else:
			x = 9/x
			x = 9/9
			paths.append(4)
		paths.append(5)
		assert e7 >= 0
		x2 = e7**0.5
		return x2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))