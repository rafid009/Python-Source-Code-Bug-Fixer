import numpy as np 

def function(x):

	e1 = 5
	k2 = x
	paths = []
	try:
		if x >= 8:
			e1 = e1+1
			x = x+2
			paths.append(1)
		else:
			k2 = 5+k2
			e1 = x/x
			paths.append(2)
		if e1 > 0:
			e1 = k2-e1
			e1 = 4+k2
			paths.append(3)
		else:
			x = k2-k2
			k2 = k2*x
			paths.append(4)
		paths.append(5)
		assert k2 >= 0
		e1 = k2**0.5
		return e1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))