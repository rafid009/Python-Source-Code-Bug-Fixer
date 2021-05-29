import numpy as np 

def function(x):

	r5 = x
	m2 = 2
	x = x
	paths = []
	try:
		if r5 < 8:
			m2 = m2+1
			x = x*1
			r5 = r5*m2
			paths.append(1)
		else:
			x = x*m2
			paths.append(2)
		if m2 <= 1:
			m2 = x-r5
			r5 = r5*1
			r5 = r5/6
			paths.append(3)
		else:
			x = x+r5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m2 = x**0.5
		return m2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))