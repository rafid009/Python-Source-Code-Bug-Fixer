import numpy as np 

def function(x):

	y4 = 6
	a5 = x
	paths = []
	try:
		if x <= 2:
			x = x*x
			paths.append(1)
		else:
			a5 = a5*a5
			paths.append(2)
		if x < 4:
			x = a5-x
			x = 4-8
			paths.append(3)
		else:
			y4 = 3-y4
			y4 = 7*2
			paths.append(4)
		paths.append(5)
		assert a5 >= 0
		y4 = a5**0.5
		return y4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))