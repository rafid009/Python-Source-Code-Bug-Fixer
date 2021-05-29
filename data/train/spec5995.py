import numpy as np 

def function(x):

	k8 = 3
	r3 = 4
	x = 3
	paths = []
	try:
		if r3 > 4:
			k8 = k8-r3
			paths.append(1)
		else:
			r3 = x-r3
			k8 = 6+r3
			k8 = 8*2
			paths.append(2)
		if x > 5:
			r3 = 8/r3
			paths.append(3)
		else:
			x = x*x
			k8 = k8+k8
			x = 2-x
			paths.append(4)
		paths.append(5)
		assert r3 >= 0
		k8 = r3**0.5
		return k8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))