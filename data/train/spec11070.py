import numpy as np 

def function(x):

	i1 = 3
	x9 = 6
	paths = []
	try:
		if i1 <= 0:
			x = x-8
			x = 7+x
			x9 = i1-x9
			paths.append(1)
		else:
			x9 = x*x9
			x9 = x9-x
			x = 3*i1
			paths.append(2)
		if x > 0:
			i1 = i1/9
			paths.append(3)
		else:
			x = x/i1
			x = i1-x
			paths.append(4)
		paths.append(5)
		assert x9 >= 0
		x = x9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))