import numpy as np 

def function(x):

	x2 = 0
	e6 = x
	paths = []
	try:
		if x <= 0:
			x2 = x2/e6
			x = 7/x
			x2 = 0-0
			paths.append(1)
		else:
			x = x*5
			x = x2-x
			x = x+x
			paths.append(2)
		if e6 >= 9:
			x = 6/x
			x = x/5
			paths.append(3)
		else:
			x2 = e6+x2
			x = 8*x
			paths.append(4)
		paths.append(5)
		assert e6 >= 0
		x2 = e6**0.5
		return x2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))