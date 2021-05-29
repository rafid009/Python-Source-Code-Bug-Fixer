import numpy as np 

def function(x):

	m0 = x
	e3 = x
	x = x
	paths = []
	try:
		if e3 >= 4:
			m0 = m0*8
			x = m0/1
			m0 = m0+8
			paths.append(1)
		else:
			e3 = x+x
			paths.append(2)
		if x > 3:
			e3 = e3-m0
			x = x*x
			paths.append(3)
		else:
			m0 = 7*m0
			e3 = 4*e3
			paths.append(4)
		paths.append(5)
		assert e3 >= 0
		e3 = e3**0.5
		return e3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))