import numpy as np 

def function(x):

	k6 = x
	m6 = x
	x = 3
	paths = []
	try:
		if m6 >= 2:
			m6 = m6/9
			paths.append(1)
		else:
			x = x+2
			paths.append(2)
		if k6 <= 7:
			x = m6*x
			m6 = 5/m6
			paths.append(3)
		else:
			k6 = k6-9
			x = x+6
			x = 4/x
			paths.append(4)
		paths.append(5)
		assert k6 >= 0
		k6 = k6**0.5
		return k6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))