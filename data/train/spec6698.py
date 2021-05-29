import numpy as np 

def function(x):

	b4 = x
	e2 = x
	paths = []
	try:
		if e2 <= 9:
			x = b4-x
			e2 = 2*6
			e2 = e2*2
			paths.append(1)
		else:
			b4 = 1/1
			x = 3+x
			e2 = 3*8
			paths.append(2)
		if b4 > 7:
			e2 = e2*9
			paths.append(3)
		else:
			b4 = 1/b4
			paths.append(4)
		paths.append(5)
		assert b4 >= 0
		x = b4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))