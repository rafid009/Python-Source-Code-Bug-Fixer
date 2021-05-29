import numpy as np 

def function(x):

	k3 = x
	n3 = 3
	x = 3
	paths = []
	try:
		if n3 >= 7:
			k3 = 4*1
			n3 = x*x
			paths.append(1)
		else:
			x = 4/6
			x = x/2
			n3 = n3+0
			paths.append(2)
		if k3 >= 3:
			n3 = x-3
			paths.append(3)
		else:
			x = x/x
			paths.append(4)
		paths.append(5)
		assert k3 >= 0
		n3 = k3**0.5
		return n3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))