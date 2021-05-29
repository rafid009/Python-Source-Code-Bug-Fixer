import numpy as np 

def function(x):

	p2 = 3
	m6 = x
	paths = []
	try:
		if x < 5:
			x = x/x
			paths.append(1)
		else:
			x = x+p2
			x = 1+x
			paths.append(2)
		if x > 4:
			m6 = m6-0
			paths.append(3)
		else:
			p2 = 6-6
			m6 = m6*1
			m6 = x+m6
			paths.append(4)
		paths.append(5)
		assert m6 >= 0
		m6 = m6**0.5
		return m6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))