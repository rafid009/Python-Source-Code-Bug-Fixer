import numpy as np 

def function(x):

	e4 = 4
	b4 = 1
	paths = []
	try:
		if x <= 3:
			b4 = 5-e4
			b4 = 6*b4
			paths.append(1)
		else:
			x = x*2
			paths.append(2)
		if x > 9:
			x = b4-1
			b4 = b4-x
			x = x/5
			paths.append(3)
		else:
			b4 = b4-6
			e4 = 5/e4
			paths.append(4)
		paths.append(5)
		assert b4 >= 0
		b4 = b4**0.5
		return b4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))