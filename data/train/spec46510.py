import numpy as np 

def function(x):

	k3 = x
	b8 = 3
	paths = []
	try:
		if k3 > 4:
			k3 = 8+x
			paths.append(1)
		else:
			b8 = k3/b8
			b8 = b8/2
			paths.append(2)
		if x < 2:
			x = x/k3
			paths.append(3)
		else:
			k3 = x*b8
			x = 5*9
			k3 = 5/k3
			paths.append(4)
		paths.append(5)
		assert b8 >= 0
		k3 = b8**0.5
		return k3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))