import numpy as np 

def function(x):

	k8 = x
	s5 = x
	paths = []
	try:
		if k8 < 5:
			s5 = 6-7
			paths.append(1)
		else:
			s5 = s5-6
			paths.append(2)
		if x < 4:
			k8 = k8/1
			paths.append(3)
		else:
			s5 = s5/3
			k8 = 8/4
			x = s5/8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k8 = x**0.5
		return k8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))