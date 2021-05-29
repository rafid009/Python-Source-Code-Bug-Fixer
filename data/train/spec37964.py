import numpy as np 

def function(x):

	m3 = x
	r1 = 9
	paths = []
	try:
		if r1 <= 9:
			m3 = m3/m3
			paths.append(1)
		else:
			r1 = r1+0
			m3 = 0*m3
			m3 = m3/4
			paths.append(2)
		if m3 >= 4:
			r1 = r1*8
			x = 7*5
			m3 = 2/x
			paths.append(3)
		else:
			r1 = x+r1
			x = x+x
			m3 = 3*r1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r1 = x**0.5
		return r1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))