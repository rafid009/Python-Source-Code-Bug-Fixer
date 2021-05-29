import numpy as np 

def function(x):

	e1 = x
	k7 = x
	paths = []
	try:
		if x <= 3:
			x = x-9
			e1 = e1+e1
			paths.append(1)
		else:
			e1 = 5*e1
			paths.append(2)
		if e1 < 9:
			x = 5+2
			e1 = e1+k7
			paths.append(3)
		else:
			e1 = e1-e1
			k7 = 1*4
			paths.append(4)
		paths.append(5)
		assert k7 >= 0
		x = k7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))