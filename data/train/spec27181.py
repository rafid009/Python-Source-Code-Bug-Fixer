import numpy as np 

def function(x):

	k6 = 5
	m8 = 3
	paths = []
	try:
		if x > 9:
			k6 = 7+m8
			k6 = x-x
			paths.append(1)
		else:
			x = x-7
			paths.append(2)
		if x <= 4:
			m8 = k6-7
			paths.append(3)
		else:
			m8 = 1/m8
			paths.append(4)
		paths.append(5)
		assert m8 >= 0
		m8 = m8**0.5
		return m8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))