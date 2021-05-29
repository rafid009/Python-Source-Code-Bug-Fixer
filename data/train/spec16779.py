import numpy as np 

def function(x):

	e5 = 6
	m5 = x
	paths = []
	try:
		if x < 9:
			e5 = x+e5
			m5 = 1/m5
			paths.append(1)
		else:
			e5 = e5/e5
			x = x-9
			e5 = e5-x
			paths.append(2)
		if m5 >= 0:
			x = x/6
			e5 = e5*0
			paths.append(3)
		else:
			x = x/8
			m5 = m5-6
			m5 = m5+e5
			paths.append(4)
		paths.append(5)
		assert m5 >= 0
		e5 = m5**0.5
		return e5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))