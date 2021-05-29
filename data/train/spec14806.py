import numpy as np 

def function(x):

	m6 = x
	k8 = 7
	paths = []
	try:
		if m6 > 1:
			m6 = m6+5
			m6 = 1-4
			paths.append(1)
		else:
			k8 = x+k8
			k8 = k8*1
			m6 = k8-m6
			paths.append(2)
		if x < 2:
			x = 2+x
			m6 = 1/x
			paths.append(3)
		else:
			x = 6/x
			paths.append(4)
		paths.append(5)
		assert k8 >= 0
		m6 = k8**0.5
		return m6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))