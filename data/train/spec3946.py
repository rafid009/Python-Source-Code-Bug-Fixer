import numpy as np 

def function(x):

	k6 = 5
	e8 = 1
	x = x
	paths = []
	try:
		if k6 > 2:
			k6 = 2+5
			paths.append(1)
		else:
			e8 = x/e8
			e8 = 7-e8
			paths.append(2)
		if e8 >= 2:
			x = x/4
			e8 = e8-7
			paths.append(3)
		else:
			e8 = 0-k6
			paths.append(4)
		paths.append(5)
		assert e8 >= 0
		e8 = e8**0.5
		return e8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))