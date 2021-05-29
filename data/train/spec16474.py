import numpy as np 

def function(x):

	m6 = x
	r7 = x
	paths = []
	try:
		if m6 > 0:
			r7 = r7*3
			x = 0+1
			r7 = r7/r7
			paths.append(1)
		else:
			m6 = m6-0
			paths.append(2)
		if r7 <= 0:
			r7 = r7-r7
			paths.append(3)
		else:
			x = 6-8
			paths.append(4)
		paths.append(5)
		assert m6 >= 0
		x = m6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))