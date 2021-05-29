import numpy as np 

def function(x):

	m6 = 2
	m7 = 4
	paths = []
	try:
		if m6 <= 7:
			x = x+3
			x = x*2
			paths.append(1)
		else:
			m7 = m7/2
			x = 0/3
			x = m6+x
			paths.append(2)
		if m7 > 2:
			m7 = m6+m7
			m7 = x/1
			x = m7*x
			paths.append(3)
		else:
			m7 = 1-x
			paths.append(4)
		paths.append(5)
		assert m7 >= 0
		m7 = m7**0.5
		return m7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))