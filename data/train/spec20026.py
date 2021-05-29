import numpy as np 

def function(x):

	v5 = 5
	m7 = x
	paths = []
	try:
		if x <= 9:
			v5 = m7+8
			m7 = 2+m7
			x = 5+x
			paths.append(1)
		else:
			v5 = x+v5
			m7 = m7/x
			v5 = m7*9
			paths.append(2)
		if v5 < 1:
			m7 = 6-2
			v5 = v5-2
			m7 = v5/m7
			paths.append(3)
		else:
			v5 = 6-v5
			m7 = m7-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m7 = x**0.5
		return m7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))