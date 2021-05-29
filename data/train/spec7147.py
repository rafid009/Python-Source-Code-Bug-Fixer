import numpy as np 

def function(x):

	p7 = 9
	x8 = 7
	paths = []
	try:
		if x >= 5:
			x8 = x8*0
			x8 = 2-5
			x8 = x8+4
			paths.append(1)
		else:
			x8 = 1/6
			paths.append(2)
		if p7 >= 4:
			x8 = 4/x8
			paths.append(3)
		else:
			p7 = 5/x
			x8 = 2-x8
			x = 4-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))