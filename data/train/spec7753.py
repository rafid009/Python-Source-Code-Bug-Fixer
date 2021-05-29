import numpy as np 

def function(x):

	z2 = x
	m3 = x
	paths = []
	try:
		if x <= 2:
			m3 = m3*5
			x = 5-x
			paths.append(1)
		else:
			x = x/2
			x = x/m3
			x = x-2
			paths.append(2)
		if z2 < 7:
			m3 = m3*2
			x = x+5
			x = x-4
			paths.append(3)
		else:
			m3 = m3/1
			x = 6-m3
			x = x+z2
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