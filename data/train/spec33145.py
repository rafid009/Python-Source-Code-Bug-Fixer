import numpy as np 

def function(x):

	e6 = x
	b3 = x
	paths = []
	try:
		if b3 <= 6:
			b3 = 5/b3
			paths.append(1)
		else:
			x = 6/8
			x = 8/5
			e6 = 5-6
			paths.append(2)
		if e6 > 5:
			b3 = e6-3
			e6 = 4+8
			paths.append(3)
		else:
			b3 = 9+b3
			paths.append(4)
		paths.append(5)
		assert b3 >= 0
		e6 = b3**0.5
		return e6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))