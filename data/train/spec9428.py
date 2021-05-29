import numpy as np 

def function(x):

	e3 = 1
	m5 = 8
	paths = []
	try:
		if x > 9:
			e3 = 8/e3
			x = x/4
			x = x-4
			paths.append(1)
		else:
			m5 = 9-m5
			m5 = x+m5
			x = x-m5
			paths.append(2)
		if m5 <= 6:
			e3 = e3+7
			paths.append(3)
		else:
			e3 = e3/7
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