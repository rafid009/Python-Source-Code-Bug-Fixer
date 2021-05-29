import numpy as np 

def function(x):

	m3 = 6
	r8 = 0
	paths = []
	try:
		if r8 >= 9:
			x = x/7
			m3 = m3*x
			x = r8+x
			paths.append(1)
		else:
			x = x-8
			r8 = r8-7
			x = m3-x
			paths.append(2)
		if m3 < 7:
			m3 = r8/8
			x = r8+r8
			r8 = 8+r8
			paths.append(3)
		else:
			r8 = r8/3
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