import numpy as np 

def function(x):

	e5 = x
	k4 = 3
	paths = []
	try:
		if e5 <= 2:
			k4 = 0/9
			k4 = k4/e5
			paths.append(1)
		else:
			k4 = x+e5
			k4 = k4*6
			e5 = e5-0
			paths.append(2)
		if x <= 7:
			k4 = x*8
			e5 = k4*9
			paths.append(3)
		else:
			k4 = k4*3
			k4 = k4/k4
			k4 = 8/1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k4 = x**0.5
		return k4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))