import numpy as np 

def function(x):

	y8 = x
	b6 = 0
	x = x
	paths = []
	try:
		if b6 >= 4:
			y8 = 2/y8
			x = 4+7
			paths.append(1)
		else:
			x = x*9
			b6 = 4+4
			b6 = 7+2
			paths.append(2)
		if x <= 4:
			y8 = y8+x
			paths.append(3)
		else:
			x = x*3
			y8 = 9-y8
			y8 = y8-4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b6 = x**0.5
		return b6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))