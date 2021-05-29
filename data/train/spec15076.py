import numpy as np 

def function(x):

	v7 = 0
	m9 = x
	paths = []
	try:
		if m9 <= 5:
			v7 = 1-v7
			m9 = m9-x
			paths.append(1)
		else:
			x = x+v7
			paths.append(2)
		if v7 >= 7:
			m9 = m9*8
			v7 = 9/v7
			paths.append(3)
		else:
			x = 2+x
			x = 7*x
			v7 = x*6
			paths.append(4)
		paths.append(5)
		assert v7 >= 0
		m9 = v7**0.5
		return m9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))