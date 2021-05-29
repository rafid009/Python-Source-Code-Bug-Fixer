import numpy as np 

def function(x):

	k2 = x
	p3 = 1
	paths = []
	try:
		if x >= 3:
			x = k2+x
			x = x*p3
			paths.append(1)
		else:
			k2 = k2*9
			k2 = k2-4
			paths.append(2)
		if x < 7:
			x = x*x
			paths.append(3)
		else:
			x = 9+5
			p3 = 0*p3
			k2 = k2-x
			paths.append(4)
		paths.append(5)
		assert k2 >= 0
		p3 = k2**0.5
		return p3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))