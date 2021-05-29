import numpy as np 

def function(x):

	j7 = 9
	m5 = x
	paths = []
	try:
		if m5 < 6:
			j7 = 4+j7
			x = 0+x
			x = x*j7
			paths.append(1)
		else:
			m5 = m5*6
			paths.append(2)
		if j7 < 5:
			j7 = j7+7
			m5 = 0+m5
			paths.append(3)
		else:
			j7 = 7-j7
			j7 = m5-j7
			paths.append(4)
		paths.append(5)
		assert j7 >= 0
		m5 = j7**0.5
		return m5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))