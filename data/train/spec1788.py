import numpy as np 

def function(x):

	r5 = 5
	m4 = x
	paths = []
	try:
		if r5 < 5:
			m4 = m4+x
			r5 = x-8
			paths.append(1)
		else:
			x = 5*x
			m4 = 5+m4
			paths.append(2)
		if m4 <= 2:
			x = x+9
			x = x-m4
			x = 5/5
			paths.append(3)
		else:
			m4 = 0+r5
			r5 = m4+r5
			paths.append(4)
		paths.append(5)
		assert m4 >= 0
		x = m4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))