import numpy as np 

def function(x):

	m9 = x
	j8 = 7
	paths = []
	try:
		if j8 < 9:
			m9 = m9*7
			j8 = 1*5
			paths.append(1)
		else:
			j8 = 6-4
			paths.append(2)
		if x <= 1:
			m9 = m9+x
			m9 = j8+x
			j8 = 0+m9
			paths.append(3)
		else:
			m9 = m9-2
			paths.append(4)
		paths.append(5)
		assert j8 >= 0
		m9 = j8**0.5
		return m9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))