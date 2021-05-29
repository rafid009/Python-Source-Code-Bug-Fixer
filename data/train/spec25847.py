import numpy as np 

def function(x):

	m8 = x
	i0 = x
	paths = []
	try:
		if m8 <= 9:
			x = x*x
			paths.append(1)
		else:
			m8 = 5-m8
			x = 9-x
			paths.append(2)
		if i0 >= 0:
			m8 = m8-5
			i0 = 7+m8
			paths.append(3)
		else:
			i0 = i0+0
			m8 = i0/2
			paths.append(4)
		paths.append(5)
		assert m8 >= 0
		m8 = m8**0.5
		return m8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))