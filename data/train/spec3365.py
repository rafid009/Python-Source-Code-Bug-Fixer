import numpy as np 

def function(x):

	n1 = 6
	m5 = 7
	paths = []
	try:
		if x > 0:
			m5 = 2+m5
			paths.append(1)
		else:
			m5 = 6-m5
			m5 = m5+2
			paths.append(2)
		if m5 < 8:
			x = 3*0
			x = 1/n1
			paths.append(3)
		else:
			m5 = 6-m5
			x = x-m5
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