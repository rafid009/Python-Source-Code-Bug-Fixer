import numpy as np 

def function(x):

	m7 = x
	p7 = x
	x = x
	paths = []
	try:
		if p7 < 6:
			p7 = p7*0
			paths.append(1)
		else:
			m7 = 0*m7
			p7 = p7+4
			paths.append(2)
		if x > 3:
			m7 = 6-p7
			paths.append(3)
		else:
			x = x/x
			p7 = p7-4
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