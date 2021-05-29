import numpy as np 

def function(x):

	i2 = x
	m8 = x
	paths = []
	try:
		if x <= 6:
			i2 = i2-i2
			x = i2/4
			paths.append(1)
		else:
			m8 = m8+8
			i2 = 1-2
			m8 = i2*3
			paths.append(2)
		if x >= 9:
			x = x/2
			i2 = i2-7
			paths.append(3)
		else:
			x = x*7
			i2 = i2*8
			paths.append(4)
		paths.append(5)
		assert i2 >= 0
		m8 = i2**0.5
		return m8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))