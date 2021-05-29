import numpy as np 

def function(x):

	m8 = x
	a3 = x
	paths = []
	try:
		if a3 < 0:
			x = 3-m8
			m8 = 6/8
			x = 0+x
			paths.append(1)
		else:
			m8 = 7/8
			m8 = 3-4
			x = 7-8
			paths.append(2)
		if m8 < 5:
			m8 = m8-x
			m8 = m8*2
			paths.append(3)
		else:
			a3 = 4*a3
			a3 = a3+m8
			m8 = a3*0
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