import numpy as np 

def function(x):

	n5 = x
	o1 = 3
	paths = []
	try:
		if o1 <= 4:
			x = 5-6
			o1 = o1*2
			x = x/n5
			paths.append(1)
		else:
			n5 = 0-n5
			n5 = 6/5
			paths.append(2)
		if o1 > 9:
			o1 = 3*n5
			paths.append(3)
		else:
			x = x-x
			paths.append(4)
		paths.append(5)
		assert n5 >= 0
		x = n5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))