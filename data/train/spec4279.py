import numpy as np 

def function(x):

	u9 = x
	m7 = x
	paths = []
	try:
		if u9 <= 6:
			m7 = 0-0
			paths.append(1)
		else:
			u9 = 5-u9
			paths.append(2)
		if m7 <= 0:
			u9 = u9-1
			x = x+m7
			paths.append(3)
		else:
			m7 = m7+m7
			m7 = m7-0
			x = 1+4
			paths.append(4)
		paths.append(5)
		assert u9 >= 0
		u9 = u9**0.5
		return u9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))