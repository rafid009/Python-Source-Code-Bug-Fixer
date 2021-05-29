import numpy as np 

def function(x):

	m9 = 5
	i2 = x
	paths = []
	try:
		if m9 <= 6:
			i2 = i2-1
			paths.append(1)
		else:
			m9 = m9-4
			x = x-2
			paths.append(2)
		if m9 > 4:
			m9 = 6*i2
			paths.append(3)
		else:
			i2 = 5*4
			m9 = m9-5
			paths.append(4)
		paths.append(5)
		assert i2 >= 0
		x = i2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))