import numpy as np 

def function(x):

	m4 = x
	v4 = x
	paths = []
	try:
		if m4 > 9:
			m4 = 7-6
			paths.append(1)
		else:
			x = 4+x
			paths.append(2)
		if x >= 3:
			x = 2*x
			v4 = m4*v4
			m4 = 3*8
			paths.append(3)
		else:
			m4 = m4+m4
			paths.append(4)
		paths.append(5)
		assert v4 >= 0
		v4 = v4**0.5
		return v4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))