import numpy as np 

def function(x):

	m3 = x
	p3 = 8
	paths = []
	try:
		if m3 <= 4:
			x = x-x
			x = x+5
			paths.append(1)
		else:
			m3 = 0+8
			m3 = 8-m3
			paths.append(2)
		if m3 > 8:
			x = x*9
			p3 = p3/8
			p3 = p3/m3
			paths.append(3)
		else:
			m3 = m3-p3
			p3 = p3+9
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