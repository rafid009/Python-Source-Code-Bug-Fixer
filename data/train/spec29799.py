import numpy as np 

def function(x):

	k5 = x
	j9 = 3
	paths = []
	try:
		if k5 >= 5:
			j9 = j9*x
			j9 = j9/j9
			x = x/2
			paths.append(1)
		else:
			k5 = k5+x
			k5 = 4-k5
			paths.append(2)
		if j9 > 3:
			j9 = j9-j9
			k5 = k5+3
			paths.append(3)
		else:
			k5 = k5*2
			x = x+5
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