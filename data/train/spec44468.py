import numpy as np 

def function(x):

	b1 = 5
	m2 = 9
	paths = []
	try:
		if m2 < 2:
			m2 = 6+m2
			b1 = 8-b1
			paths.append(1)
		else:
			x = x+m2
			m2 = x+9
			b1 = 3/b1
			paths.append(2)
		if b1 > 8:
			b1 = 1+b1
			m2 = m2-m2
			x = 8-1
			paths.append(3)
		else:
			x = 8*x
			m2 = m2/6
			m2 = b1*m2
			paths.append(4)
		paths.append(5)
		assert m2 >= 0
		m2 = m2**0.5
		return m2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))