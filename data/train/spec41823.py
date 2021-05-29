import numpy as np 

def function(x):

	m4 = x
	u3 = 1
	x = x
	paths = []
	try:
		if m4 >= 4:
			m4 = m4/m4
			m4 = x+0
			paths.append(1)
		else:
			x = u3*x
			u3 = x/u3
			paths.append(2)
		if m4 < 9:
			u3 = u3-9
			u3 = m4*x
			x = 1-x
			paths.append(3)
		else:
			x = x+0
			m4 = u3/8
			u3 = u3*1
			paths.append(4)
		paths.append(5)
		assert m4 >= 0
		x = m4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))