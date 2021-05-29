import numpy as np 

def function(x):

	n8 = x
	r8 = 4
	paths = []
	try:
		if r8 > 6:
			n8 = 1-3
			r8 = 2*r8
			n8 = n8-4
			paths.append(1)
		else:
			n8 = n8-8
			paths.append(2)
		if x <= 8:
			r8 = r8/r8
			r8 = 5+r8
			paths.append(3)
		else:
			x = x-8
			x = 2/n8
			n8 = n8/1
			paths.append(4)
		paths.append(5)
		assert n8 >= 0
		x = n8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))