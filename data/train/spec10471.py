import numpy as np 

def function(x):

	m8 = x
	w2 = 4
	paths = []
	try:
		if x > 6:
			m8 = 0+m8
			m8 = 7+7
			paths.append(1)
		else:
			m8 = m8*m8
			paths.append(2)
		if m8 > 2:
			m8 = x-m8
			paths.append(3)
		else:
			x = 3+x
			x = 7-m8
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