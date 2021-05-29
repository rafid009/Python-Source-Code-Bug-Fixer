import numpy as np 

def function(x):

	m4 = 0
	v8 = 4
	paths = []
	try:
		if v8 < 8:
			x = x*5
			x = x-7
			m4 = m4+1
			paths.append(1)
		else:
			x = x+0
			paths.append(2)
		if m4 <= 1:
			m4 = m4/m4
			v8 = v8*1
			paths.append(3)
		else:
			m4 = 6+m4
			m4 = m4+x
			v8 = 0*v8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m4 = x**0.5
		return m4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))