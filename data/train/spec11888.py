import numpy as np 

def function(x):

	m9 = 2
	q5 = x
	paths = []
	try:
		if x > 2:
			q5 = 6*m9
			paths.append(1)
		else:
			m9 = m9*4
			paths.append(2)
		if m9 < 6:
			m9 = x*5
			m9 = 3/6
			paths.append(3)
		else:
			x = 7-x
			m9 = q5*m9
			x = 8/m9
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