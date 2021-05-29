import numpy as np 

def function(x):

	b9 = x
	e7 = 4
	paths = []
	try:
		if b9 > 1:
			e7 = 4+e7
			e7 = e7/b9
			paths.append(1)
		else:
			x = x*1
			b9 = e7-b9
			b9 = e7+x
			paths.append(2)
		if e7 > 6:
			b9 = 6+b9
			b9 = 9+7
			paths.append(3)
		else:
			b9 = e7-b9
			b9 = 9-3
			b9 = x+2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e7 = x**0.5
		return e7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))