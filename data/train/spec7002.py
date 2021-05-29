import numpy as np 

def function(x):

	e1 = 9
	i4 = 0
	paths = []
	try:
		if i4 > 3:
			e1 = x*e1
			e1 = i4-1
			paths.append(1)
		else:
			e1 = e1+e1
			i4 = i4+9
			paths.append(2)
		if x >= 7:
			x = x+5
			paths.append(3)
		else:
			x = x/9
			i4 = 8-e1
			e1 = e1+0
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