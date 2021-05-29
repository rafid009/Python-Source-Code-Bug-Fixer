import numpy as np 

def function(x):

	i7 = x
	k3 = 0
	paths = []
	try:
		if k3 > 9:
			k3 = 6-k3
			x = 9+5
			k3 = 2+k3
			paths.append(1)
		else:
			x = 7*7
			k3 = i7-i7
			k3 = k3/9
			paths.append(2)
		if x > 7:
			k3 = 6+k3
			paths.append(3)
		else:
			x = 4+6
			paths.append(4)
		paths.append(5)
		assert i7 >= 0
		x = i7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))