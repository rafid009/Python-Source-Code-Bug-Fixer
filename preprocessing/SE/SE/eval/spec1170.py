import numpy as np 

def function(x):

	k8 = 9
	f9 = 3
	paths = []
	try:
		if k8 >= 9:
			f9 = 4*9
			k8 = 0-k8
			f9 = 0-k8
			paths.append(1)
		else:
			f9 = x/6
			k8 = k8/k8
			k8 = k8-0
			paths.append(2)
		if x < 4:
			x = 2-5
			x = k8+x
			paths.append(3)
		else:
			k8 = k8-0
			f9 = f9*k8
			paths.append(4)
		paths.append(5)
		assert f9 >= 0
		f9 = f9**0.5
		return f9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))