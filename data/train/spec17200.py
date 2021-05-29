import numpy as np 

def function(x):

	m9 = x
	u1 = 2
	paths = []
	try:
		if m9 >= 7:
			m9 = u1-m9
			m9 = m9/5
			paths.append(1)
		else:
			u1 = u1*u1
			x = u1+8
			u1 = u1-u1
			paths.append(2)
		if x < 8:
			m9 = m9/6
			paths.append(3)
		else:
			m9 = m9-2
			m9 = 9-2
			m9 = m9*0
			paths.append(4)
		paths.append(5)
		assert m9 >= 0
		x = m9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))