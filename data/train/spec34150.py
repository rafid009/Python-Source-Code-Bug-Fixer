import numpy as np 

def function(x):

	e1 = x
	t7 = x
	paths = []
	try:
		if e1 < 6:
			x = t7/x
			x = 4+x
			paths.append(1)
		else:
			x = 2+x
			paths.append(2)
		if t7 < 8:
			e1 = e1-e1
			e1 = e1/1
			paths.append(3)
		else:
			x = 3+3
			e1 = e1*1
			e1 = 2/7
			paths.append(4)
		paths.append(5)
		assert t7 >= 0
		x = t7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))