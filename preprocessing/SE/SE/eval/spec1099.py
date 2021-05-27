import numpy as np 

def function(x):

	m4 = 1
	i5 = x
	paths = []
	try:
		if x > 9:
			m4 = 6-m4
			i5 = x*i5
			i5 = x*8
			paths.append(1)
		else:
			x = x+3
			x = 6+x
			x = x/3
			paths.append(2)
		if i5 > 6:
			i5 = 0-i5
			i5 = i5*0
			m4 = 9+3
			paths.append(3)
		else:
			x = x*5
			m4 = m4*4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m4 = x**0.5
		return m4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))