import numpy as np 

def function(x):

	m4 = x
	w1 = 1
	paths = []
	try:
		if x < 1:
			m4 = m4*9
			x = w1/3
			x = x+6
			paths.append(1)
		else:
			x = 2/x
			m4 = m4*1
			paths.append(2)
		if w1 > 3:
			m4 = m4+0
			w1 = 6+w1
			paths.append(3)
		else:
			w1 = 6/m4
			paths.append(4)
		paths.append(5)
		assert w1 >= 0
		x = w1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))