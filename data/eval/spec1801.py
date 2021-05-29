import numpy as np 

def function(x):

	m5 = 6
	f4 = x
	x = 6
	paths = []
	try:
		if f4 <= 4:
			x = x*7
			m5 = m5+m5
			m5 = 5+m5
			paths.append(1)
		else:
			m5 = 1+m5
			f4 = f4*6
			paths.append(2)
		if f4 < 5:
			f4 = x*7
			m5 = 5-m5
			f4 = f4*2
			paths.append(3)
		else:
			m5 = m5-8
			f4 = m5*f4
			m5 = 8/3
			paths.append(4)
		paths.append(5)
		assert m5 >= 0
		m5 = m5**0.5
		return m5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))