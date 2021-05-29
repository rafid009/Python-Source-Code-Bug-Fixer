import numpy as np 

def function(x):

	w8 = x
	m5 = 7
	paths = []
	try:
		if x >= 2:
			x = x/5
			m5 = 8*5
			paths.append(1)
		else:
			w8 = 7*w8
			w8 = m5/w8
			m5 = w8/8
			paths.append(2)
		if x >= 8:
			m5 = m5*5
			w8 = w8*5
			paths.append(3)
		else:
			m5 = 7+m5
			m5 = m5*x
			m5 = 4+x
			paths.append(4)
		paths.append(5)
		assert w8 >= 0
		m5 = w8**0.5
		return m5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))