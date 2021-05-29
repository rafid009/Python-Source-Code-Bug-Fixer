import numpy as np 

def function(x):

	o5 = 2
	k8 = x
	paths = []
	try:
		if k8 < 1:
			o5 = o5-8
			x = 2-x
			x = x/o5
			paths.append(1)
		else:
			k8 = k8-o5
			x = k8-1
			x = k8-x
			paths.append(2)
		if o5 < 2:
			x = x/5
			o5 = 4-o5
			o5 = o5+4
			paths.append(3)
		else:
			o5 = 8*6
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