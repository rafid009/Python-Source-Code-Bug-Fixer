import numpy as np 

def function(x):

	o1 = 3
	m5 = 5
	paths = []
	try:
		if o1 >= 1:
			o1 = 0/o1
			o1 = o1-9
			m5 = 5-4
			paths.append(1)
		else:
			o1 = m5+x
			paths.append(2)
		if m5 <= 3:
			x = x*6
			paths.append(3)
		else:
			o1 = 5*m5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o1 = x**0.5
		return o1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))