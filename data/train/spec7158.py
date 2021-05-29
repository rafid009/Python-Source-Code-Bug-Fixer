import numpy as np 

def function(x):

	k6 = x
	m3 = 8
	paths = []
	try:
		if m3 >= 7:
			m3 = 0/x
			m3 = k6+7
			x = x-4
			paths.append(1)
		else:
			x = 3/x
			paths.append(2)
		if k6 >= 3:
			k6 = k6-k6
			k6 = k6+8
			m3 = m3/2
			paths.append(3)
		else:
			m3 = k6/5
			k6 = 0-8
			k6 = 2-k6
			paths.append(4)
		paths.append(5)
		assert m3 >= 0
		k6 = m3**0.5
		return k6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))