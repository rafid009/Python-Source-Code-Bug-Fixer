import numpy as np 

def function(x):

	t4 = x
	k8 = 2
	paths = []
	try:
		if t4 < 4:
			k8 = 5/t4
			paths.append(1)
		else:
			k8 = k8-x
			x = x*2
			k8 = k8/5
			paths.append(2)
		if x > 3:
			k8 = x-k8
			paths.append(3)
		else:
			k8 = 0-k8
			x = 8*x
			k8 = k8-4
			paths.append(4)
		paths.append(5)
		assert t4 >= 0
		t4 = t4**0.5
		return t4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))