import numpy as np 

def function(x):

	v6 = x
	m4 = x
	paths = []
	try:
		if m4 > 4:
			m4 = 4*m4
			m4 = 8/7
			v6 = x+0
			paths.append(1)
		else:
			x = x-5
			v6 = 7+v6
			paths.append(2)
		if m4 < 2:
			m4 = v6*m4
			v6 = 5+v6
			x = 2/8
			paths.append(3)
		else:
			m4 = 4*m4
			paths.append(4)
		paths.append(5)
		assert v6 >= 0
		m4 = v6**0.5
		return m4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))