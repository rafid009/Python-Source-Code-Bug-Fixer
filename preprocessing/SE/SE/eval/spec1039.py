import numpy as np 

def function(x):

	i5 = 7
	n8 = 7
	paths = []
	try:
		if i5 < 8:
			x = i5*5
			paths.append(1)
		else:
			x = x*n8
			i5 = 5-i5
			i5 = i5-6
			paths.append(2)
		if x < 3:
			i5 = i5*n8
			x = n8+n8
			i5 = 7+3
			paths.append(3)
		else:
			n8 = x/n8
			x = 2-x
			x = x-i5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n8 = x**0.5
		return n8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))