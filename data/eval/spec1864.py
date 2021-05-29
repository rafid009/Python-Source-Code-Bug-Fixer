import numpy as np 

def function(x):

	m1 = x
	r0 = x
	paths = []
	try:
		if m1 < 8:
			m1 = m1*m1
			x = x*7
			paths.append(1)
		else:
			r0 = 1+r0
			paths.append(2)
		if m1 <= 3:
			m1 = m1*7
			r0 = 3*2
			paths.append(3)
		else:
			r0 = r0*9
			x = x/x
			r0 = 3/r0
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