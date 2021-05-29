import numpy as np 

def function(x):

	m5 = x
	u6 = x
	paths = []
	try:
		if x > 8:
			x = 2/x
			m5 = m5-1
			m5 = m5+7
			paths.append(1)
		else:
			m5 = u6+x
			paths.append(2)
		if x >= 8:
			x = x*0
			u6 = 8-u6
			paths.append(3)
		else:
			u6 = u6/7
			u6 = 0-4
			paths.append(4)
		paths.append(5)
		assert m5 >= 0
		m5 = m5**0.5
		return m5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))