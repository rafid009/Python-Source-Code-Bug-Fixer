import numpy as np 

def function(x):

	m3 = 3
	o4 = x
	paths = []
	try:
		if o4 <= 8:
			m3 = 8+x
			o4 = 3/7
			paths.append(1)
		else:
			o4 = o4/o4
			x = 8*1
			paths.append(2)
		if o4 >= 8:
			x = 7/m3
			paths.append(3)
		else:
			x = 2*m3
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