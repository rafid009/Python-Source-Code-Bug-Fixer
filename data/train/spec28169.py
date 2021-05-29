import numpy as np 

def function(x):

	x5 = 7
	k8 = x
	paths = []
	try:
		if x > 4:
			k8 = k8-4
			paths.append(1)
		else:
			x = 6-x
			k8 = k8+k8
			paths.append(2)
		if x <= 3:
			x5 = 3+x5
			x = x/x5
			x = x+5
			paths.append(3)
		else:
			x5 = 0/x5
			x5 = x5*x
			paths.append(4)
		paths.append(5)
		assert k8 >= 0
		k8 = k8**0.5
		return k8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))