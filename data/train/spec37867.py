import numpy as np 

def function(x):

	k8 = 4
	g9 = x
	paths = []
	try:
		if k8 <= 1:
			g9 = g9*8
			paths.append(1)
		else:
			k8 = 9/k8
			paths.append(2)
		if k8 > 9:
			g9 = g9/2
			paths.append(3)
		else:
			k8 = k8+k8
			k8 = g9-0
			paths.append(4)
		paths.append(5)
		assert g9 >= 0
		k8 = g9**0.5
		return k8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))