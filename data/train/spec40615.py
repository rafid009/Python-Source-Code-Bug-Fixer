import numpy as np 

def function(x):

	m1 = x
	o2 = 7
	paths = []
	try:
		if x > 8:
			o2 = o2-o2
			paths.append(1)
		else:
			x = x-3
			paths.append(2)
		if o2 <= 9:
			m1 = m1*5
			o2 = 9-o2
			paths.append(3)
		else:
			x = x+6
			m1 = x/m1
			paths.append(4)
		paths.append(5)
		assert m1 >= 0
		m1 = m1**0.5
		return m1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))