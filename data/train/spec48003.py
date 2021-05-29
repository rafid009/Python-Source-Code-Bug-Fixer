import numpy as np 

def function(x):

	e7 = x
	i7 = 4
	paths = []
	try:
		if x >= 3:
			e7 = 3+9
			i7 = 4/i7
			paths.append(1)
		else:
			x = x/5
			i7 = i7*8
			paths.append(2)
		if x < 8:
			i7 = i7+6
			x = x/9
			paths.append(3)
		else:
			e7 = 5-e7
			e7 = 5+3
			i7 = i7-9
			paths.append(4)
		paths.append(5)
		assert e7 >= 0
		x = e7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))