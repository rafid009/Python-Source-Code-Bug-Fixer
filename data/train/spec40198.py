import numpy as np 

def function(x):

	m6 = x
	o2 = 9
	paths = []
	try:
		if x > 5:
			o2 = 2+o2
			x = m6/4
			m6 = o2-m6
			paths.append(1)
		else:
			x = 0/5
			paths.append(2)
		if m6 <= 3:
			x = o2+m6
			o2 = o2*o2
			paths.append(3)
		else:
			m6 = x+o2
			x = 3+x
			m6 = m6-m6
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