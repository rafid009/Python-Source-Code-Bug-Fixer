import numpy as np 

def function(x):

	m2 = 6
	k8 = x
	paths = []
	try:
		if k8 <= 0:
			m2 = m2+m2
			k8 = m2+6
			paths.append(1)
		else:
			k8 = 6-k8
			k8 = 2*k8
			x = 6/k8
			paths.append(2)
		if x > 8:
			m2 = m2*5
			x = x+6
			paths.append(3)
		else:
			x = 1+1
			paths.append(4)
		paths.append(5)
		assert k8 >= 0
		m2 = k8**0.5
		return m2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))