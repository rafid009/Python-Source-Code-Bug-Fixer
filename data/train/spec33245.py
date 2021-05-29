import numpy as np 

def function(x):

	f7 = 0
	n1 = 6
	paths = []
	try:
		if x <= 1:
			f7 = 9/7
			n1 = 1+4
			paths.append(1)
		else:
			n1 = x-6
			paths.append(2)
		if n1 >= 9:
			f7 = 0-f7
			paths.append(3)
		else:
			f7 = f7+5
			n1 = 0-n1
			paths.append(4)
		paths.append(5)
		assert n1 >= 0
		x = n1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))