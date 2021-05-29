import numpy as np 

def function(x):

	m4 = x
	u2 = 4
	paths = []
	try:
		if m4 > 4:
			m4 = 1-m4
			x = 5/x
			paths.append(1)
		else:
			x = x+x
			x = x+7
			m4 = x*1
			paths.append(2)
		if x > 7:
			u2 = u2-3
			paths.append(3)
		else:
			x = x*9
			paths.append(4)
		paths.append(5)
		assert m4 >= 0
		m4 = m4**0.5
		return m4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))