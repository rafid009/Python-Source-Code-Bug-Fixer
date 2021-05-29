import numpy as np 

def function(x):

	x6 = 4
	e7 = x
	paths = []
	try:
		if x < 3:
			x6 = 1+x6
			e7 = 2*e7
			x = x*3
			paths.append(1)
		else:
			x6 = x6-0
			x = e7*x
			x = 7/x
			paths.append(2)
		if x < 3:
			x6 = x6*6
			paths.append(3)
		else:
			x = 6+x6
			x6 = x6*x6
			x = x6*2
			paths.append(4)
		paths.append(5)
		assert e7 >= 0
		x6 = e7**0.5
		return x6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))