import numpy as np 

def function(x):

	m3 = 4
	r0 = x
	paths = []
	try:
		if r0 >= 0:
			x = r0*7
			paths.append(1)
		else:
			m3 = 8+m3
			paths.append(2)
		if x <= 8:
			r0 = x-m3
			m3 = 2*7
			paths.append(3)
		else:
			m3 = m3/7
			m3 = 8*m3
			x = 1-x
			paths.append(4)
		paths.append(5)
		assert r0 >= 0
		x = r0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))