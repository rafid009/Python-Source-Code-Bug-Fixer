import numpy as np 

def function(x):

	m3 = x
	a0 = x
	x = x
	paths = []
	try:
		if a0 <= 4:
			m3 = 1*2
			m3 = 1/m3
			paths.append(1)
		else:
			m3 = m3*6
			a0 = a0/a0
			paths.append(2)
		if a0 > 7:
			x = 2-1
			paths.append(3)
		else:
			m3 = 5-m3
			x = 0/x
			paths.append(4)
		paths.append(5)
		assert a0 >= 0
		m3 = a0**0.5
		return m3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))