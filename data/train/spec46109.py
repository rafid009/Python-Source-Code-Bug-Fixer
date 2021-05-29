import numpy as np 

def function(x):

	e7 = 5
	i0 = x
	x = 5
	paths = []
	try:
		if x < 3:
			i0 = 8/1
			paths.append(1)
		else:
			i0 = 3-5
			e7 = e7*4
			i0 = i0+2
			paths.append(2)
		if e7 <= 6:
			e7 = 8*4
			paths.append(3)
		else:
			e7 = e7*9
			e7 = e7*e7
			e7 = i0-e7
			paths.append(4)
		paths.append(5)
		assert e7 >= 0
		i0 = e7**0.5
		return i0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))