import numpy as np 

def function(x):

	u9 = x
	m6 = x
	paths = []
	try:
		if x > 8:
			m6 = 3-m6
			paths.append(1)
		else:
			x = 7-x
			m6 = m6+u9
			paths.append(2)
		if m6 <= 5:
			x = 7-2
			x = x+3
			u9 = u9/m6
			paths.append(3)
		else:
			m6 = 9*9
			m6 = 7+m6
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