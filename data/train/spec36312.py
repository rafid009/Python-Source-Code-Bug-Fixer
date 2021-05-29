import numpy as np 

def function(x):

	m6 = 5
	k9 = 3
	paths = []
	try:
		if x < 7:
			k9 = k9-7
			x = 3*7
			paths.append(1)
		else:
			k9 = x-1
			paths.append(2)
		if k9 > 4:
			m6 = m6/6
			x = 3*x
			m6 = m6/k9
			paths.append(3)
		else:
			x = m6-x
			m6 = 8*k9
			x = x/8
			paths.append(4)
		paths.append(5)
		assert m6 >= 0
		m6 = m6**0.5
		return m6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))