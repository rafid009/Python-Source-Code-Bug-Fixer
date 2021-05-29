import numpy as np 

def function(x):

	s7 = x
	k8 = 1
	paths = []
	try:
		if k8 > 1:
			k8 = x*0
			paths.append(1)
		else:
			x = x+4
			k8 = k8/s7
			k8 = 4-9
			paths.append(2)
		if s7 < 8:
			k8 = x*1
			paths.append(3)
		else:
			s7 = k8/s7
			paths.append(4)
		paths.append(5)
		assert s7 >= 0
		x = s7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))