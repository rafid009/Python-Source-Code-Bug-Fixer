import numpy as np 

def function(x):

	m5 = 8
	n7 = x
	paths = []
	try:
		if n7 < 4:
			n7 = 4*m5
			n7 = m5/n7
			n7 = x*x
			paths.append(1)
		else:
			m5 = 2-x
			paths.append(2)
		if m5 >= 5:
			n7 = n7+5
			paths.append(3)
		else:
			n7 = x*8
			n7 = 6+n7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))