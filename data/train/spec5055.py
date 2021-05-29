import numpy as np 

def function(x):

	m1 = x
	p1 = x
	paths = []
	try:
		if m1 < 6:
			x = p1/x
			paths.append(1)
		else:
			x = 7-1
			x = x-x
			paths.append(2)
		if x < 5:
			p1 = p1/9
			x = 7*m1
			p1 = 6-m1
			paths.append(3)
		else:
			m1 = p1*0
			p1 = p1/9
			paths.append(4)
		paths.append(5)
		assert p1 >= 0
		m1 = p1**0.5
		return m1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))