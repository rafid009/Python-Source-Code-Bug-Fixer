import numpy as np 

def function(x):

	v1 = x
	k3 = x
	paths = []
	try:
		if x < 3:
			v1 = 1*v1
			paths.append(1)
		else:
			x = x+x
			x = 3/k3
			x = x/4
			paths.append(2)
		if k3 >= 0:
			x = 4+x
			v1 = 8+v1
			k3 = 8-7
			paths.append(3)
		else:
			k3 = x*3
			paths.append(4)
		paths.append(5)
		assert v1 >= 0
		k3 = v1**0.5
		return k3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))