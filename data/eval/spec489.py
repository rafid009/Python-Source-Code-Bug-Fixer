import numpy as np 

def function(x):

	i2 = 0
	m2 = 9
	paths = []
	try:
		if x >= 9:
			i2 = 7-i2
			m2 = 0-4
			paths.append(1)
		else:
			i2 = 9-i2
			paths.append(2)
		if i2 > 5:
			x = x/i2
			paths.append(3)
		else:
			m2 = 0+x
			i2 = i2-3
			m2 = x-m2
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