import numpy as np 

def function(x):

	k8 = 9
	j2 = x
	paths = []
	try:
		if j2 > 0:
			k8 = j2/x
			j2 = 3+4
			paths.append(1)
		else:
			x = x-5
			x = x-x
			j2 = j2-2
			paths.append(2)
		if j2 < 0:
			x = x-k8
			x = 5/x
			j2 = 1+j2
			paths.append(3)
		else:
			k8 = 4+k8
			x = x/8
			paths.append(4)
		paths.append(5)
		assert j2 >= 0
		x = j2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))