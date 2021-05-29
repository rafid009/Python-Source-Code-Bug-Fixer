import numpy as np 

def function(x):

	k8 = x
	j2 = 5
	paths = []
	try:
		if j2 > 5:
			j2 = k8-7
			k8 = 0*x
			paths.append(1)
		else:
			x = x+5
			paths.append(2)
		if j2 > 9:
			k8 = j2-k8
			paths.append(3)
		else:
			j2 = j2-0
			x = 2+3
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