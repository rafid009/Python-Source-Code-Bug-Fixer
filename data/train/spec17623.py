import numpy as np 

def function(x):

	f7 = x
	n9 = 1
	paths = []
	try:
		if x >= 0:
			x = x-8
			f7 = f7+8
			n9 = n9*f7
			paths.append(1)
		else:
			n9 = n9*3
			paths.append(2)
		if f7 < 5:
			x = 4/6
			f7 = f7+9
			n9 = f7*n9
			paths.append(3)
		else:
			n9 = 0*5
			n9 = 7+7
			n9 = x-1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f7 = x**0.5
		return f7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))