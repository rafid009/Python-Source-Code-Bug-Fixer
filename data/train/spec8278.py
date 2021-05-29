import numpy as np 

def function(x):

	b9 = 1
	v5 = x
	paths = []
	try:
		if x > 0:
			v5 = b9*v5
			v5 = 0+6
			paths.append(1)
		else:
			b9 = 4*3
			paths.append(2)
		if b9 >= 5:
			v5 = 8-v5
			v5 = 5/v5
			v5 = 8-5
			paths.append(3)
		else:
			v5 = 8*1
			v5 = x-v5
			x = 1*9
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