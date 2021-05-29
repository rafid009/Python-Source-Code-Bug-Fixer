import numpy as np 

def function(x):

	i2 = x
	m0 = 8
	paths = []
	try:
		if m0 <= 5:
			x = i2*m0
			x = m0/5
			m0 = m0*2
			paths.append(1)
		else:
			x = x+4
			x = 3+i2
			m0 = m0*6
			paths.append(2)
		if i2 <= 8:
			x = 4*x
			m0 = i2-m0
			i2 = i2+3
			paths.append(3)
		else:
			i2 = i2-m0
			i2 = i2*9
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