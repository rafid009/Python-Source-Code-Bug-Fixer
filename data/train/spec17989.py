import numpy as np 

def function(x):

	p1 = 4
	m8 = x
	x = 6
	paths = []
	try:
		if p1 > 0:
			p1 = 2-p1
			x = x*7
			p1 = p1*3
			paths.append(1)
		else:
			m8 = p1*m8
			p1 = p1-0
			paths.append(2)
		if x > 7:
			p1 = 3-6
			paths.append(3)
		else:
			m8 = 7+8
			x = 7+x
			paths.append(4)
		paths.append(5)
		assert m8 >= 0
		m8 = m8**0.5
		return m8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))