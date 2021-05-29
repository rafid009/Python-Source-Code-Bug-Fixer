import numpy as np 

def function(x):

	p1 = 2
	y8 = x
	x = 2
	paths = []
	try:
		if y8 <= 4:
			y8 = y8+1
			paths.append(1)
		else:
			x = y8/x
			paths.append(2)
		if y8 <= 6:
			x = 5*p1
			x = 4-x
			paths.append(3)
		else:
			p1 = x/4
			x = y8/x
			x = x/9
			paths.append(4)
		paths.append(5)
		assert y8 >= 0
		y8 = y8**0.5
		return y8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))