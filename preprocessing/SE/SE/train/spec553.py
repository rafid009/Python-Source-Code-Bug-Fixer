import numpy as np 

def function(x):

	k3 = x
	b3 = x
	x = 1
	paths = []
	try:
		if k3 > 6:
			k3 = x/2
			k3 = 0+k3
			b3 = 7-b3
			paths.append(1)
		else:
			x = x/k3
			paths.append(2)
		if b3 <= 8:
			x = k3*b3
			x = x/x
			b3 = 6/b3
			paths.append(3)
		else:
			x = 0-6
			b3 = 9*6
			b3 = 5+b3
			paths.append(4)
		paths.append(5)
		assert b3 >= 0
		x = b3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))