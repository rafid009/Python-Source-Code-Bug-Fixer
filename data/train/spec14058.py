import numpy as np 

def function(x):

	m2 = x
	n7 = 2
	paths = []
	try:
		if m2 < 0:
			m2 = m2+0
			paths.append(1)
		else:
			n7 = x-3
			x = 1+x
			n7 = 5-8
			paths.append(2)
		if n7 >= 9:
			n7 = n7+x
			x = x*2
			m2 = 1+5
			paths.append(3)
		else:
			n7 = x/2
			paths.append(4)
		paths.append(5)
		assert m2 >= 0
		n7 = m2**0.5
		return n7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))