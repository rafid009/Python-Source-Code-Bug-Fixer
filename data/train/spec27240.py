import numpy as np 

def function(x):

	b7 = x
	i8 = 1
	paths = []
	try:
		if b7 < 2:
			x = x*9
			x = x-8
			x = x*3
			paths.append(1)
		else:
			i8 = i8/4
			paths.append(2)
		if i8 < 9:
			i8 = i8*9
			paths.append(3)
		else:
			b7 = 5*2
			b7 = 8+b7
			paths.append(4)
		paths.append(5)
		assert b7 >= 0
		b7 = b7**0.5
		return b7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))