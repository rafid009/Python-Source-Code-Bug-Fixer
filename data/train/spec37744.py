import numpy as np 

def function(x):

	p4 = x
	k3 = 4
	x = 2
	paths = []
	try:
		if x > 3:
			k3 = k3-2
			paths.append(1)
		else:
			k3 = k3/p4
			x = x-3
			paths.append(2)
		if p4 > 1:
			p4 = 0+6
			paths.append(3)
		else:
			k3 = x-k3
			x = x/p4
			x = x+7
			paths.append(4)
		paths.append(5)
		assert p4 >= 0
		p4 = p4**0.5
		return p4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))