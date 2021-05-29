import numpy as np 

def function(x):

	k8 = x
	r2 = 7
	paths = []
	try:
		if x < 5:
			r2 = k8-r2
			paths.append(1)
		else:
			x = x/6
			x = x+r2
			x = x/1
			paths.append(2)
		if r2 < 5:
			r2 = r2-9
			k8 = 7/x
			paths.append(3)
		else:
			k8 = 6/9
			x = x+5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))