import numpy as np 

def function(x):

	j2 = x
	k8 = x
	paths = []
	try:
		if x <= 1:
			j2 = j2*4
			j2 = 6-j2
			paths.append(1)
		else:
			j2 = j2-j2
			paths.append(2)
		if x <= 4:
			k8 = k8+7
			paths.append(3)
		else:
			k8 = k8/4
			k8 = k8/5
			k8 = k8+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j2 = x**0.5
		return j2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))