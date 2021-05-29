import numpy as np 

def function(x):

	m8 = x
	h5 = x
	paths = []
	try:
		if m8 < 4:
			m8 = 1/2
			h5 = m8*h5
			paths.append(1)
		else:
			m8 = m8+0
			paths.append(2)
		if m8 <= 8:
			x = x*5
			paths.append(3)
		else:
			m8 = 5-x
			x = x*0
			m8 = m8+m8
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