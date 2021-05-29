import numpy as np 

def function(x):

	k8 = x
	i0 = 5
	paths = []
	try:
		if i0 < 0:
			k8 = 9/i0
			k8 = k8*8
			paths.append(1)
		else:
			x = k8+5
			i0 = i0/4
			x = x+1
			paths.append(2)
		if k8 <= 9:
			i0 = i0+7
			k8 = 2*k8
			paths.append(3)
		else:
			i0 = k8+i0
			paths.append(4)
		paths.append(5)
		assert k8 >= 0
		x = k8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))