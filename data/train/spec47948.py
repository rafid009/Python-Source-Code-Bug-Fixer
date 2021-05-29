import numpy as np 

def function(x):

	e6 = x
	b8 = 7
	paths = []
	try:
		if e6 > 0:
			e6 = 6-e6
			b8 = b8-b8
			b8 = b8*7
			paths.append(1)
		else:
			e6 = 3-e6
			paths.append(2)
		if x <= 4:
			b8 = 2-x
			x = 5+e6
			e6 = e6*b8
			paths.append(3)
		else:
			x = x/7
			e6 = e6+4
			e6 = 0/e6
			paths.append(4)
		paths.append(5)
		assert e6 >= 0
		e6 = e6**0.5
		return e6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))