import numpy as np 

def function(x):

	m5 = x
	r0 = 6
	paths = []
	try:
		if r0 >= 2:
			x = x-r0
			x = x+x
			x = x/r0
			paths.append(1)
		else:
			r0 = r0*1
			m5 = m5+r0
			paths.append(2)
		if r0 > 2:
			m5 = m5*1
			paths.append(3)
		else:
			r0 = 6*r0
			m5 = 5-m5
			r0 = 2*4
			paths.append(4)
		paths.append(5)
		assert m5 >= 0
		r0 = m5**0.5
		return r0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))