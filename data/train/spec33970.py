import numpy as np 

def function(x):

	n7 = 6
	m2 = x
	paths = []
	try:
		if n7 < 1:
			m2 = m2-9
			paths.append(1)
		else:
			x = 6+x
			paths.append(2)
		if m2 <= 9:
			n7 = 4-n7
			paths.append(3)
		else:
			n7 = x*1
			paths.append(4)
		paths.append(5)
		assert m2 >= 0
		x = m2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))