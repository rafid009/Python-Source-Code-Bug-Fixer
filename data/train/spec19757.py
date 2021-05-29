import numpy as np 

def function(x):

	j9 = 1
	n8 = x
	paths = []
	try:
		if x >= 5:
			j9 = n8-j9
			paths.append(1)
		else:
			j9 = j9*x
			n8 = 8/n8
			j9 = j9/j9
			paths.append(2)
		if n8 < 7:
			x = 5+x
			x = x-1
			paths.append(3)
		else:
			n8 = n8-8
			j9 = j9*n8
			paths.append(4)
		paths.append(5)
		assert j9 >= 0
		x = j9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))