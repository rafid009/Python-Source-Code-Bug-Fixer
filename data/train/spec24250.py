import numpy as np 

def function(x):

	k3 = x
	g8 = x
	paths = []
	try:
		if k3 <= 7:
			g8 = 6/g8
			x = g8-1
			paths.append(1)
		else:
			k3 = k3/2
			paths.append(2)
		if g8 < 8:
			k3 = k3+k3
			paths.append(3)
		else:
			g8 = x/g8
			paths.append(4)
		paths.append(5)
		assert g8 >= 0
		k3 = g8**0.5
		return k3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))