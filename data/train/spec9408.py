import numpy as np 

def function(x):

	f5 = x
	q3 = 8
	paths = []
	try:
		if f5 >= 7:
			x = x/3
			paths.append(1)
		else:
			x = x+x
			paths.append(2)
		if f5 >= 7:
			x = x+7
			paths.append(3)
		else:
			q3 = 3*7
			f5 = 3*7
			f5 = 0+f5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q3 = x**0.5
		return q3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))