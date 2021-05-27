import numpy as np 

def function(x):

	m9 = 4
	k8 = x
	x = x
	paths = []
	try:
		if k8 > 1:
			x = 1+x
			x = k8/x
			m9 = 8-0
			paths.append(1)
		else:
			m9 = 5+m9
			paths.append(2)
		if x >= 6:
			k8 = 8+k8
			paths.append(3)
		else:
			m9 = m9+8
			x = x+x
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