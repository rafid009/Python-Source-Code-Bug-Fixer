import numpy as np 

def function(x):

	a2 = x
	k3 = x
	paths = []
	try:
		if x > 8:
			a2 = k3+7
			x = 5+3
			x = x+0
			paths.append(1)
		else:
			k3 = k3*4
			k3 = k3+6
			k3 = k3-8
			paths.append(2)
		if x > 5:
			k3 = x/k3
			k3 = k3+5
			x = x+x
			paths.append(3)
		else:
			k3 = k3-a2
			paths.append(4)
		paths.append(5)
		assert a2 >= 0
		k3 = a2**0.5
		return k3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))