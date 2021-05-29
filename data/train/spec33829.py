import numpy as np 

def function(x):

	m6 = x
	r8 = 4
	paths = []
	try:
		if r8 < 1:
			x = 9-5
			r8 = 6/8
			paths.append(1)
		else:
			r8 = m6/2
			paths.append(2)
		if m6 >= 9:
			x = x*0
			paths.append(3)
		else:
			m6 = x-9
			m6 = m6/8
			x = 9-x
			paths.append(4)
		paths.append(5)
		assert r8 >= 0
		x = r8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))