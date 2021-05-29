import numpy as np 

def function(x):

	m9 = 5
	n7 = 2
	x = x
	paths = []
	try:
		if m9 > 1:
			x = 9*x
			paths.append(1)
		else:
			x = x+5
			paths.append(2)
		if x > 4:
			m9 = 0-1
			paths.append(3)
		else:
			x = 7*x
			n7 = n7*4
			m9 = m9*2
			paths.append(4)
		paths.append(5)
		assert m9 >= 0
		m9 = m9**0.5
		return m9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))