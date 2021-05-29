import numpy as np 

def function(x):

	m9 = 0
	a9 = x
	paths = []
	try:
		if m9 < 2:
			a9 = m9+x
			paths.append(1)
		else:
			a9 = a9+m9
			a9 = a9-3
			x = x+8
			paths.append(2)
		if a9 <= 3:
			x = 1+x
			paths.append(3)
		else:
			m9 = m9+0
			x = x+2
			a9 = a9/1
			paths.append(4)
		paths.append(5)
		assert a9 >= 0
		m9 = a9**0.5
		return m9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))