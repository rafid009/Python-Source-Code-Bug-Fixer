import numpy as np 

def function(x):

	r7 = x
	m9 = x
	paths = []
	try:
		if x <= 7:
			m9 = 6+m9
			paths.append(1)
		else:
			r7 = m9/m9
			r7 = r7*1
			paths.append(2)
		if x > 2:
			r7 = r7-r7
			x = 4-x
			paths.append(3)
		else:
			r7 = 6+r7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r7 = x**0.5
		return r7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))