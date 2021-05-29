import numpy as np 

def function(x):

	a1 = 9
	b7 = x
	paths = []
	try:
		if x < 6:
			b7 = 2+7
			b7 = b7+4
			x = 2-a1
			paths.append(1)
		else:
			a1 = 8*a1
			b7 = b7+7
			a1 = 5-a1
			paths.append(2)
		if a1 < 7:
			b7 = 3/5
			a1 = 2+a1
			paths.append(3)
		else:
			b7 = b7*1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b7 = x**0.5
		return b7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))