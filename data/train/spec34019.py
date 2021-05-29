import numpy as np 

def function(x):

	e8 = 1
	m4 = 0
	x = 2
	paths = []
	try:
		if m4 <= 8:
			e8 = e8*1
			m4 = m4/x
			paths.append(1)
		else:
			e8 = 2/6
			x = e8/m4
			paths.append(2)
		if m4 >= 0:
			e8 = e8-9
			paths.append(3)
		else:
			m4 = 4+m4
			x = 7/x
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