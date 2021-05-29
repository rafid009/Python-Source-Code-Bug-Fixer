import numpy as np 

def function(x):

	m8 = x
	j8 = x
	paths = []
	try:
		if j8 >= 6:
			j8 = j8+j8
			m8 = m8*6
			x = 0+j8
			paths.append(1)
		else:
			j8 = 2-j8
			m8 = 8*m8
			paths.append(2)
		if m8 <= 3:
			j8 = 4+j8
			j8 = j8/6
			paths.append(3)
		else:
			x = j8/9
			m8 = 2/m8
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