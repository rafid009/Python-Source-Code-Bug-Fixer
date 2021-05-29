import numpy as np 

def function(x):

	k2 = x
	p4 = x
	paths = []
	try:
		if k2 > 6:
			k2 = 4*7
			paths.append(1)
		else:
			k2 = 9*3
			paths.append(2)
		if x > 3:
			x = p4*x
			k2 = x*0
			paths.append(3)
		else:
			x = 2-2
			x = k2*5
			paths.append(4)
		paths.append(5)
		assert p4 >= 0
		x = p4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))