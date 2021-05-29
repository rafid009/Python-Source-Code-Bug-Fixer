import numpy as np 

def function(x):

	p9 = x
	k3 = 2
	paths = []
	try:
		if x > 1:
			p9 = k3+x
			paths.append(1)
		else:
			p9 = p9+k3
			x = 1/x
			k3 = 2/9
			paths.append(2)
		if x <= 3:
			x = 4+x
			k3 = p9+k3
			paths.append(3)
		else:
			p9 = p9-k3
			k3 = 7+2
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