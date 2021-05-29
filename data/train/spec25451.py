import numpy as np 

def function(x):

	m7 = 6
	i2 = 7
	paths = []
	try:
		if m7 >= 6:
			i2 = 5/i2
			paths.append(1)
		else:
			i2 = m7+4
			x = m7*2
			m7 = 7/m7
			paths.append(2)
		if x < 3:
			i2 = i2-1
			i2 = 8*9
			m7 = 6-m7
			paths.append(3)
		else:
			i2 = 7+8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))