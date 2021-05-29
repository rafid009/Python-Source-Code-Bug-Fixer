import numpy as np 

def function(x):

	r1 = x
	m0 = x
	paths = []
	try:
		if x > 0:
			x = 3*2
			m0 = m0+r1
			r1 = x*r1
			paths.append(1)
		else:
			r1 = r1+5
			x = x+5
			paths.append(2)
		if m0 <= 8:
			r1 = r1-4
			r1 = 8-r1
			paths.append(3)
		else:
			x = r1+9
			paths.append(4)
		paths.append(5)
		assert m0 >= 0
		x = m0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))