import numpy as np 

def function(x):

	m8 = x
	f4 = x
	paths = []
	try:
		if m8 >= 2:
			m8 = 3+m8
			paths.append(1)
		else:
			m8 = m8*0
			x = x/1
			f4 = 4+f4
			paths.append(2)
		if x >= 3:
			m8 = 7*m8
			paths.append(3)
		else:
			x = m8-x
			m8 = 9+f4
			f4 = f4*x
			paths.append(4)
		paths.append(5)
		assert f4 >= 0
		m8 = f4**0.5
		return m8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))