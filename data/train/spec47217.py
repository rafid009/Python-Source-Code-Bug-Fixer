import numpy as np 

def function(x):

	e1 = x
	u4 = x
	paths = []
	try:
		if x <= 4:
			u4 = u4/5
			paths.append(1)
		else:
			u4 = 1/u4
			paths.append(2)
		if e1 <= 4:
			x = 5+u4
			e1 = 7+e1
			paths.append(3)
		else:
			x = e1-e1
			x = 4-x
			x = 8-x
			paths.append(4)
		paths.append(5)
		assert e1 >= 0
		x = e1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))