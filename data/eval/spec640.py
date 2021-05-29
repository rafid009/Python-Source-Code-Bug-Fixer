import numpy as np 

def function(x):

	e5 = 2
	b8 = x
	paths = []
	try:
		if e5 > 7:
			e5 = e5/e5
			b8 = e5+b8
			paths.append(1)
		else:
			b8 = b8/8
			e5 = x-e5
			b8 = 9+x
			paths.append(2)
		if b8 < 0:
			x = e5*x
			paths.append(3)
		else:
			x = x+5
			x = x-4
			b8 = e5+4
			paths.append(4)
		paths.append(5)
		assert e5 >= 0
		e5 = e5**0.5
		return e5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))