import numpy as np 

def function(x):

	v5 = 2
	k8 = x
	x = 6
	paths = []
	try:
		if k8 >= 6:
			v5 = k8/k8
			x = x/2
			k8 = 8+k8
			paths.append(1)
		else:
			v5 = k8-v5
			paths.append(2)
		if v5 < 9:
			x = x-v5
			paths.append(3)
		else:
			v5 = v5-x
			k8 = 6-k8
			v5 = 7+0
			paths.append(4)
		paths.append(5)
		assert v5 >= 0
		x = v5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))