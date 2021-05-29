import numpy as np 

def function(x):

	b8 = x
	a7 = x
	paths = []
	try:
		if x < 3:
			x = x+3
			a7 = 8*b8
			a7 = a7*1
			paths.append(1)
		else:
			a7 = b8*x
			paths.append(2)
		if a7 >= 3:
			b8 = a7/7
			paths.append(3)
		else:
			b8 = b8-6
			b8 = x*b8
			x = a7*6
			paths.append(4)
		paths.append(5)
		assert a7 >= 0
		a7 = a7**0.5
		return a7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))