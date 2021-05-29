import numpy as np 

def function(x):

	b2 = x
	m4 = x
	paths = []
	try:
		if x < 8:
			x = x+5
			paths.append(1)
		else:
			x = 7*b2
			m4 = m4/1
			paths.append(2)
		if m4 <= 8:
			x = x-3
			b2 = b2+b2
			b2 = x+x
			paths.append(3)
		else:
			m4 = 0+0
			paths.append(4)
		paths.append(5)
		assert b2 >= 0
		m4 = b2**0.5
		return m4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))