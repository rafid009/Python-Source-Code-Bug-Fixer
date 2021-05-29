import numpy as np 

def function(x):

	m1 = 2
	n8 = x
	paths = []
	try:
		if x < 4:
			m1 = 7*m1
			n8 = 3*2
			n8 = n8*1
			paths.append(1)
		else:
			n8 = n8+4
			x = 2-n8
			paths.append(2)
		if x > 8:
			m1 = m1*5
			paths.append(3)
		else:
			m1 = x/m1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m1 = x**0.5
		return m1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))