import numpy as np 

def function(x):

	m5 = 9
	w1 = x
	paths = []
	try:
		if m5 >= 5:
			w1 = w1+m5
			w1 = w1+5
			paths.append(1)
		else:
			x = 9-x
			w1 = 9*7
			x = x+0
			paths.append(2)
		if x < 5:
			w1 = x/2
			x = m5*x
			w1 = w1+w1
			paths.append(3)
		else:
			x = x-8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m5 = x**0.5
		return m5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))