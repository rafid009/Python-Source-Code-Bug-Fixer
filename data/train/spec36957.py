import numpy as np 

def function(x):

	k3 = x
	q3 = x
	paths = []
	try:
		if k3 >= 2:
			k3 = x*1
			k3 = 0/k3
			paths.append(1)
		else:
			q3 = x/2
			q3 = 2-2
			x = k3-7
			paths.append(2)
		if x < 9:
			q3 = 4*q3
			x = x/7
			paths.append(3)
		else:
			k3 = k3*2
			x = k3/9
			paths.append(4)
		paths.append(5)
		assert k3 >= 0
		x = k3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))