import numpy as np 

def function(x):

	f1 = 9
	i5 = 2
	paths = []
	try:
		if i5 >= 0:
			x = i5+5
			x = 5-f1
			paths.append(1)
		else:
			f1 = f1*6
			i5 = i5*i5
			paths.append(2)
		if i5 >= 5:
			i5 = i5*5
			paths.append(3)
		else:
			f1 = f1-8
			x = 9/x
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