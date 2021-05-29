import numpy as np 

def function(x):

	w6 = 0
	m5 = 2
	paths = []
	try:
		if m5 > 0:
			x = 1+m5
			x = x-4
			w6 = m5-x
			paths.append(1)
		else:
			x = x+1
			x = x/m5
			m5 = m5/1
			paths.append(2)
		if m5 < 1:
			w6 = w6*4
			m5 = 3*x
			x = x+w6
			paths.append(3)
		else:
			x = x*m5
			m5 = m5-4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m5 = x**0.5
		return m5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))