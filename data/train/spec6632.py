import numpy as np 

def function(x):

	k3 = 0
	v9 = 1
	paths = []
	try:
		if x < 3:
			k3 = 4-k3
			k3 = 1+0
			v9 = 6/x
			paths.append(1)
		else:
			x = x-k3
			paths.append(2)
		if x > 7:
			v9 = x+v9
			x = 5*4
			paths.append(3)
		else:
			x = x-x
			v9 = v9+v9
			paths.append(4)
		paths.append(5)
		assert v9 >= 0
		k3 = v9**0.5
		return k3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))