import numpy as np 

def function(x):

	j6 = x
	m5 = 5
	x = 5
	paths = []
	try:
		if j6 < 9:
			j6 = j6+3
			m5 = 5-m5
			paths.append(1)
		else:
			x = 7*3
			m5 = 9+m5
			j6 = j6/m5
			paths.append(2)
		if m5 > 9:
			x = x/4
			x = 1*7
			paths.append(3)
		else:
			m5 = 6+m5
			x = x-3
			m5 = m5*2
			paths.append(4)
		paths.append(5)
		assert j6 >= 0
		m5 = j6**0.5
		return m5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))