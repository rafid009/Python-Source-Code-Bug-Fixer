import numpy as np 

def function(x):

	e0 = 0
	a2 = x
	paths = []
	try:
		if e0 <= 8:
			e0 = 2-e0
			paths.append(1)
		else:
			x = x*0
			paths.append(2)
		if a2 >= 1:
			x = 7/x
			e0 = e0+7
			x = 9/e0
			paths.append(3)
		else:
			x = 5-x
			paths.append(4)
		paths.append(5)
		assert a2 >= 0
		x = a2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))