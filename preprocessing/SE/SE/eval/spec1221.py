import numpy as np 

def function(x):

	m6 = 0
	o1 = x
	paths = []
	try:
		if o1 > 3:
			m6 = o1*o1
			x = x*x
			paths.append(1)
		else:
			m6 = m6-4
			m6 = 9-m6
			o1 = 5-m6
			paths.append(2)
		if x > 5:
			x = 1+x
			paths.append(3)
		else:
			m6 = 3-x
			m6 = o1/7
			x = 1+x
			paths.append(4)
		paths.append(5)
		assert o1 >= 0
		o1 = o1**0.5
		return o1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))