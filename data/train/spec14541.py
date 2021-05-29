import numpy as np 

def function(x):

	m8 = x
	k8 = 8
	paths = []
	try:
		if m8 < 4:
			k8 = k8-1
			k8 = m8+2
			paths.append(1)
		else:
			m8 = x/m8
			x = x-3
			m8 = 8-m8
			paths.append(2)
		if x <= 5:
			x = 1*5
			k8 = k8*2
			k8 = k8-6
			paths.append(3)
		else:
			x = 6+k8
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