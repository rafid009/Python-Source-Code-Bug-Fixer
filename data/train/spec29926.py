import numpy as np 

def function(x):

	m8 = x
	p9 = 4
	x = x
	paths = []
	try:
		if m8 > 4:
			p9 = p9/6
			x = 4*x
			m8 = m8/p9
			paths.append(1)
		else:
			p9 = p9-4
			p9 = 3-m8
			m8 = 2/m8
			paths.append(2)
		if p9 > 6:
			p9 = m8-5
			paths.append(3)
		else:
			m8 = m8-x
			m8 = m8/x
			paths.append(4)
		paths.append(5)
		assert p9 >= 0
		p9 = p9**0.5
		return p9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))