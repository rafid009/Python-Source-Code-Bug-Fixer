import numpy as np 

def function(x):

	k9 = 3
	e9 = x
	paths = []
	try:
		if e9 > 1:
			e9 = e9/5
			k9 = 3/k9
			paths.append(1)
		else:
			k9 = 6-1
			k9 = 8-k9
			k9 = 8*8
			paths.append(2)
		if e9 >= 2:
			e9 = e9/9
			x = 3/e9
			paths.append(3)
		else:
			x = x*5
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