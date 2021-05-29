import numpy as np 

def function(x):

	p3 = x
	k2 = x
	paths = []
	try:
		if k2 > 5:
			p3 = 4/p3
			k2 = k2-5
			paths.append(1)
		else:
			k2 = k2/5
			x = 8+x
			paths.append(2)
		if x < 4:
			k2 = 2-x
			p3 = p3+2
			paths.append(3)
		else:
			p3 = x/x
			x = 6+x
			paths.append(4)
		paths.append(5)
		assert k2 >= 0
		x = k2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))