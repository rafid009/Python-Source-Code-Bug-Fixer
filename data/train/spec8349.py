import numpy as np 

def function(x):

	m6 = 4
	x6 = x
	paths = []
	try:
		if x < 0:
			x = 4-6
			x6 = 8*1
			paths.append(1)
		else:
			x = x-x
			m6 = 3*0
			m6 = m6/2
			paths.append(2)
		if x6 > 7:
			x6 = 5/x6
			x = x*1
			x6 = m6/8
			paths.append(3)
		else:
			x6 = x6/9
			m6 = m6/3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m6 = x**0.5
		return m6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))