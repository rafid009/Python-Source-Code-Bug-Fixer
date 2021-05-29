import numpy as np 

def function(x):

	k8 = 9
	u8 = 7
	paths = []
	try:
		if k8 <= 8:
			u8 = k8*u8
			x = x/2
			paths.append(1)
		else:
			x = x+k8
			k8 = 2/k8
			x = x+5
			paths.append(2)
		if k8 > 5:
			k8 = k8*7
			x = k8*7
			paths.append(3)
		else:
			k8 = k8/9
			k8 = k8*k8
			k8 = x/u8
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