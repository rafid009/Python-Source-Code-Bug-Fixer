import numpy as np 

def function(x):

	k7 = x
	a1 = x
	paths = []
	try:
		if a1 <= 9:
			x = 8+x
			paths.append(1)
		else:
			x = 6+5
			paths.append(2)
		if a1 > 9:
			k7 = k7/k7
			paths.append(3)
		else:
			x = 1+k7
			a1 = 3/a1
			paths.append(4)
		paths.append(5)
		assert k7 >= 0
		a1 = k7**0.5
		return a1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))