import numpy as np 

def function(x):

	m8 = 3
	o8 = x
	x = x
	paths = []
	try:
		if x > 8:
			o8 = o8*o8
			m8 = 4-m8
			m8 = m8*o8
			paths.append(1)
		else:
			m8 = m8+x
			o8 = o8+7
			paths.append(2)
		if m8 > 5:
			x = 6+4
			paths.append(3)
		else:
			m8 = m8-m8
			m8 = x/5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m8 = x**0.5
		return m8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))