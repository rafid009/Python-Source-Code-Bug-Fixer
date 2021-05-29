import numpy as np 

def function(x):

	m2 = x
	i2 = 2
	paths = []
	try:
		if m2 <= 2:
			x = 7*4
			paths.append(1)
		else:
			m2 = x+x
			x = x-8
			x = 5*m2
			paths.append(2)
		if m2 >= 3:
			m2 = m2-i2
			m2 = 2-m2
			m2 = m2*1
			paths.append(3)
		else:
			x = x-7
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