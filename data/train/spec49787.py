import numpy as np 

def function(x):

	m1 = x
	u9 = 8
	paths = []
	try:
		if m1 <= 2:
			m1 = u9*x
			m1 = m1/u9
			m1 = 2/x
			paths.append(1)
		else:
			x = 9*8
			u9 = u9-u9
			paths.append(2)
		if u9 > 5:
			x = 4/x
			u9 = 5/m1
			x = x/2
			paths.append(3)
		else:
			u9 = m1+2
			m1 = x+9
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