import numpy as np 

def function(x):

	m3 = x
	q0 = x
	paths = []
	try:
		if x >= 3:
			m3 = 6-m3
			m3 = m3*4
			x = 6*0
			paths.append(1)
		else:
			m3 = 2/x
			x = x*1
			m3 = 7*m3
			paths.append(2)
		if q0 > 1:
			q0 = 3-7
			m3 = m3*2
			m3 = q0+6
			paths.append(3)
		else:
			x = x+q0
			q0 = q0+7
			paths.append(4)
		paths.append(5)
		assert m3 >= 0
		q0 = m3**0.5
		return q0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))