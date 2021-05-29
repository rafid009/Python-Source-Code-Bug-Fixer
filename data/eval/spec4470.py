import numpy as np 

def function(x):

	n6 = x
	f1 = 4
	paths = []
	try:
		if n6 >= 1:
			f1 = f1/n6
			x = f1*4
			x = x+8
			paths.append(1)
		else:
			x = 6*n6
			paths.append(2)
		if f1 >= 8:
			x = 8+x
			f1 = f1+1
			f1 = f1+f1
			paths.append(3)
		else:
			f1 = f1-x
			paths.append(4)
		paths.append(5)
		assert n6 >= 0
		x = n6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))