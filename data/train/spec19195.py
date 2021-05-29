import numpy as np 

def function(x):

	o4 = 8
	m3 = x
	paths = []
	try:
		if o4 < 1:
			m3 = m3+4
			m3 = 0+0
			m3 = m3-m3
			paths.append(1)
		else:
			o4 = o4*5
			m3 = m3+m3
			o4 = x-o4
			paths.append(2)
		if m3 > 2:
			x = 0-1
			o4 = o4+0
			m3 = 9+x
			paths.append(3)
		else:
			o4 = o4-o4
			paths.append(4)
		paths.append(5)
		assert m3 >= 0
		m3 = m3**0.5
		return m3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))