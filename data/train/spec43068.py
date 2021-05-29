import numpy as np 

def function(x):

	m3 = 9
	e1 = 0
	x = x
	paths = []
	try:
		if e1 <= 0:
			e1 = e1-3
			paths.append(1)
		else:
			e1 = x-9
			e1 = 7*e1
			x = 8+x
			paths.append(2)
		if m3 > 2:
			x = 1+x
			m3 = 4-3
			x = x-2
			paths.append(3)
		else:
			e1 = e1+e1
			m3 = x+m3
			paths.append(4)
		paths.append(5)
		assert e1 >= 0
		e1 = e1**0.5
		return e1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))