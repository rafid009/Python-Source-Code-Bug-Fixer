import numpy as np 

def function(x):

	m6 = x
	k8 = 9
	paths = []
	try:
		if x <= 8:
			m6 = m6-8
			m6 = 9/m6
			paths.append(1)
		else:
			x = 7/m6
			x = 9+6
			k8 = k8/2
			paths.append(2)
		if k8 > 6:
			x = x*5
			k8 = k8*9
			k8 = x-2
			paths.append(3)
		else:
			m6 = m6-1
			x = m6/x
			x = 1/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m6 = x**0.5
		return m6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))