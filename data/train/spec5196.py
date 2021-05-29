import numpy as np 

def function(x):

	m7 = 3
	l5 = x
	paths = []
	try:
		if l5 < 3:
			x = l5*0
			m7 = m7*l5
			paths.append(1)
		else:
			l5 = 6-l5
			x = m7*8
			m7 = m7*7
			paths.append(2)
		if l5 < 7:
			x = l5*3
			m7 = l5-l5
			l5 = m7+8
			paths.append(3)
		else:
			m7 = m7/m7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l5 = x**0.5
		return l5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))