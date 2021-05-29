import numpy as np 

def function(x):

	y4 = 9
	a2 = x
	paths = []
	try:
		if x > 2:
			x = 1*1
			paths.append(1)
		else:
			x = x+y4
			y4 = x/2
			y4 = a2+y4
			paths.append(2)
		if y4 < 6:
			y4 = y4/a2
			paths.append(3)
		else:
			a2 = 1+a2
			a2 = 1*y4
			a2 = x+9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a2 = x**0.5
		return a2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))