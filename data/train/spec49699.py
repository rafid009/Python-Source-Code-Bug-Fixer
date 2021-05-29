import numpy as np 

def function(x):

	m0 = 2
	e9 = x
	paths = []
	try:
		if e9 > 8:
			m0 = m0+1
			e9 = 7-e9
			paths.append(1)
		else:
			x = x+6
			e9 = 2*2
			m0 = 5*m0
			paths.append(2)
		if x >= 4:
			m0 = 0+1
			m0 = m0/2
			paths.append(3)
		else:
			e9 = e9/e9
			x = e9*e9
			x = x/3
			paths.append(4)
		paths.append(5)
		assert e9 >= 0
		m0 = e9**0.5
		return m0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))