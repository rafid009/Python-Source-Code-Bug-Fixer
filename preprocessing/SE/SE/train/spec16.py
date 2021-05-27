import numpy as np 

def function(x):

	e2 = 4
	m2 = x
	paths = []
	try:
		if m2 < 5:
			e2 = 6+7
			paths.append(1)
		else:
			m2 = m2+1
			e2 = e2+2
			x = x/x
			paths.append(2)
		if e2 > 3:
			e2 = m2*e2
			m2 = x/3
			paths.append(3)
		else:
			x = x-m2
			paths.append(4)
		paths.append(5)
		assert e2 >= 0
		m2 = e2**0.5
		return m2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))