import numpy as np 

def function(x):

	k3 = x
	f7 = 5
	paths = []
	try:
		if k3 < 2:
			k3 = k3+0
			paths.append(1)
		else:
			f7 = f7*5
			paths.append(2)
		if k3 <= 7:
			x = k3*x
			f7 = x*5
			paths.append(3)
		else:
			k3 = x+8
			k3 = 9/4
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