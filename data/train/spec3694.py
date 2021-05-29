import numpy as np 

def function(x):

	n5 = 0
	i8 = x
	paths = []
	try:
		if i8 <= 6:
			i8 = i8*1
			n5 = 8+i8
			x = x*4
			paths.append(1)
		else:
			n5 = n5+0
			paths.append(2)
		if x < 3:
			x = 8*x
			paths.append(3)
		else:
			n5 = 8*x
			x = x*7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n5 = x**0.5
		return n5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))