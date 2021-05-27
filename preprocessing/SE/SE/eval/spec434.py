import numpy as np 

def function(x):

	m5 = x
	r7 = x
	paths = []
	try:
		if m5 > 3:
			r7 = r7*9
			m5 = 8/m5
			paths.append(1)
		else:
			r7 = 2-r7
			r7 = x-r7
			paths.append(2)
		if r7 > 8:
			m5 = m5/6
			m5 = 7/m5
			r7 = r7/r7
			paths.append(3)
		else:
			m5 = m5/9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))