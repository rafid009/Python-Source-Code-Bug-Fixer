import numpy as np 

def function(x):

	u4 = 6
	m2 = 5
	paths = []
	try:
		if m2 > 7:
			m2 = m2*4
			m2 = 7-m2
			m2 = m2+5
			paths.append(1)
		else:
			m2 = 6/6
			paths.append(2)
		if u4 >= 7:
			x = m2/9
			u4 = u4/2
			u4 = 4-u4
			paths.append(3)
		else:
			m2 = m2-7
			x = m2-8
			paths.append(4)
		paths.append(5)
		assert m2 >= 0
		u4 = m2**0.5
		return u4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))