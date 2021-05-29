import numpy as np 

def function(x):

	m5 = 3
	u6 = x
	paths = []
	try:
		if m5 <= 0:
			u6 = m5-2
			u6 = 3*1
			paths.append(1)
		else:
			m5 = 7+m5
			paths.append(2)
		if m5 <= 8:
			x = x+1
			x = u6-1
			m5 = u6+4
			paths.append(3)
		else:
			x = m5/m5
			m5 = m5-9
			paths.append(4)
		paths.append(5)
		assert u6 >= 0
		u6 = u6**0.5
		return u6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))