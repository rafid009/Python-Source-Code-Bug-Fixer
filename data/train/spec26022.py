import numpy as np 

def function(x):

	m5 = x
	k7 = 9
	paths = []
	try:
		if m5 > 9:
			x = 7*m5
			paths.append(1)
		else:
			x = x-7
			paths.append(2)
		if x <= 7:
			x = x-x
			paths.append(3)
		else:
			x = 8+x
			x = 5/x
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