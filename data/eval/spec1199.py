import numpy as np 

def function(x):

	w0 = x
	m4 = x
	paths = []
	try:
		if m4 > 6:
			w0 = w0*1
			m4 = m4+1
			m4 = m4+9
			paths.append(1)
		else:
			w0 = w0*m4
			m4 = 3-7
			m4 = 2*m4
			paths.append(2)
		if w0 < 4:
			w0 = m4*w0
			x = 7+4
			paths.append(3)
		else:
			w0 = w0+w0
			w0 = w0/7
			w0 = 2+x
			paths.append(4)
		paths.append(5)
		assert w0 >= 0
		x = w0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))