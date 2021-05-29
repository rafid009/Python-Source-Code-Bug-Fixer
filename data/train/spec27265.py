import numpy as np 

def function(x):

	k8 = 9
	m2 = x
	x = 0
	paths = []
	try:
		if k8 <= 4:
			m2 = k8*8
			paths.append(1)
		else:
			k8 = 8*1
			k8 = k8+k8
			paths.append(2)
		if k8 <= 4:
			m2 = 3-m2
			paths.append(3)
		else:
			x = x-2
			k8 = 7*k8
			m2 = m2*1
			paths.append(4)
		paths.append(5)
		assert m2 >= 0
		m2 = m2**0.5
		return m2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))