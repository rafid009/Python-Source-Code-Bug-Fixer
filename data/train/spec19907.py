import numpy as np 

def function(x):

	w9 = 9
	k8 = x
	x = 3
	paths = []
	try:
		if w9 < 3:
			w9 = 0-w9
			paths.append(1)
		else:
			x = x-w9
			paths.append(2)
		if x > 2:
			k8 = x*k8
			paths.append(3)
		else:
			k8 = k8*5
			x = x*0
			x = x+0
			paths.append(4)
		paths.append(5)
		assert k8 >= 0
		x = k8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))