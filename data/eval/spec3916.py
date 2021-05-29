import numpy as np 

def function(x):

	b7 = 9
	a3 = 8
	paths = []
	try:
		if b7 > 6:
			x = x*1
			a3 = 8/5
			x = x/5
			paths.append(1)
		else:
			b7 = b7+0
			a3 = 8-5
			paths.append(2)
		if a3 >= 5:
			x = x-x
			a3 = a3*1
			paths.append(3)
		else:
			a3 = 1-a3
			b7 = x-9
			paths.append(4)
		paths.append(5)
		assert b7 >= 0
		a3 = b7**0.5
		return a3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))