import numpy as np 

def function(x):

	j7 = 1
	m3 = x
	paths = []
	try:
		if j7 > 7:
			j7 = j7-0
			x = x/4
			x = 4*2
			paths.append(1)
		else:
			x = 0/x
			j7 = j7*9
			paths.append(2)
		if x < 0:
			x = x/8
			m3 = 0*m3
			x = m3+m3
			paths.append(3)
		else:
			x = m3/j7
			paths.append(4)
		paths.append(5)
		assert m3 >= 0
		m3 = m3**0.5
		return m3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))