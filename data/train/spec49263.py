import numpy as np 

def function(x):

	q6 = x
	f7 = 1
	paths = []
	try:
		if x > 0:
			x = x+x
			f7 = 0-6
			paths.append(1)
		else:
			q6 = q6*5
			x = 6*x
			q6 = q6+q6
			paths.append(2)
		if f7 > 6:
			x = x/2
			paths.append(3)
		else:
			x = x*x
			x = f7+3
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