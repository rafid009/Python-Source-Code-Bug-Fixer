import numpy as np 

def function(x):

	b8 = x
	k8 = x
	paths = []
	try:
		if k8 < 4:
			b8 = b8-b8
			paths.append(1)
		else:
			k8 = 1*2
			b8 = 1*b8
			paths.append(2)
		if k8 < 8:
			x = x-4
			k8 = 2+k8
			b8 = b8-2
			paths.append(3)
		else:
			k8 = 7*k8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b8 = x**0.5
		return b8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))