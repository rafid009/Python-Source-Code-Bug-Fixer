import numpy as np 

def function(x):

	o1 = x
	m6 = x
	paths = []
	try:
		if x < 0:
			o1 = 5/o1
			x = x+x
			paths.append(1)
		else:
			o1 = 2-o1
			o1 = o1/6
			m6 = 0-m6
			paths.append(2)
		if m6 < 4:
			x = x-x
			o1 = o1+3
			paths.append(3)
		else:
			m6 = m6+m6
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