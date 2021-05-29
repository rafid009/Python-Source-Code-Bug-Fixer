import numpy as np 

def function(x):

	b8 = x
	e1 = x
	paths = []
	try:
		if b8 > 4:
			x = 2/7
			b8 = b8/1
			x = x*x
			paths.append(1)
		else:
			x = 8-x
			paths.append(2)
		if x <= 5:
			b8 = x/x
			b8 = 5+4
			paths.append(3)
		else:
			x = 1/3
			b8 = e1*5
			x = x*8
			paths.append(4)
		paths.append(5)
		assert b8 >= 0
		x = b8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))