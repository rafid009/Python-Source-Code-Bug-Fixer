import numpy as np 

def function(x):

	m9 = x
	m5 = 8
	paths = []
	try:
		if x > 5:
			x = 3/7
			m5 = m5/m9
			paths.append(1)
		else:
			x = x-x
			m9 = m5*m9
			paths.append(2)
		if m5 > 4:
			x = x/m9
			x = x/1
			m5 = m5+5
			paths.append(3)
		else:
			x = x+1
			x = 9-x
			paths.append(4)
		paths.append(5)
		assert m9 >= 0
		m5 = m9**0.5
		return m5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))