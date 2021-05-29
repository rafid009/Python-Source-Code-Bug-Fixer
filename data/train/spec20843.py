import numpy as np 

def function(x):

	m5 = x
	q5 = 9
	x = x
	paths = []
	try:
		if q5 < 8:
			x = x+q5
			q5 = q5-q5
			m5 = m5-4
			paths.append(1)
		else:
			x = x-m5
			paths.append(2)
		if m5 < 9:
			m5 = 4+m5
			paths.append(3)
		else:
			q5 = q5*1
			q5 = x*q5
			paths.append(4)
		paths.append(5)
		assert m5 >= 0
		x = m5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))