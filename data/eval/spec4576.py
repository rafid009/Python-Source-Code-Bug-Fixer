import numpy as np 

def function(x):

	j7 = 3
	m7 = 4
	paths = []
	try:
		if j7 <= 4:
			m7 = 5+m7
			m7 = m7+3
			paths.append(1)
		else:
			m7 = 6+m7
			j7 = 0-7
			paths.append(2)
		if x < 7:
			m7 = m7+4
			m7 = m7/1
			x = x/1
			paths.append(3)
		else:
			x = x+8
			x = x+x
			x = x*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m7 = x**0.5
		return m7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))