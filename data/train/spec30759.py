import numpy as np 

def function(x):

	w6 = 4
	m5 = x
	paths = []
	try:
		if m5 >= 5:
			x = x/3
			x = 5-3
			m5 = x-x
			paths.append(1)
		else:
			w6 = w6+5
			x = x/3
			paths.append(2)
		if x < 0:
			w6 = 3/6
			w6 = 7+1
			x = 2/x
			paths.append(3)
		else:
			w6 = 7/w6
			paths.append(4)
		paths.append(5)
		assert m5 >= 0
		m5 = m5**0.5
		return m5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))