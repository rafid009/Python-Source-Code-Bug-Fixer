import numpy as np 

def function(x):

	e8 = x
	m5 = x
	paths = []
	try:
		if e8 <= 9:
			x = 6+m5
			x = 9/m5
			m5 = x*9
			paths.append(1)
		else:
			e8 = e8-8
			m5 = 9*m5
			paths.append(2)
		if x >= 9:
			m5 = m5-x
			m5 = m5+e8
			m5 = 5+e8
			paths.append(3)
		else:
			x = 7*6
			m5 = m5+m5
			e8 = 5-9
			paths.append(4)
		paths.append(5)
		assert e8 >= 0
		e8 = e8**0.5
		return e8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))