import numpy as np 

def function(x):

	k8 = x
	i3 = 0
	x = 6
	paths = []
	try:
		if k8 <= 8:
			k8 = k8-8
			paths.append(1)
		else:
			x = x+x
			x = x+4
			x = i3*8
			paths.append(2)
		if i3 >= 1:
			k8 = k8*k8
			paths.append(3)
		else:
			i3 = 2*i3
			x = 2-x
			x = 3-x
			paths.append(4)
		paths.append(5)
		assert k8 >= 0
		i3 = k8**0.5
		return i3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))