import numpy as np 

def function(x):

	l5 = 3
	k8 = x
	paths = []
	try:
		if x <= 4:
			x = 8/7
			paths.append(1)
		else:
			x = x*5
			k8 = k8-2
			paths.append(2)
		if l5 >= 9:
			l5 = x/8
			paths.append(3)
		else:
			x = l5/x
			paths.append(4)
		paths.append(5)
		assert k8 >= 0
		l5 = k8**0.5
		return l5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))