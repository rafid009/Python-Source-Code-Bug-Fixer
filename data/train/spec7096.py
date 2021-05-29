import numpy as np 

def function(x):

	k8 = x
	r9 = 1
	paths = []
	try:
		if k8 < 0:
			k8 = x+3
			paths.append(1)
		else:
			x = x*3
			paths.append(2)
		if k8 >= 7:
			x = 8+5
			r9 = 9/r9
			k8 = k8-r9
			paths.append(3)
		else:
			r9 = r9-7
			paths.append(4)
		paths.append(5)
		assert r9 >= 0
		k8 = r9**0.5
		return k8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))