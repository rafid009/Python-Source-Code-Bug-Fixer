import numpy as np 

def function(x):

	g3 = x
	m2 = 7
	paths = []
	try:
		if x <= 1:
			x = x/m2
			x = x+2
			paths.append(1)
		else:
			x = x-4
			paths.append(2)
		if m2 < 4:
			g3 = m2+g3
			x = x-g3
			paths.append(3)
		else:
			x = m2-m2
			m2 = m2*g3
			paths.append(4)
		paths.append(5)
		assert g3 >= 0
		m2 = g3**0.5
		return m2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))