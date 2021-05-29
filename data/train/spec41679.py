import numpy as np 

def function(x):

	m3 = 9
	q5 = x
	paths = []
	try:
		if q5 >= 8:
			q5 = q5/q5
			m3 = m3-3
			m3 = 6+2
			paths.append(1)
		else:
			q5 = 4-m3
			paths.append(2)
		if x > 2:
			m3 = 1/x
			m3 = m3*0
			paths.append(3)
		else:
			m3 = m3*q5
			x = x*x
			paths.append(4)
		paths.append(5)
		assert q5 >= 0
		x = q5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))