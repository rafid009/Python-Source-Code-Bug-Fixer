import numpy as np 

def function(x):

	k2 = 3
	p2 = x
	paths = []
	try:
		if p2 <= 0:
			p2 = p2*3
			paths.append(1)
		else:
			k2 = 3*k2
			x = x/x
			paths.append(2)
		if p2 > 9:
			k2 = k2*8
			k2 = 3+5
			paths.append(3)
		else:
			x = x/k2
			k2 = k2-4
			k2 = p2-5
			paths.append(4)
		paths.append(5)
		assert p2 >= 0
		k2 = p2**0.5
		return k2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))