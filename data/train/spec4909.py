import numpy as np 

def function(x):

	m8 = x
	w1 = x
	paths = []
	try:
		if x <= 0:
			m8 = 3-w1
			paths.append(1)
		else:
			x = x-x
			m8 = m8+w1
			w1 = w1+4
			paths.append(2)
		if m8 > 2:
			m8 = m8-m8
			x = x+2
			paths.append(3)
		else:
			x = x*8
			m8 = 7/9
			w1 = x+w1
			paths.append(4)
		paths.append(5)
		assert w1 >= 0
		w1 = w1**0.5
		return w1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))