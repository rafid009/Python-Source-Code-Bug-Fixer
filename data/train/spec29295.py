import numpy as np 

def function(x):

	v1 = 3
	k3 = x
	paths = []
	try:
		if k3 >= 7:
			k3 = k3+7
			paths.append(1)
		else:
			k3 = k3+6
			k3 = k3-3
			v1 = v1+2
			paths.append(2)
		if v1 > 2:
			k3 = k3+k3
			k3 = 9-k3
			v1 = 1/k3
			paths.append(3)
		else:
			v1 = k3-v1
			x = x*0
			paths.append(4)
		paths.append(5)
		assert v1 >= 0
		x = v1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))