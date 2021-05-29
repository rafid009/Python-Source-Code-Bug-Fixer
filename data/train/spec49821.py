import numpy as np 

def function(x):

	p2 = x
	k2 = 8
	paths = []
	try:
		if x <= 4:
			p2 = 5-p2
			paths.append(1)
		else:
			p2 = p2/8
			x = 4*x
			paths.append(2)
		if x < 6:
			k2 = 2*5
			p2 = 2*p2
			paths.append(3)
		else:
			x = x*0
			k2 = 3/p2
			p2 = k2-6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k2 = x**0.5
		return k2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))