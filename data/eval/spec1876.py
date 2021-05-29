import numpy as np 

def function(x):

	x6 = 9
	b7 = 3
	x = x
	paths = []
	try:
		if x6 > 8:
			x6 = 8/b7
			x = b7-x
			paths.append(1)
		else:
			x = b7-x
			b7 = 5*0
			x6 = x6-x
			paths.append(2)
		if x6 >= 8:
			x = 3-x
			x6 = 3+x6
			paths.append(3)
		else:
			b7 = b7-5
			x = 8+4
			x6 = 1+b7
			paths.append(4)
		paths.append(5)
		assert b7 >= 0
		x = b7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))