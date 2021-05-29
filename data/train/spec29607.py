import numpy as np 

def function(x):

	n0 = x
	m1 = x
	paths = []
	try:
		if x <= 7:
			m1 = n0/n0
			m1 = n0/m1
			x = 1*0
			paths.append(1)
		else:
			m1 = 5-m1
			x = 9*x
			x = x/1
			paths.append(2)
		if m1 <= 4:
			n0 = n0+n0
			x = x/9
			paths.append(3)
		else:
			x = x/9
			n0 = 5+2
			n0 = x+n0
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