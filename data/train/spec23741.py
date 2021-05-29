import numpy as np 

def function(x):

	k8 = x
	p4 = 9
	paths = []
	try:
		if x > 5:
			k8 = x*9
			paths.append(1)
		else:
			x = p4/6
			k8 = 6-k8
			x = x-8
			paths.append(2)
		if k8 <= 9:
			p4 = k8+1
			x = x-3
			paths.append(3)
		else:
			x = x/9
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