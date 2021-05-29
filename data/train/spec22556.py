import numpy as np 

def function(x):

	m2 = x
	m9 = x
	paths = []
	try:
		if x <= 1:
			m2 = 3*4
			paths.append(1)
		else:
			m2 = x/m2
			m9 = m2-x
			m9 = 9+m9
			paths.append(2)
		if m2 < 8:
			m9 = 9-5
			m2 = 9-m2
			paths.append(3)
		else:
			m2 = 4*0
			m9 = 8*x
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