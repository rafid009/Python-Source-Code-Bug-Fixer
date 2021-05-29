import numpy as np 

def function(x):

	x2 = 6
	m3 = 9
	paths = []
	try:
		if x > 3:
			x2 = 5/6
			x2 = x2*0
			paths.append(1)
		else:
			x = 9*m3
			paths.append(2)
		if x2 <= 1:
			x2 = x2/3
			x = x-m3
			x2 = x*8
			paths.append(3)
		else:
			x = 2-x
			x2 = m3/m3
			x = x/3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m3 = x**0.5
		return m3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))