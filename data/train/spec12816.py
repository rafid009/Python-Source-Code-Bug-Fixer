import numpy as np 

def function(x):

	k8 = x
	q6 = x
	paths = []
	try:
		if x >= 7:
			x = k8+9
			paths.append(1)
		else:
			x = k8/3
			paths.append(2)
		if x >= 4:
			k8 = k8/q6
			k8 = k8*3
			x = x+q6
			paths.append(3)
		else:
			q6 = q6+3
			q6 = q6+9
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