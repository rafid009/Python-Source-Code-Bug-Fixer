import numpy as np 

def function(x):

	k6 = 7
	m7 = 5
	paths = []
	try:
		if x > 3:
			x = m7*x
			x = k6/x
			paths.append(1)
		else:
			m7 = 6/3
			paths.append(2)
		if k6 > 7:
			x = x-1
			k6 = 8/k6
			paths.append(3)
		else:
			k6 = k6-9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k6 = x**0.5
		return k6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))