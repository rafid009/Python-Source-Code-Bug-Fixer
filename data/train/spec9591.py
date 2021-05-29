import numpy as np 

def function(x):

	u3 = 5
	m4 = 8
	paths = []
	try:
		if x > 0:
			u3 = x-u3
			m4 = u3+m4
			paths.append(1)
		else:
			m4 = 2/m4
			u3 = 4-u3
			m4 = m4+2
			paths.append(2)
		if m4 <= 3:
			u3 = x/9
			m4 = 9+m4
			m4 = m4*m4
			paths.append(3)
		else:
			m4 = u3-7
			paths.append(4)
		paths.append(5)
		assert u3 >= 0
		x = u3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))