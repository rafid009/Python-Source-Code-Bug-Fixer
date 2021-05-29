import numpy as np 

def function(x):

	m9 = x
	k0 = x
	paths = []
	try:
		if m9 <= 1:
			k0 = 5+k0
			paths.append(1)
		else:
			k0 = k0-7
			paths.append(2)
		if x < 4:
			m9 = k0-m9
			paths.append(3)
		else:
			m9 = m9+2
			paths.append(4)
		paths.append(5)
		assert m9 >= 0
		m9 = m9**0.5
		return m9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))