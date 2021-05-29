import numpy as np 

def function(x):

	e2 = 3
	m2 = x
	paths = []
	try:
		if m2 <= 1:
			x = 7+x
			x = x/4
			paths.append(1)
		else:
			m2 = 6*8
			paths.append(2)
		if e2 <= 4:
			e2 = 0+e2
			e2 = m2+e2
			paths.append(3)
		else:
			x = x+2
			paths.append(4)
		paths.append(5)
		assert e2 >= 0
		e2 = e2**0.5
		return e2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))