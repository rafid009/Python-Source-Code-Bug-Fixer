import numpy as np 

def function(x):

	b9 = 9
	e1 = x
	paths = []
	try:
		if e1 <= 7:
			e1 = 8-x
			b9 = 7+b9
			e1 = 2*e1
			paths.append(1)
		else:
			e1 = e1+3
			b9 = b9-9
			paths.append(2)
		if e1 > 6:
			e1 = b9/x
			x = x*7
			paths.append(3)
		else:
			x = x+7
			b9 = b9-9
			b9 = 0/b9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b9 = x**0.5
		return b9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))