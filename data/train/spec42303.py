import numpy as np 

def function(x):

	p1 = x
	m9 = x
	paths = []
	try:
		if x >= 1:
			p1 = p1+x
			m9 = p1-5
			x = 3/p1
			paths.append(1)
		else:
			p1 = p1+1
			x = x/4
			m9 = m9+m9
			paths.append(2)
		if x < 9:
			x = m9*7
			paths.append(3)
		else:
			m9 = m9*0
			x = p1/x
			p1 = 2/p1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m9 = x**0.5
		return m9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))