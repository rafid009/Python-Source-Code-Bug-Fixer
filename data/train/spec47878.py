import numpy as np 

def function(x):

	p3 = x
	m9 = x
	paths = []
	try:
		if p3 >= 9:
			m9 = m9+x
			m9 = m9+9
			m9 = m9/2
			paths.append(1)
		else:
			x = x/1
			paths.append(2)
		if p3 >= 9:
			x = 3*5
			p3 = 6/8
			paths.append(3)
		else:
			x = 3*x
			m9 = 9*m9
			paths.append(4)
		paths.append(5)
		assert p3 >= 0
		p3 = p3**0.5
		return p3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))