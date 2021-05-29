import numpy as np 

def function(x):

	f4 = x
	m5 = 5
	paths = []
	try:
		if f4 <= 4:
			x = 0/x
			x = 5/5
			paths.append(1)
		else:
			f4 = f4-x
			m5 = m5*7
			m5 = m5-7
			paths.append(2)
		if m5 <= 4:
			x = x+f4
			m5 = 6*m5
			f4 = f4/m5
			paths.append(3)
		else:
			x = 0+x
			m5 = m5*m5
			paths.append(4)
		paths.append(5)
		assert f4 >= 0
		m5 = f4**0.5
		return m5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))