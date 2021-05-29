import numpy as np 

def function(x):

	k7 = x
	p7 = 0
	paths = []
	try:
		if x < 8:
			x = x-3
			p7 = 9-1
			paths.append(1)
		else:
			x = 0-x
			p7 = x-p7
			x = 4*x
			paths.append(2)
		if k7 < 7:
			p7 = p7*p7
			paths.append(3)
		else:
			p7 = k7*p7
			x = 9-x
			paths.append(4)
		paths.append(5)
		assert p7 >= 0
		k7 = p7**0.5
		return k7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))