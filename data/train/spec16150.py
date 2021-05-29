import numpy as np 

def function(x):

	k8 = x
	p1 = x
	paths = []
	try:
		if p1 > 7:
			p1 = 3/p1
			x = 8-3
			paths.append(1)
		else:
			x = 0*5
			k8 = 7+k8
			paths.append(2)
		if x <= 8:
			k8 = k8*9
			paths.append(3)
		else:
			k8 = k8-6
			k8 = p1-k8
			x = 2+x
			paths.append(4)
		paths.append(5)
		assert k8 >= 0
		k8 = k8**0.5
		return k8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))