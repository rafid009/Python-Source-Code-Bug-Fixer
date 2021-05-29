import numpy as np 

def function(x):

	f0 = 6
	k8 = x
	paths = []
	try:
		if f0 > 9:
			f0 = f0+k8
			f0 = 9+f0
			f0 = f0-0
			paths.append(1)
		else:
			f0 = f0-0
			paths.append(2)
		if x >= 0:
			k8 = 5*x
			f0 = 4/f0
			f0 = 5*x
			paths.append(3)
		else:
			k8 = k8-4
			paths.append(4)
		paths.append(5)
		assert k8 >= 0
		f0 = k8**0.5
		return f0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))