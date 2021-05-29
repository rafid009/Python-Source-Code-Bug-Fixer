import numpy as np 

def function(x):

	e6 = x
	v7 = x
	x = 5
	paths = []
	try:
		if v7 <= 5:
			x = e6/x
			v7 = 0+v7
			x = 8+5
			paths.append(1)
		else:
			v7 = v7+e6
			e6 = 2+e6
			x = 5/v7
			paths.append(2)
		if e6 > 5:
			x = 1-7
			v7 = 9/v7
			paths.append(3)
		else:
			x = x/1
			paths.append(4)
		paths.append(5)
		assert v7 >= 0
		e6 = v7**0.5
		return e6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))