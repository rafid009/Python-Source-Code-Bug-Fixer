import numpy as np 

def function(x):

	m8 = 8
	p6 = x
	paths = []
	try:
		if p6 <= 3:
			m8 = m8*3
			paths.append(1)
		else:
			x = x/x
			m8 = 6-m8
			m8 = 0-9
			paths.append(2)
		if x >= 4:
			x = x*8
			p6 = 7/p6
			paths.append(3)
		else:
			x = p6+p6
			paths.append(4)
		paths.append(5)
		assert p6 >= 0
		p6 = p6**0.5
		return p6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))