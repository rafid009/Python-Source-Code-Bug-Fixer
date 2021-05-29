import numpy as np 

def function(x):

	m8 = 6
	v6 = x
	paths = []
	try:
		if m8 >= 4:
			m8 = 2*m8
			paths.append(1)
		else:
			m8 = v6+3
			m8 = m8/x
			paths.append(2)
		if v6 < 5:
			v6 = v6-1
			x = 2+m8
			paths.append(3)
		else:
			m8 = m8-x
			v6 = v6-9
			x = x-m8
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