import numpy as np 

def function(x):

	o1 = x
	n6 = 2
	paths = []
	try:
		if n6 >= 4:
			x = 8+x
			paths.append(1)
		else:
			o1 = o1+0
			paths.append(2)
		if x < 3:
			o1 = 5/o1
			n6 = n6+n6
			n6 = n6*x
			paths.append(3)
		else:
			o1 = o1+3
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