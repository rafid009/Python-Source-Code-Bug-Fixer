import numpy as np 

def function(x):

	k9 = 7
	e3 = x
	paths = []
	try:
		if k9 > 3:
			x = x/x
			paths.append(1)
		else:
			k9 = 1/k9
			x = x+1
			paths.append(2)
		if k9 >= 1:
			x = e3+x
			k9 = k9*6
			e3 = 6+e3
			paths.append(3)
		else:
			e3 = 4+5
			k9 = 5+3
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