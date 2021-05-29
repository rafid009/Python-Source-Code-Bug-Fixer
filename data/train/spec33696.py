import numpy as np 

def function(x):

	k9 = x
	j1 = x
	paths = []
	try:
		if x >= 6:
			j1 = x+k9
			k9 = 0-7
			j1 = x/j1
			paths.append(1)
		else:
			k9 = k9-8
			k9 = k9/k9
			j1 = k9/1
			paths.append(2)
		if k9 > 7:
			x = x+3
			j1 = j1*x
			paths.append(3)
		else:
			k9 = k9+k9
			j1 = j1-7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k9 = x**0.5
		return k9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))