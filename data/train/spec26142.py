import numpy as np 

def function(x):

	r7 = 2
	k8 = 9
	paths = []
	try:
		if k8 <= 3:
			x = x-0
			paths.append(1)
		else:
			k8 = 1/1
			r7 = 3/x
			r7 = 5*x
			paths.append(2)
		if k8 <= 5:
			r7 = 4/r7
			paths.append(3)
		else:
			x = x*5
			k8 = 4+6
			paths.append(4)
		paths.append(5)
		assert r7 >= 0
		r7 = r7**0.5
		return r7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))