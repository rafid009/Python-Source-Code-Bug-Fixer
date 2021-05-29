import numpy as np 

def function(x):

	o1 = 0
	m6 = 5
	paths = []
	try:
		if x < 0:
			o1 = 6/1
			x = x+0
			m6 = m6-6
			paths.append(1)
		else:
			o1 = o1-6
			x = 6+3
			m6 = x*3
			paths.append(2)
		if o1 <= 3:
			x = x+8
			x = x/x
			paths.append(3)
		else:
			x = x*8
			o1 = o1*7
			paths.append(4)
		paths.append(5)
		assert o1 >= 0
		m6 = o1**0.5
		return m6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))