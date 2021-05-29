import numpy as np 

def function(x):

	k1 = x
	m3 = x
	x = 1
	paths = []
	try:
		if m3 >= 0:
			m3 = m3+7
			paths.append(1)
		else:
			m3 = m3/x
			paths.append(2)
		if x <= 8:
			x = k1+x
			k1 = k1-m3
			paths.append(3)
		else:
			x = x-2
			paths.append(4)
		paths.append(5)
		assert k1 >= 0
		m3 = k1**0.5
		return m3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))