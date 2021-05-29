import numpy as np 

def function(x):

	k3 = x
	p6 = x
	paths = []
	try:
		if k3 <= 4:
			p6 = k3*x
			k3 = k3+8
			paths.append(1)
		else:
			p6 = p6-7
			p6 = 6-1
			k3 = k3*9
			paths.append(2)
		if k3 > 6:
			k3 = x-4
			x = 9-x
			k3 = 0/2
			paths.append(3)
		else:
			p6 = 6+p6
			paths.append(4)
		paths.append(5)
		assert k3 >= 0
		k3 = k3**0.5
		return k3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))