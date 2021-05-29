import numpy as np 

def function(x):

	m1 = 2
	a2 = x
	paths = []
	try:
		if a2 < 2:
			x = x*a2
			m1 = 2-7
			paths.append(1)
		else:
			x = x*2
			a2 = 6-3
			paths.append(2)
		if m1 <= 5:
			x = 5-x
			x = 5-x
			m1 = m1*4
			paths.append(3)
		else:
			a2 = a2*8
			paths.append(4)
		paths.append(5)
		assert m1 >= 0
		m1 = m1**0.5
		return m1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))