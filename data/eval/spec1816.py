import numpy as np 

def function(x):

	i2 = x
	m2 = 3
	paths = []
	try:
		if x >= 5:
			x = x/m2
			paths.append(1)
		else:
			m2 = m2/m2
			paths.append(2)
		if m2 >= 4:
			i2 = i2-4
			m2 = m2/5
			paths.append(3)
		else:
			x = i2/x
			i2 = 2-i2
			paths.append(4)
		paths.append(5)
		assert i2 >= 0
		i2 = i2**0.5
		return i2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))