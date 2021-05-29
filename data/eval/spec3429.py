import numpy as np 

def function(x):

	b6 = 8
	e4 = 8
	paths = []
	try:
		if e4 > 4:
			b6 = 2+b6
			b6 = 6*x
			paths.append(1)
		else:
			x = 0+x
			paths.append(2)
		if x < 2:
			e4 = e4+1
			b6 = b6+e4
			e4 = 2-e4
			paths.append(3)
		else:
			e4 = 0-e4
			paths.append(4)
		paths.append(5)
		assert b6 >= 0
		x = b6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))