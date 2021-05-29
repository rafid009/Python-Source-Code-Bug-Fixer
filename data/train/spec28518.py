import numpy as np 

def function(x):

	i3 = 2
	k8 = 1
	paths = []
	try:
		if x < 0:
			x = x/k8
			x = i3*5
			i3 = i3*i3
			paths.append(1)
		else:
			k8 = x/9
			paths.append(2)
		if x <= 6:
			x = 1/x
			x = 5/x
			paths.append(3)
		else:
			x = i3-x
			i3 = x*1
			k8 = 8*k8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k8 = x**0.5
		return k8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))