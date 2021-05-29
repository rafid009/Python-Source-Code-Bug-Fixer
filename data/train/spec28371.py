import numpy as np 

def function(x):

	k8 = x
	m3 = x
	paths = []
	try:
		if x > 7:
			k8 = k8+4
			m3 = m3+0
			paths.append(1)
		else:
			k8 = k8-1
			paths.append(2)
		if m3 <= 0:
			x = 3+x
			paths.append(3)
		else:
			m3 = 2*1
			k8 = 7/x
			k8 = m3*k8
			paths.append(4)
		paths.append(5)
		assert k8 >= 0
		x = k8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))