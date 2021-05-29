import numpy as np 

def function(x):

	m3 = x
	u5 = 5
	paths = []
	try:
		if x > 7:
			m3 = x*m3
			paths.append(1)
		else:
			u5 = m3+m3
			m3 = x-m3
			x = 2*x
			paths.append(2)
		if u5 > 5:
			x = x*m3
			m3 = m3/9
			m3 = m3/6
			paths.append(3)
		else:
			x = m3+x
			x = u5-0
			u5 = x-u5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m3 = x**0.5
		return m3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))