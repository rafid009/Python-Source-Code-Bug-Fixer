import numpy as np 

def function(x):

	b5 = x
	e0 = 8
	paths = []
	try:
		if e0 >= 7:
			b5 = b5-b5
			paths.append(1)
		else:
			x = e0+x
			b5 = b5-7
			paths.append(2)
		if x < 9:
			x = 2/9
			e0 = x-e0
			e0 = 6/e0
			paths.append(3)
		else:
			x = x*x
			paths.append(4)
		paths.append(5)
		assert e0 >= 0
		e0 = e0**0.5
		return e0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))