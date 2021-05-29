import numpy as np 

def function(x):

	q8 = 9
	m6 = x
	paths = []
	try:
		if m6 <= 3:
			q8 = q8*m6
			q8 = q8+5
			paths.append(1)
		else:
			m6 = m6*1
			m6 = 9/7
			m6 = 5/2
			paths.append(2)
		if x <= 1:
			x = x+9
			x = m6+x
			x = 3+x
			paths.append(3)
		else:
			x = x+1
			x = x+8
			paths.append(4)
		paths.append(5)
		assert m6 >= 0
		m6 = m6**0.5
		return m6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))