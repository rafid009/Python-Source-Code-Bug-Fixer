import numpy as np 

def function(x):

	f7 = x
	k8 = 5
	paths = []
	try:
		if k8 <= 3:
			x = 6-x
			paths.append(1)
		else:
			f7 = f7+9
			paths.append(2)
		if k8 > 4:
			k8 = x-0
			x = f7/x
			paths.append(3)
		else:
			k8 = k8*8
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