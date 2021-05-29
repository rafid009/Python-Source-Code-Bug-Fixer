import numpy as np 

def function(x):

	k8 = 6
	b5 = x
	paths = []
	try:
		if k8 < 2:
			k8 = k8/6
			paths.append(1)
		else:
			x = b5+5
			k8 = k8+x
			b5 = b5+x
			paths.append(2)
		if x <= 6:
			k8 = k8*2
			x = 5+x
			b5 = b5+5
			paths.append(3)
		else:
			b5 = 0*b5
			k8 = b5-4
			k8 = b5*x
			paths.append(4)
		paths.append(5)
		assert b5 >= 0
		k8 = b5**0.5
		return k8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))