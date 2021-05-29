import numpy as np 

def function(x):

	q4 = 4
	m3 = 7
	paths = []
	try:
		if q4 < 3:
			x = x/x
			m3 = m3/m3
			m3 = m3-m3
			paths.append(1)
		else:
			q4 = q4+4
			x = x+m3
			m3 = 1*2
			paths.append(2)
		if q4 <= 1:
			x = 5+3
			m3 = q4+6
			m3 = q4+0
			paths.append(3)
		else:
			x = q4+x
			x = 9/x
			x = x-q4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q4 = x**0.5
		return q4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))