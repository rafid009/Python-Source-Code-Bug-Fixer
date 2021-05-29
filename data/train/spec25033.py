import numpy as np 

def function(x):

	x3 = x
	x6 = x
	x = x
	paths = []
	try:
		if x > 0:
			x3 = x6/x3
			x3 = x3-6
			paths.append(1)
		else:
			x = 0/5
			x = x6+x
			x3 = 1-x3
			paths.append(2)
		if x3 > 7:
			x6 = x6+2
			x6 = x6-5
			x = x+3
			paths.append(3)
		else:
			x = x*1
			x6 = x6*2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x6 = x**0.5
		return x6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))