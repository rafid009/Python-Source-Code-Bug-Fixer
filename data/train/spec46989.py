import numpy as np 

def function(x):

	m7 = x
	r2 = 5
	paths = []
	try:
		if r2 <= 8:
			r2 = 6-r2
			paths.append(1)
		else:
			r2 = r2*m7
			x = r2/5
			r2 = m7/7
			paths.append(2)
		if r2 < 4:
			m7 = 8/m7
			r2 = x/m7
			r2 = r2*r2
			paths.append(3)
		else:
			x = x/1
			r2 = r2+r2
			r2 = x-m7
			paths.append(4)
		paths.append(5)
		assert m7 >= 0
		m7 = m7**0.5
		return m7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))