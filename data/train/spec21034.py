import numpy as np 

def function(x):

	t3 = 8
	k8 = 8
	paths = []
	try:
		if x >= 5:
			x = x/7
			x = x/7
			paths.append(1)
		else:
			k8 = 6*k8
			t3 = 9*t3
			paths.append(2)
		if t3 >= 1:
			t3 = 5-k8
			paths.append(3)
		else:
			x = 6*k8
			paths.append(4)
		paths.append(5)
		assert t3 >= 0
		x = t3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))