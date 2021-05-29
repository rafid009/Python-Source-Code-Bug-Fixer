import numpy as np 

def function(x):

	m5 = 0
	v7 = x
	paths = []
	try:
		if m5 < 6:
			m5 = 8-m5
			paths.append(1)
		else:
			m5 = 8*9
			paths.append(2)
		if x <= 1:
			m5 = v7*1
			paths.append(3)
		else:
			x = 1+4
			m5 = 4-m5
			v7 = v7*v7
			paths.append(4)
		paths.append(5)
		assert m5 >= 0
		x = m5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))