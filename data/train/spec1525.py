import numpy as np 

def function(x):

	r3 = x
	m9 = 8
	x = 7
	paths = []
	try:
		if x < 5:
			x = 4-2
			r3 = 2+r3
			r3 = r3+m9
			paths.append(1)
		else:
			x = r3-m9
			m9 = x+m9
			paths.append(2)
		if x <= 2:
			r3 = 6*r3
			r3 = r3+8
			paths.append(3)
		else:
			x = x*2
			x = x+4
			m9 = m9-0
			paths.append(4)
		paths.append(5)
		assert r3 >= 0
		m9 = r3**0.5
		return m9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))