import numpy as np 

def function(x):

	k8 = 8
	m1 = 7
	paths = []
	try:
		if m1 > 1:
			m1 = m1/8
			paths.append(1)
		else:
			m1 = 3+x
			k8 = k8/8
			paths.append(2)
		if m1 >= 2:
			k8 = m1/m1
			m1 = 8+m1
			paths.append(3)
		else:
			m1 = k8-0
			k8 = 1+1
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