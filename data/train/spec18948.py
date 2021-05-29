import numpy as np 

def function(x):

	m6 = 8
	j5 = x
	paths = []
	try:
		if x <= 2:
			j5 = j5-2
			x = x*8
			j5 = j5-2
			paths.append(1)
		else:
			x = j5*2
			m6 = j5*4
			m6 = m6/m6
			paths.append(2)
		if m6 <= 6:
			j5 = 4/x
			m6 = m6+3
			paths.append(3)
		else:
			m6 = m6*5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j5 = x**0.5
		return j5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))