import numpy as np 

def function(x):

	b4 = x
	k3 = 9
	paths = []
	try:
		if k3 > 0:
			k3 = 4-k3
			paths.append(1)
		else:
			b4 = 4/b4
			paths.append(2)
		if x <= 9:
			b4 = 4*b4
			b4 = 2*6
			paths.append(3)
		else:
			x = 1*x
			paths.append(4)
		paths.append(5)
		assert k3 >= 0
		b4 = k3**0.5
		return b4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))