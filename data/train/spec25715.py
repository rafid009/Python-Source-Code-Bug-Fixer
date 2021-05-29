import numpy as np 

def function(x):

	r6 = 3
	k8 = x
	paths = []
	try:
		if x > 4:
			k8 = k8*0
			x = x+7
			k8 = r6*9
			paths.append(1)
		else:
			k8 = 4-k8
			paths.append(2)
		if r6 > 5:
			k8 = k8/4
			k8 = 2/9
			paths.append(3)
		else:
			r6 = 8-1
			x = x+5
			k8 = k8*4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r6 = x**0.5
		return r6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))