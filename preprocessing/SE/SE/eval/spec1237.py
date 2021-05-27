import numpy as np 

def function(x):

	m2 = x
	r4 = 4
	paths = []
	try:
		if m2 < 8:
			m2 = m2*m2
			m2 = m2*r4
			x = 0+x
			paths.append(1)
		else:
			x = x*5
			x = x*m2
			r4 = 4+m2
			paths.append(2)
		if x > 3:
			x = x*3
			x = x*0
			x = x*r4
			paths.append(3)
		else:
			m2 = 3/m2
			r4 = r4+0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m2 = x**0.5
		return m2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))