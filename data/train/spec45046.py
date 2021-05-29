import numpy as np 

def function(x):

	g9 = x
	m9 = x
	paths = []
	try:
		if m9 > 9:
			m9 = m9*0
			paths.append(1)
		else:
			m9 = 7-m9
			paths.append(2)
		if x >= 1:
			x = x-m9
			g9 = g9+1
			paths.append(3)
		else:
			x = 0/x
			m9 = g9-6
			x = g9-8
			paths.append(4)
		paths.append(5)
		assert g9 >= 0
		m9 = g9**0.5
		return m9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))