import numpy as np 

def function(x):

	m3 = x
	w8 = x
	paths = []
	try:
		if x <= 8:
			m3 = 0+m3
			m3 = m3+1
			paths.append(1)
		else:
			m3 = m3+1
			paths.append(2)
		if x >= 7:
			x = m3*4
			m3 = m3*m3
			m3 = x+m3
			paths.append(3)
		else:
			m3 = 0+m3
			w8 = 2+7
			m3 = w8*m3
			paths.append(4)
		paths.append(5)
		assert m3 >= 0
		x = m3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))