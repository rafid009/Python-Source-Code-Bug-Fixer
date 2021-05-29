import numpy as np 

def function(x):

	m0 = x
	m1 = x
	paths = []
	try:
		if x > 1:
			m0 = m0-9
			m1 = 1/m1
			paths.append(1)
		else:
			m0 = m0+7
			m0 = 7+m0
			x = 8*m0
			paths.append(2)
		if m1 <= 4:
			m0 = x+m1
			paths.append(3)
		else:
			x = x/7
			m0 = m0*2
			m0 = m0+0
			paths.append(4)
		paths.append(5)
		assert m1 >= 0
		m1 = m1**0.5
		return m1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))