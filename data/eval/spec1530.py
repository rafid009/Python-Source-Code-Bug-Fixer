import numpy as np 

def function(x):

	r8 = 5
	m1 = 9
	paths = []
	try:
		if r8 > 8:
			r8 = x+r8
			paths.append(1)
		else:
			m1 = 6-m1
			r8 = r8-x
			paths.append(2)
		if x >= 4:
			x = x-0
			paths.append(3)
		else:
			m1 = m1+5
			r8 = 9*2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m1 = x**0.5
		return m1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))