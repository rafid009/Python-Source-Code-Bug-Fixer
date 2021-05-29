import numpy as np 

def function(x):

	j0 = x
	k9 = x
	paths = []
	try:
		if j0 > 4:
			x = x+2
			j0 = j0-1
			j0 = j0/9
			paths.append(1)
		else:
			k9 = k9*j0
			k9 = j0-k9
			paths.append(2)
		if x <= 8:
			k9 = k9-3
			paths.append(3)
		else:
			j0 = j0/j0
			j0 = x/j0
			x = 1*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j0 = x**0.5
		return j0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))