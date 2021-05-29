import numpy as np 

def function(x):

	b1 = x
	m7 = 4
	paths = []
	try:
		if x <= 8:
			x = x+b1
			m7 = 6-3
			paths.append(1)
		else:
			m7 = 1*x
			m7 = m7*x
			x = x/1
			paths.append(2)
		if m7 > 5:
			m7 = m7*x
			x = b1-x
			paths.append(3)
		else:
			x = 7/x
			b1 = 5+b1
			m7 = m7/b1
			paths.append(4)
		paths.append(5)
		assert m7 >= 0
		b1 = m7**0.5
		return b1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))