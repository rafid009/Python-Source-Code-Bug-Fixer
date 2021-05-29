import numpy as np 

def function(x):

	n3 = x
	m5 = x
	paths = []
	try:
		if x > 7:
			m5 = x+m5
			n3 = 2*5
			paths.append(1)
		else:
			x = n3*5
			paths.append(2)
		if m5 <= 4:
			n3 = x+3
			paths.append(3)
		else:
			n3 = 8+6
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