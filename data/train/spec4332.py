import numpy as np 

def function(x):

	a3 = x
	m7 = 0
	paths = []
	try:
		if x > 7:
			m7 = 8*m7
			m7 = m7*m7
			paths.append(1)
		else:
			x = x+3
			paths.append(2)
		if m7 < 0:
			m7 = m7*8
			paths.append(3)
		else:
			x = 7+x
			x = x*9
			a3 = m7-m7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a3 = x**0.5
		return a3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))