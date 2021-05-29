import numpy as np 

def function(x):

	e4 = 4
	i6 = 7
	paths = []
	try:
		if x <= 4:
			x = x*5
			e4 = e4*5
			x = x-e4
			paths.append(1)
		else:
			x = x*i6
			i6 = i6-x
			paths.append(2)
		if e4 <= 0:
			i6 = i6-6
			paths.append(3)
		else:
			i6 = i6/5
			e4 = 1-e4
			paths.append(4)
		paths.append(5)
		assert e4 >= 0
		i6 = e4**0.5
		return i6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))